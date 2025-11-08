"""Фикстуры для тестирования MethodRateLimiter."""
import pytest
import asyncio

from src.ozonapi.seller.core.method_rate_limiter import (
    MethodRateLimiterManager,
    MethodRateLimitConfig
)


@pytest.fixture
def method_rate_limiter_manager():
    """Создает менеджер ограничителей методов."""
    manager = MethodRateLimiterManager(cleanup_interval=0.1, min_instance_ttl=0.1)
    yield manager

    try:
        asyncio.run(manager.shutdown())
    except RuntimeError:
        pass


@pytest.fixture
def method_config():
    """Создает конфигурацию метода."""
    return MethodRateLimitConfig(
        limit_requests=10,
        interval_seconds=1.0,
        method_identifier="test_method"
    )


@pytest.fixture
def mock_class_with_manager(method_rate_limiter_manager):
    """Создает mock класс с менеджером ограничителей."""

    class MockClass:
        def __init__(self):
            self._client_id = "test_client"
            self._method_rate_limiter_manager = method_rate_limiter_manager

    return MockClass()