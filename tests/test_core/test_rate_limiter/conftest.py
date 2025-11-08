"""Фикстуры и моки для тестирования RateLimiterManager."""
import pytest
from unittest.mock import Mock, AsyncMock

from src.ozonapi.seller.core.rate_limiter import RateLimiterManager, InstanceData


@pytest.fixture
def mock_api_manager():
    """Создает мок APIManager."""
    mock_manager = Mock()
    mock_manager.client_id = "test_client_123"
    mock_manager.config = Mock()
    mock_manager.config.max_requests_per_second = 10
    mock_manager.config.min_instance_ttl = 300.0
    return mock_manager


@pytest.fixture
def rate_limiter_manager(mock_api_manager, mock_logger):
    """Создает экземпляр RateLimiterManager для тестирования."""
    # Очищаем глобальное состояние перед тестом
    RateLimiterManager._clients.clear()
    return RateLimiterManager(instance=mock_api_manager, logger=mock_logger)


@pytest.fixture
def instance_data(mock_api_manager):
    """Создает экземпляр InstanceData для тестирования."""
    return InstanceData(instance=mock_api_manager)
