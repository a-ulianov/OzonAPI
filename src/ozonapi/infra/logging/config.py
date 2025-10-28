"""Logging subsystem configuration model.

This module defines the Pydantic model used to configure all aspects
of application logging behavior, including:
- Log levels and formatting
- Output destinations (console, file)
- Async logging configuration
- Log rotation settings
"""
from typing import Optional

from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings

class LoggingSettings(BaseSettings):
    """Pydantic model for logging configuration parameters.

    Attributes:
        NAME: Logger name. Defaults to '' (ROOT).
        LEVEL: Minimum logging level. Defaults to 'INFO'.
        JSON: Enable JSON formatting for machine-readable logs.
            Defaults to False.
        FORMAT: Format string for text-based logs. Defaults to
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'.
        USE_ASYNC: Enable non-blocking asynchronous logging.
            Defaults to True.
        MAX_QUEUE_SIZE: Maximum queue size for async logging (Prevent infinite queue growth).
            Defaults to 1000.
        DIR: Directory path for log files. Required if file logging
            is enabled. Defaults to 'logs'.
        FILE: Base filename for logs. Required if file logging is
            enabled. Defaults to 'app.log'.
        MAX_BYTES: Maximum log file size in bytes before rotation.
            Defaults to 10MB.
        BACKUP_FILES_COUNT: Number of backup logs to retain. Defaults to 5.

    Environment variables:
        All parameters can be set via environment variables with 'LOG_' prefix.
        Example: LOG_LEVEL='DEBUG' sets the logging level.
    """

    NAME: str = ''
    LEVEL: str = Field('INFO', pattern='^(DEBUG|INFO|WARNING|ERROR|CRITICAL)$')
    JSON: bool = False
    FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    USE_ASYNC: bool = Field(True, description='Enable async logging')
    MAX_QUEUE_SIZE: int = Field(10000, description='Limit queue size (for async mode only)')
    DIR: Optional[str] = None
    FILE: Optional[str] = None
    MAX_BYTES: int = 10 * 1024 * 1024  # 10MB
    BACKUP_FILES_COUNT: int = 5

    # model_config = ConfigDict(
    #     env_prefix='LOG_',      #type: ignore
    #     case_sensitive=False,   #type: ignore
    # )
