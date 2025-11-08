"""Тесты инициализации RateLimiterManager."""
from src.ozonapi.seller.core.rate_limiter import RateLimiterManager, Register


class TestRateLimiterManagerInitialization:
    """Тесты инициализации RateLimiterManager."""

    def test_rate_limiter_manager_creation(self, rate_limiter_manager, mock_api_manager):
        """Тест создания RateLimiterManager."""
        assert rate_limiter_manager._instance_data is not None
        assert rate_limiter_manager._instance_limiter is not None
        assert rate_limiter_manager._client_limiter is not None
        assert rate_limiter_manager._logger is not None

    def test_client_registry_created(self, rate_limiter_manager, mock_api_manager):
        """Тест создания регистра клиента."""
        client_id = mock_api_manager.client_id

        assert client_id in RateLimiterManager._clients
        assert isinstance(RateLimiterManager._clients[client_id], Register)