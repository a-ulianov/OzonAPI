"""Фикстуры для тестирования SessionManager."""
import pytest
from unittest.mock import Mock, AsyncMock

from src.ozonapi.seller.core.sessions import SessionManager


@pytest.fixture
def session_manager(mock_logger):
    """Создает экземпляр SessionManager для тестирования."""
    return SessionManager(
        timeout=30.0,
        connector_limit=100,
        instance_logger=mock_logger
    )


@pytest.fixture
def mock_client_session():
    """Создает мок ClientSession."""
    session = AsyncMock()
    session.closed = False
    session.close = AsyncMock()
    return session