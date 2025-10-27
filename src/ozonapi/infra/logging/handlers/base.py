"""Base implementations of logging handlers for the application.

This module contains essential handler implementations used by the logging system,
including console and file handlers with rotation support. Handlers are designed
to work in both synchronous and asynchronous logging configurations.
"""

import logging
import os
from logging.handlers import RotatingFileHandler
from typing import List
from ..config import LoggingSettings


def create_handlers(
        settings: LoggingSettings,
        formatter: logging.Formatter
) -> List[logging.Handler]:
    """Create configured output handlers.

    Args:
        settings: Logging configuration.
        formatter: Formatter for handlers.

    Returns:
        List of initialized logging handlers.
    """
    handlers = []

    # Standard console output
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    handlers.append(console)

    # Optional file output
    if settings.DIR and settings.FILE:
        file_handler = RotatingFileHandler(
            filename=os.path.join(settings.DIR, settings.FILE),
            maxBytes=settings.MAX_BYTES,
            backupCount=settings.BACKUP_FILES_COUNT,
            encoding='utf-8'
        )
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)

    return handlers