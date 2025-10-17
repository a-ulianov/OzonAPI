import asyncio
import time
import pytest
from unittest.mock import patch

from src.ozonapi.seller.core.method_rate_limiter import (
    MethodRateLimiterManager,
    MethodRateLimitConfig,
    method_rate_limit
)


class TestMethodRateLimiterManager:
    """Тесты для MethodRateLimiterManager."""

    @pytest.fixture
    def method_rate_limiter_manager(self):
        """Фикстура для создания менеджера ограничителей методов."""
        manager = MethodRateLimiterManager(cleanup_interval=0.1, min_instance_ttl=0.1)
        yield manager

        try:
            asyncio.run(manager.shutdown())
        except RuntimeError:
            pass

    @pytest.fixture
    def method_config(self):
        """Фикстура для конфигурации метода."""
        return MethodRateLimitConfig(
            limit_requests=10,
            interval_seconds=1.0,
            method_identifier="test_method"
        )

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

    @pytest.mark.asyncio
    async def test_get_limiter_different_clients_create_different_limiters(self, method_rate_limiter_manager,
                                                                           method_config):
        """Тест создания разных ограничителей для разных клиентов."""
        limiter1 = await method_rate_limiter_manager.get_limiter("client_1", method_config)
        limiter2 = await method_rate_limiter_manager.get_limiter("client_2", method_config)

        assert limiter1 is not limiter2

        stats = await method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 2

    @pytest.mark.asyncio
    async def test_get_limiter_different_methods_create_different_limiters(self, method_rate_limiter_manager):
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

        # Проверяем, что у третьего запроса задержка существенная
        assert time_third_request > 0.1
        assert time_third_request < 0.7  # Но не слишком большая

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


class TestMethodRateLimitDecorator:
    """Тесты для декоратора method_rate_limit."""

    @pytest.fixture
    def mock_class(self):
        """Фикстура для создания mock класса с необходимыми атрибутами."""

        class MockClass:
            def __init__(self):
                self._client_id = "test_client"
                self._method_rate_limiter_manager = MethodRateLimiterManager(
                    cleanup_interval=300.0, min_instance_ttl=300.0
                )

            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def limited_method(self, arg1, arg2=None):
                return f"result_{arg1}_{arg2}"

            @method_rate_limit(limit_requests=10, interval_seconds=2.0)
            async def another_limited_method(self):
                return "another_result"

        return MockClass()

    @pytest.mark.asyncio
    async def test_method_rate_limit_decorator(self, mock_class):
        """Тест применения декоратора к методу."""
        result = await mock_class.limited_method("test", arg2="value")

        assert result == "result_test_value"

        # Проверяем, что ограничитель создан
        stats = await mock_class._method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 1

    @pytest.mark.asyncio
    async def test_method_rate_limit_multiple_methods(self, mock_class):
        """Тест применения декоратора к нескольким методам."""
        await mock_class.limited_method("test1")
        await mock_class.another_limited_method()

        # Проверяем, что создано два ограничителя
        stats = await mock_class._method_rate_limiter_manager.get_limiter_stats()
        assert len(stats) == 2

    @pytest.mark.asyncio
    async def test_method_rate_limit_without_required_attributes(self):
        """Тест вызова декорированного метода без необходимых атрибутов."""

        class InvalidClass:
            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def limited_method(self):
                return "result"

        instance = InvalidClass()

        # Должен сработать warning, а метод выполниться без ограничений
        with patch('loguru.logger.warning') as mock_warning:
            result = await instance.limited_method()

            assert result == "result"
            mock_warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_method_rate_limit_with_none_manager(self):
        """Тест вызова декорированного метода с None менеджером."""

        class InvalidClass:
            def __init__(self):
                self._client_id = "test_client"
                self._method_rate_limiter_manager = None

            @method_rate_limit(limit_requests=5, interval_seconds=1.0)
            async def limited_method(self):
                return "result"

        instance = InvalidClass()

        # Должен сработать warning, а метод выполниться без ограничений
        with patch('loguru.logger.warning') as mock_warning:
            result = await instance.limited_method()

            assert result == "result"
            mock_warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_method_rate_limit_actual_limiting(self, mock_class):
        """Тест реального ограничения частоты вызовов метода."""
        start_time = time.monotonic()

        # Первые 5 вызовов должны пройти быстро
        for i in range(5):
            await mock_class.limited_method(i)

        time_five_calls = time.monotonic() - start_time

        # Шестой вызов должен быть ограничен
        start_sixth = time.monotonic()
        await mock_class.limited_method(6)
        time_sixth_call = time.monotonic() - start_sixth

        assert time_five_calls < 0.1  # Первые 5 быстро
        assert 0.1 < time_sixth_call <= 0.8  # Последний с задержкой

    @pytest.mark.asyncio
    async def test_method_identifier_generation(self, mock_class):
        """Тест генерации идентификатора метода."""
        # Проверяем, что у декорированного метода есть метаданные
        assert hasattr(mock_class.limited_method, '_rate_limit_config')
        config = mock_class.limited_method._rate_limit_config

        assert config.limit_requests == 5
        assert config.interval_seconds == 1.0
        assert "limited_method" in config.method_identifier
        assert "MockClass" in config.method_identifier


class TestMethodRateLimitConfig:
    """Тесты для MethodRateLimitConfig."""

    def test_method_rate_limit_config_initialization(self):
        """Тест инициализации конфигурации ограничителя метода."""
        config = MethodRateLimitConfig(
            limit_requests=15,
            interval_seconds=3.0,
            method_identifier="api.test_method"
        )

        assert config.limit_requests == 15
        assert config.interval_seconds == 3.0
        assert config.method_identifier == "api.test_method"

    def test_method_rate_limit_config_validation(self):
        """Тест валидации конфигурации ограничителя метода."""
        # Должен пройти без ошибок
        MethodRateLimitConfig(
            limit_requests=1,  # Минимальное значение
            interval_seconds=0.1,  # Больше 0
            method_identifier="test"
        )

        # Должны вызываться ошибки валидации
        with pytest.raises(ValueError):
            MethodRateLimitConfig(
                limit_requests=0,  # Меньше 1
                interval_seconds=1.0,
                method_identifier="test"
            )

        with pytest.raises(ValueError):
            MethodRateLimitConfig(
                limit_requests=5,
                interval_seconds=0,  # Меньше или равно 0
                method_identifier="test"
            )


@pytest.mark.asyncio
async def test_comprehensive_workflow():
    """Комплексный тест полного workflow ограничителей методов."""
    manager = MethodRateLimiterManager(cleanup_interval=0.1, min_instance_ttl=0.1)

    class TestAPI:
        def __init__(self):
            self._client_id = "test_client"
            self._method_rate_limiter_manager = manager

        @method_rate_limit(limit_requests=3, interval_seconds=1.0)
        async def get_products(self):
            await asyncio.sleep(0.01)
            return "products"

        @method_rate_limit(limit_requests=2, interval_seconds=0.5)
        async def get_orders(self):
            await asyncio.sleep(0.01)
            return "orders"

    api = TestAPI()

    # Используем методы
    results = []
    for _ in range(2):
        results.append(await api.get_products())
        results.append(await api.get_orders())

    assert all(r in results for r in ["products", "orders"])

    # Проверяем статистику
    stats = await manager.get_limiter_stats()
    assert len(stats) == 2

    # Ждем очистку и проверяем
    await asyncio.sleep(0.3)
    await manager._cleanup_unused_limiters()

    stats_after_cleanup = await manager.get_limiter_stats()
    assert len(stats_after_cleanup) == 0

    await manager.shutdown()