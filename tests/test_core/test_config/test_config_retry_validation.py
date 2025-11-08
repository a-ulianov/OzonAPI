"""Тесты валидации параметров повторов в APIConfig."""
import pytest
from pydantic import ValidationError

from src.ozonapi.seller.core import APIConfig


class TestAPIConfigRetryValidation:
    """Тесты валидации параметров повторов APIConfig."""

    def test_retry_times_validation_success(self):
        """Тест успешной валидации времени повторов."""
        config = APIConfig(retry_min_wait=2.0, retry_max_wait=5.0)
        assert config.retry_min_wait == 2.0
        assert config.retry_max_wait == 5.0

    def test_retry_times_validation_failure(self):
        """Тест неуспешной валидации времени повторов."""
        with pytest.raises(ValidationError, match="retry_max_wait должен быть больше или равен retry_min_wait"):
            APIConfig(retry_min_wait=5.0, retry_max_wait=2.0)