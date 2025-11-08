"""Тесты MethodRateLimiterManager."""
import pytest

from src.ozonapi.seller.core.method_rate_limiter import MethodRateLimitConfig


class TestMethodRateLimiterManagerBasics:
    """Тесты базовой функциональности MethodRateLimiterManager."""

    @pytest.mark.asyncio
    async def test_get_limiter_creates_new_limiter(self, method_rate_limiter_manager, method_config):
        """Тест создания нового ограничителя метода."""
        client_id = "test_client"

        limiter = await method_rate_limiter_manager.get_limiter(client_id, method_config)

        assert limiter is not None
        stats = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 1

    @pytest.mark.asyncio
    async def test_get_limiter_reuses_existing_limiter(self, method_rate_limiter_manager, method_config):
        """Тест повторного использования существующего ограничителя."""
        client_id = "test_client"

        limiter1 = await method_rate_limiter_manager.get_limiter(client_id, method_config)
        limiter2 = await method_rate_limiter_manager.get_limiter(client_id, method_config)

        assert limiter1 is limiter2


class TestMethodRateLimiterManagerIsolation:
    """Тесты изоляции MethodRateLimiterManager."""

    @pytest.mark.asyncio
    async def test_different_clients_create_different_limiters(self, method_rate_limiter_manager, method_config):
        """Тест создания разных ограничителей для разных клиентов."""
        limiter1 = await method_rate_limiter_manager.get_limiter("client_1", method_config)
        limiter2 = await method_rate_limiter_manager.get_limiter("client_2", method_config)

        assert limiter1 is not limiter2

        stats = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 2

    @pytest.mark.asyncio
    async def test_different_methods_create_different_limiters(self, method_rate_limiter_manager):
        """Тест создания разных ограничителей для разных методов."""
        config1 = MethodRateLimitConfig(
            limit_requests=10,
            interval_seconds=1.0,
            method_identifier="method_1"
        )
        config2 = MethodRateLimitConfig(
            limit_requests=5,
            interval_seconds=2.0,
            method_identifier="method_2"
        )

        limiter1 = await method_rate_limiter_manager.get_limiter("test_client", config1)
        limiter2 = await method_rate_limiter_manager.get_limiter("test_client", config2)

        assert limiter1 is not limiter2

        stats = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 2