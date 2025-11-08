"""Тесты инициализации SessionManager."""
from src.ozonapi.seller.core.sessions import SessionManager


class TestSessionManagerInitialization:
    """Тесты инициализации SessionManager."""

    def test_session_manager_creation(self, session_manager, mock_logger):
        """Тест создания SessionManager."""
        assert session_manager._sessions == {}
        assert session_manager._session_refs == {}
        assert session_manager._lock is not None
        assert session_manager._logger is mock_logger

    def test_session_manager_default_parameters(self, mock_logger):
        """Тест параметров по умолчанию."""
        manager = SessionManager(instance_logger=mock_logger)

        assert manager._timeout.total == 30.0
        assert manager._connector_limit == 100