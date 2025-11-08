"""Тесты обработки OAuth токенов в APIManager."""
from unittest.mock import patch, Mock

from src.ozonapi.seller.core.core import APIManager


class TestOAuthTokenProcessing:
    """Тесты обработки OAuth токенов в APIManager."""

    def test_bearer_prefix_removal(self, api_manager_with_bearer_token):
        """Тест удаления Bearer префикса из токена."""
        assert api_manager_with_bearer_token._token == "test_token"

    def test_oauth_token_persistence(self, mock_config):
        """Тест сохранения OAuth токена."""
        with patch('src.ozonapi.seller.core.core.load_dotenv'), \
                patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:
            mock_config_class.return_value = mock_config

            manager = APIManager(token="test_token_123")

            assert manager._token == "test_token_123"
            assert manager.auth_type == "oauth"