"""
Centralized management of application logging lifecycle.

Implements domain-based logging architecture with flexible configuration
and proper resource cleanup.
"""

import logging
import weakref
from logging.handlers import QueueHandler
from queue import Queue
from typing import Iterable

from .factory import LoggingFactory
from .config import LoggingSettings


class LoggerManager:
    """Manages logging components lifecycle for a specific domain.

    Features:
    - Domain isolation (api, business, core, etc.)
    - Thread-safe operations
    - Automatic resource cleanup
    """

    def __init__(self, domain: str):
        """Initialize manager for specified domain.

        Args:
            domain: Root namespace for loggers (e.g. 'api', 'business')
        """
        self._domain = domain
        self._managed_loggers = weakref.WeakValueDictionary()
        self._listener = None
        self._is_configured = False
        self._default_settings = None
        self._formatter = None

    def configure(
            self,
            settings: LoggingSettings = LoggingSettings(),
            custom_handler_factory: callable = None
    ) -> None:
        """Configure logging domain with specified settings.

        Args:
            settings: Configuration parameters
            custom_handler_factory: Optional callable that takes settings and formatter,
                and returns a list of additional handlers to add to the pipeline.
                Signature: (LoggingSettings, logging.Formatter) -> List[logging.Handler]

        Raises:
            RuntimeError: If already configured or conflict detected
        """
        if self._is_configured:
            raise RuntimeError('LoggerManager already configured. Call shutdown() first.')

        existing_logger = logging.getLogger(self._domain)
        if existing_logger.handlers and existing_logger not in self._managed_loggers.values():
            raise RuntimeError(f"Domain '{self._domain}' already configured by another manager")

        self._default_settings = settings
        factory = LoggingFactory(settings)

        root_logger, self._listener = factory.create_logging_pipeline(self._domain)
        self._formatter = root_logger.handlers[0].formatter if root_logger.handlers else None

        # Add custom handlers if factory provided
        if custom_handler_factory is not None:
            self._add_custom_handlers(root_logger, settings, custom_handler_factory)

        self._managed_loggers[self._domain] = root_logger
        self._is_configured = True

    def get_logger(self, module_path: str = None) -> logging.Logger:
        """Get or create logger for specific module.

        Args:
            module_path: Relative path within domain (e.g. 'v1.auth' for api.v1.auth)

        Returns:
            Configured logger instance
        """
        if not self._is_configured:
            raise RuntimeError('LoggerManager is not configured')

        full_name = self._get_full_logger_name(module_path)

        if full_name not in self._managed_loggers:
            logger = logging.getLogger(full_name)
            logger.propagate = False
            logger.setLevel(self._default_settings.LEVEL)

            # Get root domain logger
            root_logger = self._managed_loggers.get(self._domain)
            if not root_logger:
                return logger

            self._copy_logger(root_logger, logger)

            self._managed_loggers[full_name] = logger

        return self._managed_loggers[full_name]

    def _get_full_logger_name(self, module_path: str | None) -> str:
        """Construct full logger name from domain and module path.

        Args:
            module_path: Relative path within domain

        Returns:
            Fully qualified logger name
        """
        return f"{self._domain}.{module_path}" if module_path else self._domain

    @staticmethod
    def _cleanup_logger_handlers(logger: logging.Logger) -> None:
        """Remove and close all handlers from logger.

        Args:
            logger: Logger instance to clean up
        """
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
            handler.close()

    @staticmethod
    def _cleanup_logger_formatters(logger: logging.Logger) -> None:
        """Remove formatters from all logger handlers.

        Args:
            logger: Logger instance to clean up
        """
        for handler in logger.handlers:
            handler.setFormatter(None)

    def _copy_handler(self, handler: logging.Handler) -> logging.Handler:
        """Create new handler instance with same configuration as source.

        Args:
            handler: Source handler to copy

        Returns:
            New handler instance with identical configuration
        """
        if isinstance(handler, logging.StreamHandler):
            new_handler = logging.StreamHandler()
        elif isinstance(handler, logging.handlers.RotatingFileHandler):
            new_handler = logging.handlers.RotatingFileHandler(
                filename=handler.baseFilename,
                maxBytes=handler.maxBytes,
                backupCount=handler.backupCount,
                encoding=handler.encoding
            )
        elif isinstance(handler, logging.handlers.QueueHandler):
            queue = self._listener.queue if hasattr(self, '_listener') and self._listener else Queue()
            new_handler = logging.handlers.QueueHandler(queue)
        else:
            new_handler = type(handler)()

        new_handler.setLevel(handler.level)
        return new_handler

    def _copy_logger(self, source: logging.Logger, target: logging.Logger) -> None:
        """Copy handlers and configuration from source to target logger.

        Args:
            source: Logger to copy configuration from
            target: Logger to apply configuration to
        """
        for handler in source.handlers:
            new_handler = self._copy_handler(handler)
            if handler.formatter:
                new_handler.setFormatter(handler.formatter)
            target.addHandler(new_handler)

        target.setLevel(source.level)

    def shutdown(self) -> None:
        """Clean up all logging resources for this domain."""
        if not self._is_configured:
            return

        for logger in self._managed_loggers.values():
            self._cleanup_logger(logger)
        self._managed_loggers.clear()

        if self._listener:
            self._listener.stop()
            self._listener = None

        self._is_configured = False

    @staticmethod
    def _cleanup_logger(logger: logging.Logger) -> None:
        """Safely remove all logger components."""
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
            handler.close()
        logger.filters.clear()

    def _add_custom_handlers(self, logger, settings, handler_factory):
        """Add custom handlers to logger"""
        if callable(handler_factory):
            custom_handlers = handler_factory(settings, self._formatter)
            if not isinstance(custom_handlers, Iterable):
                raise TypeError('Handler factory must be iterable')
            for handler in custom_handlers:
                if isinstance(handler, logging.Handler):
                    logger.addHandler(handler)
                else:
                    raise TypeError(f'Handler `{handler}` is not a logging.Handler')
        else:
            raise TypeError(f'Handler `{handler_factory}` is not callable')

    def __enter__(self) -> 'LoggerManager':
        """Context manager realisation"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Completion of work of context manager with correct resources cleaning"""
        self.shutdown()

    def __del__(self):
        """Safety cleanup."""
        self.shutdown()