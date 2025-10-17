import asyncio
import time
from unittest.mock import patch
import pytest
from aiolimiter import AsyncLimiter

from src.ozonapi.seller.core.rate_limiter import RateLimiterManager, RateLimiterConfig


class TestRateLimiterManager:
    """Тесты для RateLimiterManager."""

    @pytest.fixture
    def rate_limiter_manager(self):
        """Фикстура для создания экземпляра RateLimiterManager."""
        return RateLimiterManager(cleanup_interval=0.1, min_instance_ttl=0.1)

    @pytest.fixture
    def rate_limiter_config(self):
        """Фикстура для создания конфигурации ограничителя."""
        return RateLimiterConfig(max_requests=50, time_window=1.0)

    @pytest.mark.asyncio
    async def test_get_limiter_creates_new_limiter(self, rate_limiter_manager, rate_limiter_config):
        """Тест создания нового ограничителя при первом обращении."""
        client_id = "test_client"

        limiter = await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        assert isinstance(limiter, AsyncLimiter)

        stats = await rate_limiter_manager.get_limiter_stats()
        assert client_id in stats
        assert stats[client_id]["config"] == rate_limiter_config

    @pytest.mark.asyncio
    async def test_limiter_usage_with_multiple_instances(self, rate_limiter_manager, rate_limiter_config):
        """Тест использования ограничителя с несколькими экземплярами."""
        client_id = "test_client"
        instance_ids = [123, 456, 789]

        # Регистрируем несколько экземпляров
        for instance_id in instance_ids:
            await rate_limiter_manager.register_instance(client_id, instance_id)

        # Получаем ограничитель
        limiter = await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        # Проверяем статистику экземпляров
        stats = await rate_limiter_manager.get_instance_stats()
        assert client_id in stats
        assert stats[client_id] == len(instance_ids)
        assert isinstance(limiter, AsyncLimiter)

        # Проверяем статистику ограничителей
        limiter_stats = await rate_limiter_manager.get_limiter_stats()
        assert client_id in limiter_stats
        assert limiter_stats[client_id]["instances"] == len(instance_ids)

    @pytest.mark.asyncio
    async def test_comprehensive_workflow(self, rate_limiter_manager):
        """Комплексный тест полного workflow."""
        client_id = "test_client"
        config = RateLimiterConfig(max_requests=5, time_window=1.0)
        instance_ids = [1, 2, 3]

        # Регистрируем экземпляры
        for instance_id in instance_ids:
            await rate_limiter_manager.register_instance(client_id, instance_id)

        # Получаем ограничитель
        limiter = await rate_limiter_manager.get_limiter(client_id, config)

        # Проверяем статистику экземпляров
        stats = await rate_limiter_manager.get_instance_stats()
        assert client_id in stats
        assert stats[client_id] == len(instance_ids)
        assert isinstance(limiter, AsyncLimiter)

        # Проверяем статистику ограничителей
        limiter_stats = await rate_limiter_manager.get_limiter_stats()
        assert client_id in limiter_stats
        assert limiter_stats[client_id]["instances"] == len(instance_ids)

        # Удаляем экземпляры
        for instance_id in instance_ids:
            await rate_limiter_manager.unregister_instance(client_id, instance_id)

        # Проверяем, что экземпляры удалены
        stats_after = await rate_limiter_manager.get_instance_stats()
        # client_id может отсутствовать в статистике после удаления всех экземпляров
        assert client_id not in stats_after or stats_after[client_id] == 0

        # Запускаем очистку
        await rate_limiter_manager.start()
        await asyncio.sleep(0.3)  # Ждем очистки
        await rate_limiter_manager.shutdown()

        # Проверяем очистку в статистике
        final_stats = await rate_limiter_manager.get_limiter_stats()
        assert client_id not in final_stats

    @pytest.mark.asyncio
    async def test_get_limiter_reuses_existing_limiter(self, rate_limiter_manager, rate_limiter_config):
        """Тест повторного использования существующего ограничителя."""
        client_id = "test_client"

        limiter1 = await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)
        limiter2 = await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        assert limiter1 is limiter2

    @pytest.mark.asyncio
    async def test_get_limiter_different_clients_create_different_limiters(self, rate_limiter_manager,
                                                                           rate_limiter_config):
        """Тест создания разных ограничителей для разных client_id."""
        client_id_1 = "client_1"
        client_id_2 = "client_2"

        limiter1 = await rate_limiter_manager.get_limiter(client_id_1, rate_limiter_config)
        limiter2 = await rate_limiter_manager.get_limiter(client_id_2, rate_limiter_config)

        assert limiter1 is not limiter2

    @pytest.mark.asyncio
    async def test_register_instance(self, rate_limiter_manager):
        """Тест регистрации экземпляра."""
        client_id = "test_client"
        instance_id = 123

        await rate_limiter_manager.register_instance(client_id, instance_id)

        # Проверяем через статистику
        stats = await rate_limiter_manager.get_instance_stats()
        assert client_id in stats
        assert stats[client_id] == 1

    @pytest.mark.asyncio
    async def test_unregister_instance(self, rate_limiter_manager):
        """Тест удаления регистрации экземпляра."""
        client_id = "test_client"
        instance_id = 123

        # Сначала регистрируем
        await rate_limiter_manager.register_instance(client_id, instance_id)
        stats_before = await rate_limiter_manager.get_instance_stats()
        assert stats_before[client_id] == 1

        # Затем удаляем
        await rate_limiter_manager.unregister_instance(client_id, instance_id)
        stats_after = await rate_limiter_manager.get_instance_stats()

        assert client_id not in stats_after or stats_after[client_id] == 0

    @pytest.mark.asyncio
    async def test_unregister_nonexistent_instance(self, rate_limiter_manager):
        """Тест удаления несуществующего экземпляра."""
        # Не должно быть исключения при удалении несуществующего экземпляра
        await rate_limiter_manager.unregister_instance("nonexistent_client", 123)

    @pytest.mark.asyncio
    async def test_cleanup_unused_limiters_with_active_instances(self, rate_limiter_manager, rate_limiter_config):
        """Тест очистки неиспользуемых ограничителей с активными экземплярами."""
        client_id = "test_client"
        instance_id = 123

        # Создаем ограничитель и регистрируем экземпляр
        await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)
        await rate_limiter_manager.register_instance(client_id, instance_id)

        # Очищаем неиспользуемые ограничители
        await rate_limiter_manager._cleanup_unused_limiters()

        # Ограничитель не должен быть очищен, т.к. есть активные экземпляры
        active_clients = await rate_limiter_manager.get_active_client_ids()
        assert client_id in active_clients

    @pytest.mark.asyncio
    async def test_cleanup_unused_limiters_with_no_instances(self, rate_limiter_manager, rate_limiter_config):
        """Тест очистки неиспользуемых ограничителей без активных экземпляров."""
        client_id = "test_client"

        # Создаем ограничитель без регистрации экземпляров
        await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        await asyncio.sleep(0.2)

        # Очищаем неиспользуемые ограничители
        await rate_limiter_manager._cleanup_unused_limiters()

        # Ограничитель должен быть очищен, т.к. нет активных экземпляров
        active_clients = await rate_limiter_manager.get_active_client_ids()
        assert client_id not in active_clients

    @pytest.mark.asyncio
    async def test_cleanup_loop_functionality(self, rate_limiter_manager, rate_limiter_config):
        """Тест работы фоновой задачи очистки."""
        client_id = "test_client"

        # Создаем ограничитель без регистрации экземпляров
        await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        # Запускаем менеджер
        await rate_limiter_manager.start()

        await asyncio.sleep(0.3)

        # Останавливаем менеджер
        await rate_limiter_manager.shutdown()

        # Ограничитель должен быть очищен
        active_clients = await rate_limiter_manager.get_active_client_ids()
        assert client_id not in active_clients

    @pytest.mark.asyncio
    async def test_start_and_shutdown(self, rate_limiter_manager):
        """Тест запуска и остановки менеджера."""
        # Запускаем менеджер
        await rate_limiter_manager.start()
        assert rate_limiter_manager._cleanup_task is not None
        assert not rate_limiter_manager._shutdown

        # Останавливаем менеджер
        await rate_limiter_manager.shutdown()
        assert rate_limiter_manager._cleanup_task is None
        assert rate_limiter_manager._shutdown

    @pytest.mark.asyncio
    async def test_multiple_start_calls(self, rate_limiter_manager):
        """Тест множественных вызовов start."""
        # Первый вызов
        await rate_limiter_manager.start()
        task1 = rate_limiter_manager._cleanup_task

        # Второй вызов
        await rate_limiter_manager.start()
        task2 = rate_limiter_manager._cleanup_task

        # Задача не должна меняться при повторных вызовах
        assert task1 is task2

        await rate_limiter_manager.shutdown()

    @pytest.mark.asyncio
    async def test_get_active_client_ids(self, rate_limiter_manager):
        """Тест получения списка активных client_id."""
        client_id_1 = "client_1"
        client_id_2 = "client_2"

        # Регистрируем экземпляры
        await rate_limiter_manager.register_instance(client_id_1, 123)
        await rate_limiter_manager.register_instance(client_id_2, 456)

        active_clients = await rate_limiter_manager.get_active_client_ids()

        assert client_id_1 in active_clients
        assert client_id_2 in active_clients
        assert len(active_clients) == 2

    @pytest.mark.asyncio
    async def test_get_active_client_ids_empty(self, rate_limiter_manager):
        """Тест получения пустого списка активных client_id."""
        active_clients = await rate_limiter_manager.get_active_client_ids()

        assert isinstance(active_clients, list)
        assert len(active_clients) == 0

    @pytest.mark.asyncio
    async def test_get_instance_stats(self, rate_limiter_manager):
        """Тест получения статистики по экземплярам."""
        client_id_1 = "client_1"
        client_id_2 = "client_2"

        # Регистрируем экземпляры
        await rate_limiter_manager.register_instance(client_id_1, 123)
        await rate_limiter_manager.register_instance(client_id_1, 456)
        await rate_limiter_manager.register_instance(client_id_2, 789)

        stats = await rate_limiter_manager.get_instance_stats()

        assert client_id_1 in stats
        assert client_id_2 in stats
        assert stats[client_id_1] == 2
        assert stats[client_id_2] == 1

    @pytest.mark.asyncio
    async def test_get_limiter_stats(self, rate_limiter_manager, rate_limiter_config):
        """Тест получения детальной статистики по ограничителям."""
        client_id = "test_client"

        # Создаем ограничитель и регистрируем экземпляр
        await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)
        await rate_limiter_manager.register_instance(client_id, 123)

        stats = await rate_limiter_manager.get_limiter_stats()

        assert client_id in stats
        assert "config" in stats[client_id]
        assert "instances" in stats[client_id]
        assert "limiter" in stats[client_id]
        assert "last_instance_creation" in stats[client_id]
        assert "time_since_creation" in stats[client_id]

        assert stats[client_id]["config"] == rate_limiter_config
        assert stats[client_id]["instances"] == 1
        assert isinstance(stats[client_id]["limiter"], str)

    @pytest.mark.asyncio
    async def test_concurrent_access_to_same_limiter(self, rate_limiter_manager, rate_limiter_config):
        """Тест конкурентного доступа к одному ограничителю."""
        client_id = "test_client"

        async def get_limiter_task(task_id):
            return await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        # Запускаем несколько задач одновременно
        tasks = [get_limiter_task(i) for i in range(10)]
        results = await asyncio.gather(*tasks)

        # Все задачи должны получить один и тот же ограничитель
        first_limiter = results[0]
        assert all(limiter is first_limiter for limiter in results)

    @pytest.mark.asyncio
    async def test_limiter_actual_rate_limiting(self, rate_limiter_manager):
        """Тест реального ограничения запросов."""
        config = RateLimiterConfig(max_requests=2, time_window=0.5)
        client_id = "test_client"

        limiter = await rate_limiter_manager.get_limiter(client_id, config)

        # Первые два запроса должны пройти быстро
        start_time = time.monotonic()

        async with limiter:
            pass
        async with limiter:
            pass

        first_two_time = time.monotonic() - start_time
        assert first_two_time < 0.1  # Должны выполниться быстро

        # Третий запрос должен быть ограничен (но время может варьироваться)
        start_time = time.monotonic()
        async with limiter:
            pass
        third_request_time = time.monotonic() - start_time

        # Время ожидания должно быть значительным (но не обязательно точно 0.4)
        assert third_request_time > 0.1  # Должен ждать некоторое время

    @pytest.mark.asyncio
    async def test_different_configs_same_client(self, rate_limiter_manager):
        """Тест использования разных конфигураций для одного client_id."""
        client_id = "test_client"
        config1 = RateLimiterConfig(max_requests=10, time_window=1.0)
        config2 = RateLimiterConfig(max_requests=20, time_window=2.0)

        # Первый вызов создает ограничитель
        limiter1 = await rate_limiter_manager.get_limiter(client_id, config1)

        # Второй вызов с другой конфигурацией должен вернуть тот же ограничитель
        limiter2 = await rate_limiter_manager.get_limiter(client_id, config2)

        assert limiter1 is limiter2
        # Конфигурация должна остаться от первого вызова
        stats = await rate_limiter_manager.get_limiter_stats()
        assert stats[client_id]["config"] == config1

    @pytest.mark.asyncio
    async def test_cleanup_preserves_recent_instances(self, rate_limiter_manager, rate_limiter_config):
        """Тест, что очистка сохраняет недавно созданные экземпляры."""
        client_id = "test_client"

        # Создаем ограничитель без экземпляров
        await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)

        # Очищаем сразу - не должен очиститься из-за min_instance_ttl
        await rate_limiter_manager._cleanup_unused_limiters()

        # Должен остаться, т.к. время создания меньше min_instance_ttl
        stats = await rate_limiter_manager.get_limiter_stats()
        assert client_id in stats

    @pytest.mark.asyncio
    async def test_shutdown_without_start(self, rate_limiter_manager):
        """Тест остановки без предварительного запуска."""
        # Не должно быть исключения
        await rate_limiter_manager.shutdown()

    @pytest.mark.asyncio
    async def test_cleanup_loop_handles_exceptions(self, rate_limiter_manager):
        """Тест обработки исключений в цикле очистки."""
        # Мокаем метод очистки чтобы вызвать исключение
        with patch.object(rate_limiter_manager, '_cleanup_unused_limiters', side_effect=Exception("Test error")):
            await rate_limiter_manager.start()

            await asyncio.sleep(0.2)

            # Не должно быть исключения, цикл должен продолжать работать
            assert rate_limiter_manager._cleanup_task is not None

            await rate_limiter_manager.shutdown()

    def test_rate_limiter_config_repr(self, rate_limiter_config):
        """Тест строкового представления конфигурации."""
        repr_str = repr(rate_limiter_config)

        assert "RateLimiterConfig" in repr_str
        assert "max_requests=50" in repr_str
        assert "time_window=1.0" in repr_str

    def test_rate_limiter_config_initialization(self):
        """Тест инициализации конфигурации с различными параметрами."""
        config = RateLimiterConfig(max_requests=100, time_window=2.0)

        assert config.max_requests == 100
        assert config.time_window == 2.0

    @pytest.mark.asyncio
    async def test_limiter_configuration_correctness(self, rate_limiter_manager):
        """Тест корректности конфигурации ограничителя."""
        max_requests = 25
        time_window = 2.0
        config = RateLimiterConfig(max_requests=max_requests, time_window=time_window)
        client_id = "test_client"

        limiter = await rate_limiter_manager.get_limiter(client_id, config)

        assert limiter.max_rate == max_requests
        assert limiter.time_period == time_window

    @pytest.mark.asyncio
    async def test_race_condition_prevention(self, rate_limiter_manager, rate_limiter_config):
        """Тест предотвращения гонок условий при создании ограничителей."""
        client_id = "test_client"
        results = []

        async def create_limiter(task_id):
            limiter = await rate_limiter_manager.get_limiter(client_id, rate_limiter_config)
            results.append(limiter)
            await asyncio.sleep(0.01)

        # Запускаем несколько задач одновременно
        tasks = [create_limiter(i) for i in range(5)]
        await asyncio.gather(*tasks)

        # Все задачи должны получить один и тот же объект ограничителя
        first_limiter = results[0]
        assert all(limiter is first_limiter for limiter in results)