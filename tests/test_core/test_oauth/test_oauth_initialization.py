"""Тесты инициализации OAuth в APIManager."""
from unittest.mock import patch, Mock

from src.ozonapi.seller.core.core import APIManager


class TestOAuthInitialization:
    """Тесты инициализации OAuth в APIManager."""

    def test_oauth_manager_creation_with_token(self, mock_config):
        """Тест создания менеджера с OAuth токеном."""
        with patch('src.ozonapi.seller.core.core.load_dotenv'), \
             patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:

            mock_config_class.return_value = mock_config

            manager = APIManager(token="some_token")

            assert manager is not None
            assert manager._token == "some_token"

    def test_oauth_auth_type_property(self, api_manager_with_token):
        """Тест свойства auth_type для OAuth."""
        assert api_manager_with_token.auth_type == "oauth"