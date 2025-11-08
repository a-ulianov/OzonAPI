"""Тесты декоратора method_rate_limit."""
import pytest
from unittest.mock import patch

from src.ozonapi.seller.core.method_rate_limiter import (
    method_rate_limit,
    MethodRateLimiterManager
)


class TestMethodRateLimitDecoratorBasics:
    """Тесты базовой функциональности декоратора method_rate_limit."""

    @pytest.mark.asyncio
    async def test_decorator_applies_to_method(self, mock_class_with_manager):
        """Тест применения декоратора к методу."""

        class TestClass:
            def __init__(self):
                self._client_id = "test_client"
                self._method_rate_limiter_manager = MethodRateLimiterManager(
                    cleanup_interval=300.0, min_instance_ttl=300.0
                )

            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def limited_method(self, arg1, arg2=None):
                return f"result_{arg1}_{arg2}"

        instance = TestClass()
        result = await instance.limited_method("test", arg2="value")

        assert result == "result_test_value"

    @pytest.mark.asyncio
    async def test_decorator_creates_limiter(self, mock_class_with_manager):
        """Тест создания ограничителя декоратором."""

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
        await instance.limited_method()

        # Проверяем, что ограничитель создан
        stats = await instance._method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 1


class TestMethodRateLimitDecoratorAdvanced:
    """Тесты расширенной функциональности декоратора method_rate_limit."""

    @pytest.mark.asyncio
    async def test_multiple_methods_create_multiple_limiters(self, mock_class_with_manager):
        """Тест создания нескольких ограничителей для разных методов."""

        class TestClass:
            def __init__(self):
                self._client_id = "test_client"
                self._method_rate_limiter_manager = MethodRateLimiterManager(
                    cleanup_interval=300.0, min_instance_ttl=300.0
                )

            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def method1(self):
                return "result1"

            @method_rate_limit(limit_requests=10, interval_seconds=2.0)
            async def method2(self):
                return "result2"

        instance = TestClass()
        await instance.method1()
        await instance.method2()

        # Проверяем, что создано два ограничителя
        stats = await instance._method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 2

    @pytest.mark.asyncio
    async def test_decorator_without_required_attributes(self):
        """Тест вызова декорированного метода без необходимых атрибутов."""

        class InvalidClass:
            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def limited_method(self):
                return "result"

        instance = InvalidClass()

        # Должен сработать warning, а метод выполниться без ограничений
        with patch('src.ozonapi.infrastructure.logging.ozonapi_logger.warning') as mock_warning:
            result = await instance.limited_method()

            assert result == "result"
            mock_warning.assert_called_once()