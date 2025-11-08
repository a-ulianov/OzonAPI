"""Фикстуры для тестирования APIManager."""
import pytest
from unittest.mock import Mock, AsyncMock, patch
import asyncio

from src.ozonapi.seller.core.config import APIConfig
from src.ozonapi.seller.core.core import APIManager


@pytest.fixture
def api_config():
    """Создает тестовую конфигурацию API."""
    # Используем model_construct чтобы обойти валидацию
    return APIConfig.model_construct(
        client_id=None,
        api_key=None,
        token=None,
        base_url="https://api-seller.ozon.ru",
        max_requests_per_second=10,
        request_timeout=30.0,
        max_retries=3
    )


@pytest.fixture
def mock_api_manager():
    """Создает мок APIManager."""
    manager = Mock(spec=APIManager)
    manager._client_id = "test_client"
    manager._api_key = "test_api_key"
    manager._token = None
    manager._closed = False
    manager.client_id = "test_client"
    manager.is_closed = False
    manager.auth_type = "api_key"
    return manager


@pytest.fixture
async def api_manager():
    """Создает экземпляр APIManager для тестирования."""
    # Сохраняем оригинальные менеджеры
    original_session_manager = APIManager._session_manager
    original_method_limiter_manager = APIManager._method_rate_limiter_manager
    original_initialized = APIManager._initialized

    # Сбрасываем для чистого теста
    APIManager._session_manager = None
    APIManager._method_rate_limiter_manager = None
    APIManager._initialized = False

    # Мокаем загрузку .env и создаем чистый конфиг
    with patch('src.ozonapi.seller.core.core.load_dotenv'), \
         patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:

        # Создаем чистый конфиг без данных
        clean_config = APIConfig.model_construct(
            client_id=None,
            api_key=None,
            token=None,
            base_url="https://api-seller.ozon.ru"
        )
        mock_config_class.return_value = clean_config

        manager = APIManager(
            client_id="test_client",
            api_key="test_api_key"
        )

    yield manager

    # Очищаем ресурсы
    if hasattr(manager, '_logging_manager') and manager._logging_manager:
        manager._logging_manager.shutdown()

    # Восстанавливаем оригинальные менеджеры
    APIManager._session_manager = original_session_manager
    APIManager._method_rate_limiter_manager = original_method_limiter_manager
    APIManager._initialized = original_initialized


@pytest.fixture
async def api_manager_with_token():
    """Создает экземпляр APIManager с OAuth токеном."""
    # Сохраняем оригинальные менеджеры
    original_session_manager = APIManager._session_manager
    original_method_limiter_manager = APIManager._method_rate_limiter_manager
    original_initialized = APIManager._initialized

    # Сбрасываем для чистого теста
    APIManager._session_manager = None
    APIManager._method_rate_limiter_manager = None
    APIManager._initialized = False

    # Мокаем загрузку .env и создаем чистый конфиг
    with patch('src.ozonapi.seller.core.core.load_dotenv'), \
         patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:

        # Создаем чистый конфиг без данных
        clean_config = APIConfig.model_construct(
            client_id=None,
            api_key=None,
            token=None,
            base_url="https://api-seller.ozon.ru"
        )
        mock_config_class.return_value = clean_config

        manager = APIManager(token="test_oauth_token")

    yield manager

    # Очищаем ресурсы
    if hasattr(manager, '_logging_manager') and manager._logging_manager:
        manager._logging_manager.shutdown()

    # Восстанавливаем оригинальные менеджеры
    APIManager._session_manager = original_session_manager
    APIManager._method_rate_limiter_manager = original_method_limiter_manager
    APIManager._initialized = original_initialized


# Остальные фикстуры для моков
@pytest.fixture
def mock_session_manager():
    session_manager = Mock()
    session_manager.get_session = AsyncMock()
    session_manager.remove_instance = AsyncMock()
    session_manager.close_all = AsyncMock()
    return session_manager


@pytest.fixture
def mock_rate_limiter():
    rate_limiter = Mock()
    rate_limiter.instance_limiter = Mock()
    rate_limiter.client_limiter = Mock()
    rate_limiter.instance_limiter.__aenter__ = AsyncMock(return_value=AsyncMock())
    rate_limiter.instance_limiter.__aexit__ = AsyncMock(return_value=None)
    rate_limiter.client_limiter.__aenter__ = AsyncMock(return_value=AsyncMock())
    rate_limiter.client_limiter.__aexit__ = AsyncMock(return_value=None)
    return rate_limiter


@pytest.fixture
def mock_method_rate_limiter_manager():
    method_limiter = Mock()
    method_limiter.start = AsyncMock()
    method_limiter.shutdown = AsyncMock()
    method_limiter.get_limiter = AsyncMock()
    method_limiter.get_limiter_stats = AsyncMock(return_value={})
    return method_limiter


@pytest.fixture
def mock_aiohttp_response():
    response = Mock()
    response.status = 200
    response.json = AsyncMock(return_value={"result": "success"})
    return response


@pytest.fixture
def mock_aiohttp_session(mock_aiohttp_response):
    session = Mock()
    session.request = AsyncMock(return_value=mock_aiohttp_response)
    session.close = AsyncMock()
    session.closed = False
    return session