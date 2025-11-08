"""Тесты загрузки переменных окружения в APIConfig."""
import os
from unittest.mock import patch

from src.ozonapi.seller.core import APIConfig


class TestAPIConfigEnvironmentVariables:
    """Тесты загрузки переменных окружения APIConfig."""

    def test_env_variables_loading(self):
        """Тест загрузки переменных окружения."""
        env_vars = {
            "OZON_SELLER_CLIENT_ID": "env_client",
            "OZON_SELLER_API_KEY": "env_key",
            "OZON_SELLER_BASE_URL": "https://env-api.ozon.ru",
        }

        with patch.dict(os.environ, env_vars):
            config = APIConfig()

            assert config.client_id == "env_client"
            assert config.api_key == "env_key"
            assert config.base_url == "https://env-api.ozon.ru"

    def test_case_insensitive_env_variables(self):
        """Тест нечувствительности к регистру переменных окружения."""
        env_vars = {
            "ozon_seller_client_id": "lowercase_client",
            "OZON_SELLER_API_KEY": "uppercase_key",
        }

        with patch.dict(os.environ, env_vars):
            config = APIConfig()

            assert config.client_id == "lowercase_client"
            assert config.api_key == "uppercase_key"