import os
import tempfile
from typing import Dict, Any
from unittest.mock import patch

import pytest
from pydantic import ValidationError

from src.ozonapi.seller.core.config import APIConfig


class TestAPIConfig:
    """Тесты для класса APIConfig."""

    def test_custom_values(self):
        """Тестирование пользовательских значений."""
        custom_values = {
            "client_id": "test_client",
            "api_key": "test_key",
            "base_url": "https://test-api.ozon.ru",
            "max_requests_per_second": 25,
            "cleanup_interval": 150.0,
            "min_instance_ttl": 150.0,
            "connector_limit": 50,
            "request_timeout": 15.0,
            "max_retries": 5,
            "retry_min_wait": 2.0,
            "retry_max_wait": 8.0,
        }

        config = APIConfig(**custom_values)

        for key, value in custom_values.items():
            assert getattr(config, key) == value

    def test_base_url_validation_success(self):
        """Тестирование валидации base_url."""
        valid_urls = [
            "https://api-seller.ozon.ru",
            "http://localhost:8000",
            "https://test.example.com/api",
        ]

        for url in valid_urls:
            config = APIConfig(base_url=url)
            assert config.base_url == url.rstrip("/")

        invalid_urls = [
            "api-seller.ozon.ru",  # отсутствует схема
            "ftp://api-seller.ozon.ru",  # неподдерживаемая схема
            "://invalid-url",  # некорректный URL
        ]

        for url in invalid_urls:
            with pytest.raises(ValidationError, match="URL должен начинаться с http:// или https://"):
                APIConfig(base_url=url)

    def test_base_url_trailing_slash_removal(self):
        """Тестирование удаления завершающего слеша из base_url."""
        config = APIConfig(base_url="https://api-seller.ozon.ru/")
        assert config.base_url == "https://api-seller.ozon.ru"

    def test_retry_times_validation_success(self):
        """Тестирование успешной валидации времени повторов."""
        config = APIConfig(retry_min_wait=2.0, retry_max_wait=5.0)
        assert config.retry_min_wait == 2.0
        assert config.retry_max_wait == 5.0

    def test_retry_times_validation_failure(self):
        """Тестирование неуспешной валидации времени повторов."""
        with pytest.raises(ValidationError, match="retry_max_wait должен быть больше или равен retry_min_wait"):
            APIConfig(retry_min_wait=5.0, retry_max_wait=2.0)

    def test_numeric_constraints_validation(self):
        """Тестирование валидации числовых ограничений."""
        # max_requests_per_second вне диапазона
        with pytest.raises(ValidationError):
            APIConfig(max_requests_per_second=0)

        with pytest.raises(ValidationError):
            APIConfig(max_requests_per_second=51)

        # max_retries вне диапазона
        with pytest.raises(ValidationError):
            APIConfig(max_retries=-1)

        with pytest.raises(ValidationError):
            APIConfig(max_retries=100)

        # connector_limit меньше минимального значения
        with pytest.raises(ValidationError):
            APIConfig(connector_limit=0)

    @pytest.mark.parametrize("env_vars,expected_values", [
        (
                {
                    "OZON_SELLER_CLIENT_ID": "env_client",
                    "OZON_SELLER_API_KEY": "env_key",
                    "OZON_SELLER_BASE_URL": "https://env-api.ozon.ru",
                },
                {
                    "client_id": "env_client",
                    "api_key": "env_key",
                    "base_url": "https://env-api.ozon.ru",
                }
        ),
    ])
    def test_env_variables_loading(self, env_vars: Dict[str, str], expected_values: Dict[str, Any]):
        """Тестирование загрузки переменных окружения."""
        with patch.dict(os.environ, env_vars):
            config = APIConfig()

            for key, expected_value in expected_values.items():
                assert getattr(config, key) == expected_value

    def test_env_file_loading(self):
        """Тестирование загрузки из .env файла."""
        env_content = """OZON_SELLER_CLIENT_ID=file_client
    OZON_SELLER_API_KEY=file_key
    OZON_SELLER_BASE_URL=https://file-api.ozon.ru
    OZON_SELLER_MAX_REQUESTS_PER_SECOND=40
    """

        with tempfile.NamedTemporaryFile(mode='w', suffix='.env', delete=False) as f:
            f.write(env_content)
            temp_env_file = f.name

        try:
            # Временное переопределение env_file через наследование
            class TempAPIConfig(APIConfig):
                model_config = APIConfig.model_config.copy()
                model_config['env_file'] = temp_env_file

            config = TempAPIConfig()

            assert config.client_id == "file_client"
            assert config.api_key == "file_key"
            assert config.base_url == "https://file-api.ozon.ru"
            assert config.max_requests_per_second == 40
        finally:
            os.unlink(temp_env_file)

    def test_case_insensitive_env_variables(self):
        """Тестирование нечувствительности к регистру переменных окружения."""
        env_vars = {
            "ozon_seller_client_id": "lowercase_client",
            "OZON_SELLER_API_KEY": "uppercase_key",
        }

        with patch.dict(os.environ, env_vars):
            config = APIConfig()

            assert config.client_id == "lowercase_client"
            assert config.api_key == "uppercase_key"

    def test_extra_fields_ignored(self):
        """Тестирование игнорирования дополнительных полей."""
        config = APIConfig(
            client_id="test_client",
            unknown_field="should_be_ignored",  # type: ignore
            another_unknown=123  # type: ignore
        )

        assert config.client_id == "test_client"
        assert not hasattr(config, "unknown_field")
        assert not hasattr(config, "another_unknown")