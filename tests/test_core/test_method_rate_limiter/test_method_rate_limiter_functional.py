"""Тесты функциональности MethodRateLimiter."""
import pytest
import asyncio
import time

from src.ozonapi.seller.core.method_rate_limiter import MethodRateLimitConfig


class TestMethodRateLimiterFunctional:
    """Тесты функциональности MethodRateLimiter."""

    @pytest.mark.asyncio
    async def test_limiter_actual_rate_limiting(self, method_rate_limiter_manager):
        """Тест реального ограничения частоты запросов."""
        config = MethodRateLimitConfig(
            limit_requests=2,
            interval_seconds=0.5,
            method_identifier="test_method"
        )

        limiter = await method_rate_limiter_manager.get_limiter("test_client", config)

        # Первые два запроса должны пройти быстро
        start_time = time.monotonic()
        async with limiter:
            pass
        async with limiter:
            pass
        time_two_requests = time.monotonic() - start_time

        # Третий запрос должен быть ограничен
        start_time = time.monotonic()
        async with limiter:
            pass
        time_third_request = time.monotonic() - start_time

        assert time_two_requests < 0.1  # Первые два быстро
        assert time_third_request > 0.1  # Третий с задержкой


class TestMethodRateLimiterConcurrency:
    """Тесты конкурентности MethodRateLimiter."""

    @pytest.mark.asyncio
    async def test_concurrent_access_to_same_limiter(self, method_rate_limiter_manager, method_config):
        """Тест конкурентного доступа к одному ограничителю."""
        client_id = "test_client"

        # Создаем несколько задач, обращающихся к одному ограничителю
        async def use_limiter():
            limiter = await method_rate_limiter_manager.get_limiter(client_id, method_config)
            async with limiter:
                await asyncio.sleep(0.01)

        tasks = [use_limiter() for _ in range(5)]
        await asyncio.gather(*tasks)

        # Проверяем, что создан только один ограничитель
        stats = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 1