"""Тесты валидации APIConfig."""
import pytest
from pydantic import ValidationError

from src.ozonapi.seller.core import APIConfig


class TestAPIConfigURLValidation:
    """Тесты валидации URL в APIConfig."""

    def test_base_url_validation_success(self):
        """Тест успешной валидации base_url."""
        valid_urls = [
            "https://api-seller.ozon.ru",
            "http://localhost:8000",
            "https://test.example.com/api",
        ]

        for url in valid_urls:
            config = APIConfig(base_url=url)
            assert config.base_url == url.rstrip("/")

    def test_base_url_validation_failure(self):
        """Тест неуспешной валидации base_url."""
        invalid_urls = [
            "api-seller.ozon.ru",  # отсутствует схема
            "ftp://api-seller.ozon.ru",  # неподдерживаемая схема
        ]

        for url in invalid_urls:
            with pytest.raises(ValidationError, match="URL должен начинаться с http:// или https://"):
                APIConfig(base_url=url)


class TestAPIConfigNumericValidation:
    """Тесты валидации числовых полей в APIConfig."""

    def test_numeric_constraints_validation_success(self):
        """Тест успешной валидации числовых ограничений."""
        config = APIConfig(
            max_requests_per_second=30,
            max_retries=5,
            connector_limit=50
        )

        assert config.max_requests_per_second == 30
        assert config.max_retries == 5
        assert config.connector_limit == 50

    def test_numeric_constraints_validation_failure(self):
        """Тест неуспешной валидации числовых ограничений."""
        with pytest.raises(ValidationError):
            APIConfig(max_requests_per_second=0)

        with pytest.raises(ValidationError):
            APIConfig(max_requests_per_second=51)