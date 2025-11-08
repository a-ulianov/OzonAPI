"""Тесты жизненного цикла MethodRateLimiter."""
import pytest

from src.ozonapi.seller.core.method_rate_limiter import MethodRateLimitConfig


class TestMethodRateLimiterLifecycle:
    """Тесты жизненного цикла MethodRateLimiter."""

    @pytest.mark.asyncio
    async def test_start_and_shutdown(self, method_rate_limiter_manager):
        """Тест запуска и остановки менеджера."""
        await method_rate_limiter_manager.start()
        await method_rate_limiter_manager.shutdown()

        # Проверяем, что менеджер корректно остановился
        assert method_rate_limiter_manager._cleanup_task is None
        assert method_rate_limiter_manager._shutdown is True

    @pytest.mark.asyncio
    async def test_get_limiter_stats(self, method_rate_limiter_manager):
        """Тест получения статистики ограничителей."""
        config = MethodRateLimitConfig(
            limit_requests=5,
            interval_seconds=1.0,
            method_identifier="test_method"
        )

        await method_rate_limiter_manager.get_limiter("test_client", config)

        stats = await method_rate_limiter_manager.get_limiter_stats()

        assert len(stats) == 1
        limiter_key = list(stats.keys())[0]
        stat = stats[limiter_key]

        assert stat["config"] == config
        assert "last_used" in stat
        assert "last_instance_creation" in stat
        assert "time_since_creation" in stat
        assert "time_since_usage" in stat