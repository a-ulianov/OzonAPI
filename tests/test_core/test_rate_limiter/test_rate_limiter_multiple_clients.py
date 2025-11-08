"""Тесты работы с несколькими клиентами."""
from unittest.mock import Mock

from src.ozonapi.seller.core.rate_limiter import RateLimiterManager


class TestRateLimiterManagerMultipleClients:
    """Тесты работы с несколькими клиентами."""

    def test_multiple_clients_isolation(self):
        """Тест изоляции между разными клиентами."""
        client1 = Mock()
        client1.client_id = "client_1"
        client1.config = Mock()
        client1.config.max_requests_per_second = 10

        client2 = Mock()
        client2.client_id = "client_2"
        client2.config = Mock()
        client2.config.max_requests_per_second = 20

        RateLimiterManager.get_or_register_instance(client1)
        RateLimiterManager.get_or_register_instance(client2)

        assert "client_1" in RateLimiterManager._clients
        assert "client_2" in RateLimiterManager._clients
        assert RateLimiterManager._clients["client_1"] is not RateLimiterManager._clients["client_2"]
