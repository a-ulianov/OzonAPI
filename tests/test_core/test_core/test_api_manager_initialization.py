"""Тесты инициализации APIManager."""
import pytest
from unittest.mock import patch, Mock

from src.ozonapi.seller.core.core import APIManager


class TestAPIManagerInitialization:
    """Тесты инициализации APIManager."""

    def test_initialization_with_api_key_credentials(self, api_manager):
        """Тест инициализации с API key аутентификацией."""
        assert api_manager._client_id == "test_client"
        assert api_manager._api_key == "test_api_key"
        assert api_manager._token is None
        assert api_manager.auth_type == "api_key"

    def test_initialization_with_oauth_token(self, api_manager_with_token):
        """Тест инициализации с OAuth токеном."""
        assert api_manager_with_token._token == "test_oauth_token"
        assert api_manager_with_token._api_key is None
        assert api_manager_with_token.auth_type == "oauth"


class TestAPIManagerValidation:
    """Тесты валидации APIManager."""

    @patch('src.ozonapi.seller.core.core.load_dotenv')
    def test_validation_fails_with_no_credentials(self, mock_load_dotenv):
        """Тест провала валидации при отсутствии учетных данных."""
        with patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:
            # Конфиг без учетных данных
            mock_config = Mock()
            mock_config.client_id = None
            mock_config.api_key = None
            mock_config.token = None
            mock_config_class.return_value = mock_config

            with pytest.raises(ValueError, match="Не предоставлены авторизационные данные"):
                APIManager()

    @patch('src.ozonapi.seller.core.core.load_dotenv')
    def test_validation_fails_with_invalid_api_key(self, mock_load_dotenv):
        """Тест провала валидации при неполных API key данных."""
        with patch('src.ozonapi.seller.core.core.APIConfig') as mock_config_class:
            mock_config = Mock()
            mock_config.client_id = None
            mock_config.api_key = "some_key"
            mock_config.token = None
            mock_config_class.return_value = mock_config

            with pytest.raises(ValueError, match="client_id должен быть непустой строкой"):
                APIManager()