"""Общие фикстуры для тестирования."""
import pytest
from unittest.mock import Mock
import asyncio


@pytest.fixture
def mock_logger():
    """Создает мок логгера."""
    logger = Mock()
    logger.debug = Mock()
    logger.info = Mock()
    logger.warning = Mock()
    logger.error = Mock()
    return logger


@pytest.fixture
def mock_client_data():
    """Создает тестовые данные клиента."""
    def create_client(client_id="test_client", api_key="test_key", token=None):
        return {
            "client_id": client_id,
            "api_key": api_key,
            "token": token
        }
    return create_client


@pytest.fixture(scope="session")
def event_loop():
    """Создает event loop для тестов."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()