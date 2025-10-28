"""Unit tests for infrastructure/logging module."""

import json
import logging
import os
from logging.handlers import QueueHandler, RotatingFileHandler
from pathlib import Path
from typing import Generator

import pytest

from src.ozonapi.infra.logging import LoggerManager, LoggingSettings


class TestLogging:
    """Test suite for logging infrastructure."""

    @pytest.fixture
    def temp_log_dir(self, tmp_path: Path) -> Path:
        """Fixture providing temporary directory for log files."""
        return tmp_path / "logs"

    @pytest.fixture
    def env_vars(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Fixture setting up environment variables for testing."""
        monkeypatch.setenv("LOG_LEVEL", "DEBUG")
        monkeypatch.setenv("LOG_JSON", "true")
        monkeypatch.setenv("LOG_USE_ASYNC", "false")
        monkeypatch.setenv("LOG_MAX_QUEUE_SIZE", "500")

    @pytest.fixture
    def default_manager(self) -> Generator[LoggerManager, None, None]:
        """Fixture providing configured LoggerManager with default settings."""
        manager = LoggerManager("test")
        settings = LoggingSettings(LEVEL="DEBUG", JSON=False, USE_ASYNC=False)
        manager.configure(settings)
        yield manager
        manager.shutdown()

    # def test_environment_variables_loading(self, env_vars: None) -> None:
    #     """Test that environment variables are loaded correctly with LOG_ prefix."""
    #     settings = LoggingSettings()
    #     assert settings.LEVEL == "DEBUG"
    #     assert settings.JSON is True
    #     assert settings.USE_ASYNC is False
    #     assert settings.MAX_QUEUE_SIZE == 500

    def test_manager_initialization(self) -> None:
        """Test that LoggerManager is initialized correctly."""
        manager = LoggerManager("test_domain")
        assert manager._domain == "test_domain"
        assert not manager._is_configured
        assert len(manager._managed_loggers) == 0
        manager.shutdown()

    def test_manager_configuration(self, default_manager: LoggerManager) -> None:
        """Test that LoggerManager configuration works correctly."""
        assert default_manager._is_configured
        assert logging.getLogger("test").level == logging.DEBUG
        assert len(logging.getLogger("test").handlers) > 0

    def test_reconfiguration_raises_exception(self, default_manager: LoggerManager) -> None:
        """Test that reconfiguring a manager raises RuntimeError."""
        with pytest.raises(RuntimeError, match="already configured"):
            default_manager.configure(LoggingSettings())

    def test_duplicate_domain_raises_exception(self, default_manager: LoggerManager) -> None:
        """Test that creating another manager for same domain raises RuntimeError."""
        with pytest.raises(RuntimeError, match="already configured by another manager"):
            manager2 = LoggerManager("test")
            manager2.configure(LoggingSettings())
            manager2.shutdown()

    def test_unconfigured_manager_raises_exception(self) -> None:
        """Test that getting logger from unconfigured manager raises RuntimeError."""
        manager = LoggerManager("unconfigured")
        with pytest.raises(RuntimeError, match="not configured"):
            manager.get_logger()
        manager.shutdown()

    def test_logger_naming(self, default_manager: LoggerManager) -> None:
        """Test that loggers are named correctly with domain hierarchy."""
        root_logger = default_manager.get_logger()
        assert root_logger.name == "test"

        sub_logger = default_manager.get_logger("sub.module")
        assert sub_logger.name == "test.sub.module"

    def test_format_change(self) -> None:
        """Test that log message format can be changed."""
        custom_format = "%(levelname)s - %(message)s"
        manager = LoggerManager("format_test")
        settings = LoggingSettings(FORMAT=custom_format, JSON=False, USE_ASYNC=False)
        manager.configure(settings)

        logger = manager.get_logger()
        # Find a non-QueueHandler to check the formatter
        handler = next(h for h in logger.handlers if not isinstance(h, QueueHandler))
        assert isinstance(handler.formatter, logging.Formatter)
        assert handler.formatter._fmt == custom_format
        manager.shutdown()

    def test_subdomain_logger_inheritance(self, default_manager: LoggerManager) -> None:
        """Test that subdomain loggers inherit settings from parent domain."""
        root_logger = default_manager.get_logger()
        sub_logger = default_manager.get_logger("sub")

        assert sub_logger.level == root_logger.level
        assert len(sub_logger.handlers) == len(root_logger.handlers)

    def test_console_logger_output(self, capsys: pytest.CaptureFixture) -> None:
        """Test that console logger outputs messages correctly."""
        manager = LoggerManager("console_test")
        settings = LoggingSettings(
            USE_ASYNC=False,  # Disable async to test console output directly
            JSON=False,  # Ensure we're using text format
            FORMAT='%(message)s'  # Simple format for easier testing
        )
        manager.configure(settings)

        logger = manager.get_logger()
        test_message = "Test console output"
        logger.info(test_message)

        captured = capsys.readouterr()
        # Check both stdout and stderr as logging can use either
        assert test_message in captured.out or test_message in captured.err
        manager.shutdown()

    def test_json_logging(self) -> None:
        """Test that JSON logging produces valid JSON output."""
        manager = LoggerManager("json_test")
        settings = LoggingSettings(JSON=True, USE_ASYNC=False)
        manager.configure(settings)

        logger = manager.get_logger()
        # Get the first non-QueueHandler
        handler = next(h for h in logger.handlers if not isinstance(h, QueueHandler))

        # Create a test record
        record = logging.LogRecord(
            name="json_test",
            level=logging.INFO,
            pathname=__file__,
            lineno=1,
            msg="Test JSON output",
            args=None,
            exc_info=None
        )

        formatted = handler.formatter.format(record)
        assert json.loads(formatted)  # Will raise if not valid JSON
        manager.shutdown()

    def test_file_logging_parameters(self, temp_log_dir: Path) -> None:
        """Test that file logging parameters are set correctly."""
        temp_log_dir.mkdir(parents=True, exist_ok=True)  # Create directory first
        manager = LoggerManager("file_test")
        settings = LoggingSettings(
            DIR=str(temp_log_dir),
            FILE="test.log",
            MAX_BYTES=1024,
            BACKUP_FILES_COUNT=3,
            USE_ASYNC=False
        )
        manager.configure(settings)

        logger = manager.get_logger()
        file_handlers = [h for h in logger.handlers if isinstance(h, RotatingFileHandler)]
        assert len(file_handlers) == 1

        handler = file_handlers[0]
        assert str(temp_log_dir) in handler.baseFilename
        assert handler.maxBytes == 1024
        assert handler.backupCount == 3
        manager.shutdown()

    def test_file_logging_output(self, temp_log_dir: Path) -> None:
        """Test that messages are written to log files."""
        temp_log_dir.mkdir(parents=True, exist_ok=True)  # Create directory first
        file_name = "output_test.log"
        log_file = os.path.join(temp_log_dir, file_name)
        manager = LoggerManager("file_output_test")
        settings = LoggingSettings(DIR=str(temp_log_dir), FILE=file_name, USE_ASYNC=False)
        manager.configure(settings)

        logger = manager.get_logger()
        test_message = "Test file output"
        logger.info(test_message)

        # Ensure the message was written to file
        assert os.path.exists(log_file)
        with open(log_file) as f:
            content = f.read()
            assert test_message in content
        manager.shutdown()

    def test_async_logging_configuration(self) -> None:
        """Test that async logging is configured with queues."""
        manager = LoggerManager("async_test")
        settings = LoggingSettings(USE_ASYNC=True)
        manager.configure(settings)

        logger = manager.get_logger()
        queue_handlers = [h for h in logger.handlers if isinstance(h, QueueHandler)]
        assert len(queue_handlers) == 1
        assert manager._listener is not None
        manager.shutdown()

    def test_queue_size_parameter(self) -> None:
        """Test that max queue size parameter is respected."""
        manager = LoggerManager("queue_test")
        settings = LoggingSettings(USE_ASYNC=True, MAX_QUEUE_SIZE=10)
        manager.configure(settings)

        assert manager._listener is not None
        assert manager._listener.queue.maxsize == 10
        manager.shutdown()

    def test_custom_handler_factory(self, temp_log_dir: Path, capsys: pytest.CaptureFixture):
        """Test that custom_handler_factory properly integrates custom handlers."""
        # Setup
        temp_log_dir.mkdir(parents=True, exist_ok=True)
        test_log_file = 'test.log'

        # Track created handlers for cleanup verification
        test_handlers = []

        def create_custom_handlers(settings: LoggingSettings, formatter: logging.Formatter):
            """Test custom handler factory that creates multiple handler types."""
            nonlocal test_handlers

            # Create a MemoryHandler that writes to StringIO
            memory_handler = logging.handlers.MemoryHandler(capacity=10)
            memory_handler.setFormatter(formatter)
            memory_handler.setLevel(settings.LEVEL)
            test_handlers.append(memory_handler)

            # Create a SysLogHandler (mocked to stdout for testing)
            syslog = logging.StreamHandler()
            syslog.setFormatter(logging.Formatter('SYSLOG: %(message)s'))
            syslog.setLevel(settings.LEVEL)  # Explicitly set level from settings
            test_handlers.append(syslog)

            return [memory_handler, syslog]

        # Test configuration with custom factory
        manager = LoggerManager('custom_test')
        settings = LoggingSettings(
            LEVEL='WARNING',
            JSON=False,
            USE_ASYNC=False,
            DIR=str(temp_log_dir),
            FILE=test_log_file,
            FORMAT='%(levelname)s - %(message)s'
        )
        manager.configure(settings, custom_handler_factory=create_custom_handlers)

        # Verify handler integration
        logger = manager.get_logger()

        # Should have:
        # 1. Default console handler
        # 2. File handler (since DIR specified)
        # 3. Custom memory handler
        # 4. Custom syslog handler
        assert len(logger.handlers) >= 4

        # Verify custom handlers were properly configured
        for handler in test_handlers:
            assert handler in logger.handlers
            assert handler.level == logging.WARNING  # From settings
            assert handler.formatter is not None

        # Test logging functionality
        test_message = "Custom handler test message"
        logger.warning(test_message)

        # Verify output contains our message
        captured = capsys.readouterr()
        assert test_message in captured.out or test_message in captured.err

        # Verify shutdown cleanup
        manager.shutdown()
        for handler in test_handlers:
            if hasattr(handler, 'closed'):  # Only MemoryHandler has closed attribute
                assert handler.closed is True
            else:  # For StreamHandler, verify it's not in logger anymore
                assert handler not in logging.getLogger('custom_test').handlers

    def test_custom_handler_factory_not_callable_raises_exception(self, temp_log_dir: Path) -> None:
        """Test that non-callable custom_handler_factory raises TypeError."""
        manager = LoggerManager("not_callable_test")
        settings = LoggingSettings(
            LEVEL="INFO",
            DIR=None,
            USE_ASYNC=False
        )

        # Test with non-callable factory (using a string as example)
        with pytest.raises(TypeError, match="is not callable"):
            manager.configure(settings, custom_handler_factory="not_a_callable")

        manager.shutdown()

    def test_custom_handler_factory_non_iterable_return_raises_exception(self, temp_log_dir: Path) -> None:
        """Test that custom_handler_factory returning non-iterable raises TypeError."""
        manager = LoggerManager("non_iterable_test")
        settings = LoggingSettings(
            LEVEL="INFO",
            DIR=None,
            USE_ASYNC=False
        )

        # Factory that returns a non-iterable (using int as example)
        def bad_factory(*args, **kwargs):
            return 42

        with pytest.raises(TypeError, match="must be iterable"):
            manager.configure(settings, custom_handler_factory=bad_factory)

        manager.shutdown()

    def test_custom_handler_factory_non_handler_objects_raises_exception(self, temp_log_dir: Path) -> None:
        """Test that custom_handler_factory returning non-handler objects raises TypeError."""
        manager = LoggerManager("non_handler_test")
        settings = LoggingSettings(
            LEVEL="INFO",
            DIR=None,
            USE_ASYNC=False
        )

        # Factory that returns a mix of valid and invalid objects
        def bad_factory(_, formatter):
            valid_handler = logging.StreamHandler()
            valid_handler.setFormatter(formatter)
            return [valid_handler, "not_a_handler", 42]  # Contains non-handler objects

        with pytest.raises(TypeError, match="is not a logging.Handler"):
            manager.configure(settings, custom_handler_factory=bad_factory)

        manager.shutdown()

    def test_shutdown_cleanup(self, default_manager: LoggerManager) -> None:
        """Test that shutdown cleans up all resources."""
        logger = default_manager.get_logger()
        assert len(logger.handlers) > 0

        default_manager.shutdown()
        assert len(logger.handlers) == 0
        assert not default_manager._is_configured
        assert len(default_manager._managed_loggers) == 0