"""Фикстуры для тестирования OAuth функциональности."""
import pytest
from unittest.mock import patch, Mock

from src.ozonapi.seller.core.core import APIManager


@pytest.fixture
def mock_config():
    """Создает полный мок конфигурации."""
    config = Mock()
    config.client_id = None
    config.api_key = None
    config.token = None
    config.base_url = "https://api-seller.ozon.ru"
    config.max_requests_per_second = 10
    config.request_timeout = 30.0
    config.max_retries = 3
    config.retry_min_wait = 1.0
    config.retry_max_wait = 5.0
    config.cleanup_interval = 300.0
    config.min_instance_ttl = 300.0
    config.connector_limit = 100
    # Атрибуты для логирования
    config.log_level = 'ERROR'
    config.log_json = False
    config.log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    config.log_dir = None
    config.log_file = None
    config.log_max_bytes = 10 * 1024 * 1024
    config.log_backup_files_count = 5
    config.logger = Mock()
    return config


@pytest.fixture
def api_manager_with_token(mock_config):
    """Создает APIManager с OAuth токеном."""
    with patch('src.ozonapi.seller.core.core.load_dotenv'), \
         patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:

        mock_config_class.return_value = mock_config

        manager = APIManager(token="test_oauth_token")
        return manager


@pytest.fixture
def api_manager_with_bearer_token(mock_config):
    """Создает APIManager с Bearer токеном."""
    with patch('src.ozonapi.seller.core.core.load_dotenv'), \
         patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:

        mock_config_class.return_value = mock_config

        manager = APIManager(token="Bearer test_token")
        return manager


@pytest.fixture
def api_manager_with_mixed_auth(mock_config):
    """Создает APIManager со смешанной аутентификацией."""
    with patch('src.ozonapi.seller.core.core.load_dotenv'), \
         patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:

        mock_config_class.return_value = mock_config

        manager = APIManager(
            client_id="test_client",
            api_key="test_key",
            token="test_token"
        )
        return manager