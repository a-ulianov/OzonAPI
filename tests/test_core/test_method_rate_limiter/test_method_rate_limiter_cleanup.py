"""Тесты очистки MethodRateLimiter."""
import pytest
import asyncio


class TestMethodRateLimiterCleanup:
    """Тесты очистки MethodRateLimiter."""

    @pytest.mark.asyncio
    async def test_cleanup_unused_limiters(self, method_rate_limiter_manager, method_config):
        """Тест очистки неиспользуемых ограничителей."""
        # Создаем ограничитель
        await method_rate_limiter_manager.get_limiter("test_client", method_config)

        # Проверяем, что ограничитель создан
        stats_before = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats_before) == 1

        # Ждем очистку
        await asyncio.sleep(0.2)
        await method_rate_limiter_manager._cleanup_unused_limiters()

        # Проверяем, что ограничитель удален
        stats_after = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats_after) == 0

    @pytest.mark.asyncio
    async def test_cleanup_loop_functionality(self, method_rate_limiter_manager, method_config):
        """Тест работы фоновой задачи очистки."""
        await method_rate_limiter_manager.start()

        # Создаем ограничитель
        await method_rate_limiter_manager.get_limiter("test_client", method_config)

        # Ждем, пока cleanup loop сработает
        await asyncio.sleep(0.3)

        # Проверяем, что ограничитель очищен
        stats = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 0

        await method_rate_limiter_manager.shutdown()