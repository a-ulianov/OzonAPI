"""Тесты получения активных клиентов."""
from src.ozonapi.seller.core.rate_limiter import RateLimiterManager


class TestRateLimiterManagerActiveClients:
    """Тесты получения активных клиентов."""

    def test_get_active_client_ids_with_active_instances(self, mock_api_manager):
        """Тест получения активных client_id."""
        RateLimiterManager.get_or_register_instance(mock_api_manager)

        active_clients = RateLimiterManager.get_active_client_ids()

        assert mock_api_manager.client_id in active_clients
        assert len(active_clients) >= 1

    def test_get_active_client_ids_empty(self):
        """Тест получения активных client_id когда нет активных инстансов."""
        RateLimiterManager._clients.clear()

        active_clients = RateLimiterManager.get_active_client_ids()

        assert active_clients == []