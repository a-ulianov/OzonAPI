"""Тесты OAuth сессий в APIManager."""
from unittest.mock import patch, Mock

from src.ozonapi.seller.core.core import APIManager


class TestOAuthSession:
    """Тесты OAuth сессий в APIManager."""

    def test_oauth_session_headers_generation(self, api_manager_with_token):
        """Тест генерации заголовков для OAuth сессии."""
        manager = api_manager_with_token

        assert manager._token == "test_oauth_token"
        assert manager.auth_type == "oauth"
        assert manager._client_id is not None

    def test_oauth_client_id_generation(self, mock_config):
        """Тест генерации client_id для OAuth аутентификации."""
        with patch('src.ozonapi.seller.core.core.load_dotenv'), \
                patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:
            mock_config_class.return_value = mock_config

            manager = APIManager(token="test_token")

            # Проверяем что client_id генерируется на основе токена
            assert manager._client_id is not None
            assert manager._client_id.startswith("OAuth")