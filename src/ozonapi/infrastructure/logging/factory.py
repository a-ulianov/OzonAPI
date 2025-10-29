"""Factory for creating configured logging pipelines.

This module contains the LoggingFactory class which constructs complete
logging systems based on configuration settings, including both synchronous
and asynchronous logging setups.
"""

import logging
from logging.handlers import QueueHandler, QueueListener
from queue import Queue
from typing import Optional
from .config import LoggingSettings
from .handlers import create_handlers
from .formatters import get_formatter


class LoggingFactory:
    """Constructs and configures complete logging pipelines.

    Handles:
    - Logger instantiation
    - Handler attachment
    - Formatter configuration
    - Async/sync mode switching
    """

    def __init__(self, settings: LoggingSettings):
        self.settings = settings

    def create_logging_pipeline(
            self,
            logger_name: str | None = None
    ) -> tuple[logging.Logger, Optional[QueueListener]]:
        """Create complete logging pipeline.

        Returns:
            Tuple of (root logger, optional listener for async mode).
        """
        logger = logging.getLogger(self.settings.NAME if logger_name is None else logger_name)
        self._configure_logger(logger)
        return self._create_pipeline(logger)

    def _configure_logger(self, logger: logging.Logger) -> None:
        """Configure base logger settings."""
        logger.setLevel(self.settings.LEVEL)
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
            handler.close()
        logger.propagate = False

    def _create_pipeline(self, logger: logging.Logger) -> tuple[logging.Logger, Optional[QueueListener]]:
        """Create sync/async logging pipeline."""
        formatter = get_formatter(self.settings.JSON, self.settings.FORMAT)
        handlers = create_handlers(self.settings, formatter)

        if not self.settings.USE_ASYNC:
            for handler in handlers:
                logger.addHandler(handler)
            return logger, None

        log_queue = Queue(maxsize=self.settings.MAX_QUEUE_SIZE)
        queue_handler = QueueHandler(log_queue)
        listener = QueueListener(log_queue, *handlers)

        logger.addHandler(queue_handler)
        listener.start()

        return logger, listener