from unittest.mock import patch, AsyncMock

import pytest

from src.ozonapi.seller import SellerAPI
from src.ozonapi.seller.core import APIManager, MethodRateLimiterManager


@pytest.fixture
def api():
    """Фикстура для создания экземпляра SellerWarehouseAPI."""
    return SellerAPI(client_id="test_client", api_key="test_api_key")


@pytest.fixture
def mock_api_request():
    """Фикстура для мока метода _request APIManager."""
    with patch.object(APIManager, '_request', new_callable=AsyncMock) as mock_request:
        yield mock_request


@pytest.fixture(autouse=True)
def mock_method_rate_limiter():
    """Фикстура для мока MethodRateLimiterManager.get_limiter (применяется автоматически ко всем тестам)."""
    with patch.object(MethodRateLimiterManager, 'get_limiter', new_callable=AsyncMock) as mock_get_limiter:
        mock_limiter = AsyncMock()
        mock_limiter.__aenter__ = AsyncMock(return_value=None)
        mock_limiter.__aexit__ = AsyncMock(return_value=None)
        mock_get_limiter.return_value = mock_limiter
        yield mock_get_limiter