"""Public interface for domain-based logging subsystem.

Provides centralized management of application logging with domain isolation,
flexible configuration and proper resource cleanup. Designed for complex
multi-module applications with different logging requirements per component.

Refferences:
    https://github.com/a-ulianov/logging-manage-module

Key Features:
- Domain-based logger hierarchy (api, business, core, etc.)
- Thread-safe operations
- Async/sync logging support
- Clean resource termination
- Custom handler integration

Exported Classes:
    LoggerManager: Manages logging lifecycle for specific domain
    LoggingSettings: Configuration model for logging parameters

Example Usage:
    Basic Configuration:
    >>> from src import LoggerManager, LoggingSettings
    >>>
    >>> # Initialize for API domain
    >>> api_manager = LoggerManager('api')
    >>> api_manager.configure(LoggingSettings(JSON=False, LEVEL='INFO'))
    >>>
    >>> # Get loggers
    >>> root_logger = api_manager.get_logger()  # 'api'
    >>> auth_logger = api_manager.get_logger('v1.auth')  # 'api.v1.auth'

Advanced Usage with Custom Handlers:
    >>> from logging.handlers import SysLogHandler
    >>>
    >>> def create_custom_handlers(settings, formatter):
    ...     syslog = SysLogHandler(address=('logs.example.com', 514))
    ...     syslog.setFormatter(formatter)
    ...     return [syslog]
    >>>
    >>> manager = LoggerManager('custom')
    >>> manager.configure(
    ...     LoggingSettings(),
    ...     custom_handler_factory=create_custom_handlers
    ... )

Configuration Parameters:
    LoggerManager.configure() accepts:
    - settings: LoggingSettings - Core logging configuration
    - custom_handler_factory: Callable[[LoggingSettings, logging.Formatter],
                                List[logging.Handler]] - Optional factory function
      that receives settings and formatter, and returns additional handlers to add
      to the logging pipeline. Handlers are automatically cleaned up during shutdown.

Shutdown Behavior:
    - Stops all logging operations for the domain
    - Removes all handlers (including custom handlers) and clears queues
    - Breaks parent-child relationships
    - After shutdown, loggers become non-functional
    - Required before reconfiguration
    - Automatically called in destructor

Warning:
    - Avoid premature shutdown as it will immediately stop all logging
      for the entire domain and its child loggers
    - Custom handlers must be thread-safe if used in async mode
    - Handler cleanup is automatic but implementations should properly
      close their resources
"""

__all__ = ['LoggerManager', 'LoggingSettings', 'ozonapi_logger', 'manager']

from .manager import LoggerManager
from .config import LoggingSettings

manager = LoggerManager('ozonapi')
manager.configure(LoggingSettings())

ozonapi_logger = manager.get_logger()


class Logger:
    pass