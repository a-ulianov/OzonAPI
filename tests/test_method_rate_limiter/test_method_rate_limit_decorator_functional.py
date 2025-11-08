"""Тесты функциональности декоратора method_rate_limit."""
import pytest
import time

from src.ozonapi.seller.core.method_rate_limiter import (
    method_rate_limit,
    MethodRateLimiterManager
)


class TestMethodRateLimitDecoratorFunctional:
    """Тесты функциональности декоратора method_rate_limit."""

    @pytest.mark.asyncio
    async def test_decorator_actual_limiting(self):
        """Тест реального ограничения частоты вызовов метода."""

        class TestClass:
            def __init__(self):
                self._client_id = "test_client"
                self._method_rate_limiter_manager = MethodRateLimiterManager(
                    cleanup_interval=300.0, min_instance_ttl=300.0
                )

            @method_rate_limit(limit_requests=2, interval_seconds=0.5)
            async def limited_method(self, value):
                return f"result_{value}"

        instance = TestClass()

        start_time = time.monotonic()

        # Первые два вызова должны пройти быстро
        for i in range(2):
            await instance.limited_method(i)

        time_two_calls = time.monotonic() - start_time

        # Третий вызов должен быть ограничен
        start_third = time.monotonic()
        await instance.limited_method(2)
        time_third_call = time.monotonic() - start_third

        assert time_two_calls < 0.1  # Первые два быстро
        assert time_third_call > 0.1  # Третий с задержкой

    @pytest.mark.asyncio
    async def test_method_identifier_generation(self):
        """Тест генерации идентификатора метода."""

        class TestClass:
            def __init__(self):
                self._client_id = "test_client"
                self._method_rate_limiter_manager = MethodRateLimiterManager(
                    cleanup_interval=300.0, min_instance_ttl=300.0
                )

            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def limited_method(self):
                return "result"

        instance = TestClass()

        # Проверяем, что у декорированного метода есть метаданные
        assert hasattr(instance.limited_method, '_rate_limit_config')
        config = instance.limited_method._rate_limit_config

        assert config.limit_requests == 5
        assert config.interval_seconds == 1.0
        assert "limited_method" in config.method_identifier
        assert "TestClass" in config.method_identifier