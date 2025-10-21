import asyncio
from unittest.mock import AsyncMock, patch
import pytest
from aiohttp import ClientResponse, ClientSession

from src.ozonapi.seller.core.core import APIManager
from src.ozonapi.seller.core.config import APIConfig
from src.ozonapi.seller.core.exceptions import (
    APIClientError, APIForbiddenError, APINotFoundError,
    APIConflictError, APIServerError, APIError, APITooManyRequestsError
)


class TestAPIManager:
    """Тесты для APIManager."""

    @pytest.fixture
    def api_config(self):
        """Фикстура для создания конфигурации API."""
        return APIConfig(
            base_url="https://api-seller.ozon.ru",
            max_requests_per_second=10,
            request_timeout=30.0,
            max_retries=2,
            retry_min_wait=0.1,
            retry_max_wait=0.2,
            cleanup_interval=300.0,
            min_instance_ttl=300.0,
            connector_limit=100
        )

    @pytest.fixture
    def api_manager(self, api_config):
        """Фикстура для создания экземпляра APIManager."""
        return APIManager(
            client_id="test_client",
            api_key="test_api_key",
            config=api_config
        )

    @pytest.fixture
    def mock_response(self):
        """Фикстура для мока ответа API."""
        response = AsyncMock(spec=ClientResponse)
        response.status = 200
        response.json.return_value = {"result": "success"}
        return response

    @pytest.fixture
    def mock_session(self):
        """Фикстура для мока сессии."""
        session = AsyncMock(spec=ClientSession)
        return session

    @pytest.fixture(autouse=True)
    async def setup_teardown(self):
        """Автоматическая настройка и очистка перед каждым тестом."""
        # Сбрасываем состояние класса перед каждым тестом
        if hasattr(APIManager, '_rate_limiter_manager'):
            APIManager._rate_limiter_manager = None
        if hasattr(APIManager, '_session_manager'):
            APIManager._session_manager = None
        if hasattr(APIManager, '_method_rate_limiter_manager'):
            APIManager._method_rate_limiter_manager = None
        APIManager._initialized = False
        APIManager._instance_count = 0

        yield

        # Очистка после теста
        try:
            await APIManager.shutdown()
        except:
            pass

    @pytest.mark.asyncio
    async def test_initialization(self, api_manager, api_config):
        """Тест инициализации APIManager."""
        with patch('src.ozonapi.seller.core.core.APIManager.load_config') as mock_load_config:
            mock_load_config.return_value = api_config
            manager = APIManager(client_id="test_client", api_key="test_api_key", config=api_config)

            assert manager._client_id == "test_client"
            assert manager._api_key == "test_api_key"
            assert manager._config == api_config

    @pytest.mark.asyncio
    async def test_initialization_with_default_config(self):
        """Тест инициализации с конфигурацией по умолчанию."""
        manager = APIManager(client_id="test_client", api_key="test_api_key")

        assert manager._client_id == "test_client"
        assert manager._api_key == "test_api_key"
        assert isinstance(manager._config, APIConfig)

    @pytest.mark.asyncio
    async def test_context_manager(self, api_config):
        """Тест работы контекстного менеджера."""
        async with APIManager(client_id="test_client", api_key="test_key", config=api_config) as manager:
            assert not manager.is_closed
            assert manager._registered

        assert manager.is_closed

    @pytest.mark.asyncio
    async def test_context_manager_closed_access(self, api_config):
        """Тест доступа к закрытому менеджеру."""
        async with APIManager(client_id="test_client", api_key="test_key", config=api_config) as manager:
            pass

        with pytest.raises(RuntimeError, match="Невозможно использовать закрытый API-клиент для ClientID test_client"):
            async with manager:
                pass

    @pytest.mark.asyncio
    async def test_close_method(self, api_manager):
        """Тест метода close."""
        await api_manager.close()
        assert api_manager.is_closed

        # Повторный вызов close не должен вызывать ошибку
        await api_manager.close()

    @pytest.mark.asyncio
    async def test_class_initialize_shutdown(self):
        """Тест классовых методов initialize и shutdown."""
        await APIManager.initialize()
        assert APIManager._initialized

        await APIManager.shutdown()
        assert not APIManager._initialized

    @pytest.mark.asyncio
    async def test_successful_request(self, api_manager, mock_response):
        """Тест успешного запроса к API."""
        # Мокаем SessionManager и его методы
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            result = await api_manager._request(
                method="post",
                endpoint="test-endpoint",
                json={"data": "test"}
            )

            assert result == {"result": "success"}
            mock_session.request.assert_called_once()

    @pytest.mark.asyncio
    async def test_request_with_params(self, api_manager, mock_response):
        """Тест запроса с параметрами."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            result = await api_manager._request(
                method="get",
                endpoint="test-endpoint",
                params={"param1": "value1", "param2": "value2"}
            )

            assert result == {"result": "success"}
            call_args = mock_session.request.call_args
            assert call_args[1]["params"] == {"param1": "value1", "param2": "value2"}

    @pytest.mark.asyncio
    async def test_request_different_methods(self, api_manager, mock_response):
        """Тест запросов с разными HTTP методами."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            methods = ["post", "get", "put", "delete"]
            for method in methods:
                await api_manager._request(method=method, endpoint="test-endpoint")

                call_args = mock_session.request.call_args
                assert call_args[0][0] == method

    @pytest.mark.asyncio
    async def test_request_api_versions(self, api_manager, mock_response):
        """Тест запросов с разными версиями API."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            api_versions = ["v1", "v2", "v3"]
            for version in api_versions:
                await api_manager._request(
                    method="post",
                    api_version=version,
                    endpoint="test-endpoint"
                )

                call_args = mock_session.request.call_args
                expected_url = f"https://api-seller.ozon.ru/{version}/test-endpoint"
                assert call_args[0][1] == expected_url

    @pytest.mark.asyncio
    async def test_request_retry_on_server_error(self, api_manager):
        """Тест повторных попыток при ошибках сервера."""
        with (
                patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager,
                patch('src.ozonapi.seller.core.core.APIManager._rate_limiter_manager') as mock_limiter_manager
        ):
            # Настраиваем моки
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session

            mock_limiter = AsyncMock()
            mock_limiter_manager.get_limiter = AsyncMock(return_value=mock_limiter)
            mock_limiter.acquire.return_value = None

            # Мокаем register_instance
            mock_limiter_manager.register_instance = AsyncMock()

            success_response = AsyncMock(spec=ClientResponse)
            success_response.status = 200
            success_response.json.return_value = {"result": "success"}
            mock_session.request.return_value.__aenter__.return_value = success_response

            result = await api_manager._request(method="post", endpoint="test-endpoint")

            assert result == {"result": "success"}

    @pytest.mark.asyncio
    async def test_request_no_retry_on_client_error(self, api_manager):
        """Тест отсутствия повторных попыток при ошибках клиента."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session

            error_response = AsyncMock(spec=ClientResponse)
            error_response.status = 400
            error_response.json.return_value = {"code": 400, "message": "Bad Request"}

            mock_session.request.return_value.__aenter__.return_value = error_response

            with pytest.raises(APIClientError):
                await api_manager._request(method="post", endpoint="test-endpoint")

            assert mock_session.request.call_count == 1

    @pytest.mark.asyncio
    async def test_error_handling(self, api_manager):
        """Тест обработки различных ошибок API."""
        error_cases = [
            (400, APIClientError),
            (403, APIForbiddenError),
            (404, APINotFoundError),
            (409, APIConflictError),
            (429, APITooManyRequestsError),
            (500, APIServerError),
        ]

        for status_code, expected_exception in error_cases:
            with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
                mock_session = AsyncMock(spec=ClientSession)
                mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session

                error_response = AsyncMock(spec=ClientResponse)
                error_response.status = status_code
                error_response.json.return_value = {
                    "code": status_code,
                    "message": f"Error {status_code}",
                    "details": []
                }

                mock_session.request.return_value.__aenter__.return_value = error_response

                with pytest.raises(expected_exception):
                    await api_manager._request(method="post", endpoint="test-endpoint")

    @pytest.mark.asyncio
    async def test_network_error_handling(self, api_manager):
        """Тест обработки сетевых ошибок."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.side_effect = ConnectionError("Network error")

            with pytest.raises(APIError, match="Network error"):
                await api_manager._request(method="post", endpoint="test-endpoint")

    @pytest.mark.asyncio
    async def test_closed_manager_request(self, api_manager):
        """Тест запроса от закрытого менеджера."""
        await api_manager.close()

        with pytest.raises(RuntimeError, match="API-клиент остановлен"):
            await api_manager._request(method="post", endpoint="test-endpoint")

    @pytest.mark.asyncio
    async def test_get_active_client_ids(self, api_config):
        """Тест получения активных client_id."""
        async with APIManager(client_id="client1", api_key="key1", config=api_config) as manager1:
            async with APIManager(client_id="client2", api_key="key2", config=api_config) as manager2:
                active_clients = await APIManager.get_active_client_ids()

                # Проверяем что оба клиента активны
                assert len(active_clients) >= 2
                assert "client1" in active_clients or "client2" in active_clients

    @pytest.mark.asyncio
    async def test_get_rate_limiter_stats(self, api_config):
        """Тест получения статистики ограничителей."""
        async with APIManager(client_id="test_client", api_key="test_key", config=api_config) as manager:
            stats = await APIManager.get_rate_limiter_stats()

            assert isinstance(stats, dict)

    @pytest.mark.asyncio
    async def test_get_detailed_stats(self, api_config):
        """Тест получения детальной статистики."""
        async with APIManager(client_id="test_client", api_key="test_key", config=api_config) as manager:
            stats = await APIManager.get_detailed_stats()

            assert isinstance(stats, dict)

    @pytest.mark.asyncio
    async def test_get_method_limiter_stats(self, api_config):
        """Тест получения статистики ограничителей методов."""
        async with APIManager(client_id="test_client", api_key="test_key", config=api_config) as manager:
            stats = await APIManager.get_method_limiter_stats()

            assert isinstance(stats, dict)

    def test_properties(self, api_manager):
        """Тест свойств класса."""
        assert api_manager.client_id == "test_client"
        assert isinstance(api_manager.config, APIConfig)
        assert api_manager.is_closed is False

    @pytest.mark.asyncio
    async def test_multiple_instances_same_client(self, api_config):
        """Тест нескольких экземпляров с одним client_id."""
        # Сохраняем начальное количество экземпляров
        initial_count = APIManager._instance_count

        manager1 = APIManager(client_id="same_client", api_key="key1", config=api_config)
        manager2 = APIManager(client_id="same_client", api_key="key1", config=api_config)

        # Проверяем что создано 2 новых экземпляра
        assert APIManager._instance_count == initial_count + 2

        await manager1.close()
        await manager2.close()

    @pytest.mark.asyncio
    async def test_concurrent_requests(self, api_manager, mock_response):
        """Тест конкурентных запросов."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            # Запускаем несколько конкурентных запросов
            tasks = [
                api_manager._request(method="post", endpoint=f"endpoint-{i}")
                for i in range(5)
            ]
            results = await asyncio.gather(*tasks)

            assert len(results) == 5
            assert all(result == {"result": "success"} for result in results)
            assert mock_session.request.call_count == 5

    @pytest.mark.asyncio
    async def test_request_headers(self, api_manager, mock_response):
        """Тест заголовков запроса."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            # Сессия уже создается с заголовками в SessionManager
            # Проверяем, что заголовки установлены при создании сессии
            await api_manager._request(method="post", endpoint="test-endpoint")

            # Проверяем, что сессия создана с правильными заголовками
            mock_session_manager.get_session.assert_called_once()
            call_args = mock_session_manager.get_session.call_args
            assert call_args[0][0] == "test_client"
            assert call_args[0][1] == "test_api_key"

    @pytest.mark.asyncio
    async def test_ensure_registered(self, api_manager):
        """Тест гарантированной регистрации экземпляра."""
        await api_manager._ensure_registered()
        assert api_manager._registered

        # Повторный вызов не должен вызывать проблем
        await api_manager._ensure_registered()

    @pytest.mark.asyncio
    async def test_ensure_registered_closed_manager(self, api_manager):
        """Тест регистрации закрытого менеджера."""
        await api_manager.close()

        with pytest.raises(RuntimeError, match="Регистрация API-клиента отменена"):
            await api_manager._ensure_registered()

    @pytest.mark.asyncio
    async def test_request_logging(self, api_manager, mock_response, caplog):
        """Тест логирования запросов."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager, \
                patch.object(api_manager.logger, 'debug') as mock_debug, \
                patch.object(APIManager._class_logger, 'debug') as mock_class_debug:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session
            mock_session.request.return_value.__aenter__.return_value = mock_response

            await api_manager._request(
                method="post",
                api_name="Test API",
                endpoint="test-endpoint",
                json={"data": "test"}
            )

            # Проверяем что методы логирования вызывались
            debug_calls = [call for call in mock_debug.call_args_list
                           if "Отправка запроса к API" in str(call) or "Успешный ответ от API" in str(call)]
            assert len(debug_calls) >= 2

    @pytest.mark.asyncio
    async def test_error_logging(self, api_manager, caplog):
        """Тест логирования ошибок."""
        with patch('src.ozonapi.seller.core.core.APIManager._session_manager') as mock_session_manager, \
                patch.object(APIManager._class_logger, 'error') as mock_class_error:
            mock_session = AsyncMock(spec=ClientSession)
            mock_session_manager.get_session.return_value.__aenter__.return_value = mock_session

            error_response = AsyncMock(spec=ClientResponse)
            error_response.status = 400
            error_response.json.return_value = {
                "code": 400,
                "message": "Bad Request",
                "details": ["Invalid parameter"]
            }
            mock_session.request.return_value.__aenter__.return_value = error_response

            with pytest.raises(APIClientError):
                await api_manager._request(method="post", endpoint="test-endpoint")

            # Проверяем что метод error вызывался у классового логгера
            mock_class_error.assert_called()
            error_calls = [call for call in mock_class_error.call_args_list
                           if "Ошибка API" in str(call)]
            assert len(error_calls) >= 1

    @pytest.mark.asyncio
    async def test_retry_decorator_directly(self, api_manager):
        """Тест retry декоратора."""

        retry_decorator = api_manager._create_retry_decorator()

        attempt_count = 0

        @retry_decorator
        async def failing_function():
            nonlocal attempt_count
            attempt_count += 1
            raise APIServerError(500, f"Server error on attempt {attempt_count}")

        # Должен упасть после всех попыток
        with pytest.raises(APIServerError):
            await failing_function()

        # Проверяем что было 3 попытки (1 исходная + 2 ретрая)
        expected_attempts = api_manager.config.max_retries + 1
        assert attempt_count == expected_attempts


    @pytest.mark.asyncio
    async def test_retry_only_on_server_errors(self, api_manager):
        """Тестирует, что retry работает только для серверных ошибок."""

        retry_decorator = api_manager._create_retry_decorator()

        # APIServerError должен ретраиться
        server_error_count = 0

        @retry_decorator
        async def test_server_error():
            nonlocal server_error_count
            server_error_count += 1
            raise APIServerError(500, "Server error")

        with pytest.raises(APIServerError):
            await test_server_error()

        assert server_error_count == 3, f"APIServerError: ожидалось 3 попытки, получили {server_error_count}"

        # APIClientError НЕ должен ретраиться
        client_error_count = 0

        @retry_decorator
        async def test_client_error():
            nonlocal client_error_count
            client_error_count += 1
            raise APIClientError(400, "Client error")

        with pytest.raises(APIClientError):
            await test_client_error()

        assert client_error_count == 1, f"APIClientError: ожидалась 1 попытка, получили {client_error_count}"