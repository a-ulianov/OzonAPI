"""Тесты смешанной аутентификации в APIManager."""
from unittest.mock import patch, Mock

from src.ozonapi.seller.core.core import APIManager


class TestOAuthMixedAuth:
    """Тесты смешанной аутентификации в APIManager."""

    def test_mixed_auth_credentials_persistence(self, api_manager_with_mixed_auth):
        """Тест сохранения учетных данных при смешанной аутентификации."""
        manager = api_manager_with_mixed_auth

        assert manager._client_id == "test_client"
        assert manager._api_key == "test_key"
        assert manager._token == "test_token"

    def test_oauth_priority_in_mixed_auth(self, mock_config):
        """Тест приоритета OAuth при смешанной аутентификации."""
        with patch('src.ozonapi.seller.core.core.load_dotenv'), \
                patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:
            mock_config_class.return_value = mock_config

            manager = APIManager(
                client_id="test_client",
                api_key="test_key",
                token="oauth_token"
            )

            assert manager.auth_type == "oauth"
            assert manager._token == "oauth_token"