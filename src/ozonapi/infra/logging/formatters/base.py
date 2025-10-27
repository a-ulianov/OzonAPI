"""JSON formatter for structured logging output.

Converts log records into JSON format suitable for machine processing
and log aggregation systems like ELK or Splunk.
"""

import logging
import json
from datetime import datetime


class JsonFormatter(logging.Formatter):
    """Formats log records as JSON strings with structured data.

    Produces output containing:
    - Timestamp in ISO8601 format
    - Log level
    - Logger name
    - Message content
    - Additional context (when available)
    """

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON.

        Args:
            record: Log record to format.

        Returns:
            JSON string with log data.
        """
        log_entry = {
            'timestamp': datetime.fromtimestamp(record.created).isoformat() + 'Z',
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'context': getattr(record, 'context', {})
        }
        return json.dumps(log_entry)


def get_formatter(json_output: bool, fmt: str) -> logging.Formatter:
    """Get appropriate formatter.

    Args:
        json_output: Whether to use JSON format.
        fmt: Format string for text output.

    Returns:
        Configured formatter instance.
    """
    return JsonFormatter() if json_output else logging.Formatter(fmt)