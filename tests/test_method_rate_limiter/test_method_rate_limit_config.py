"""Тесты MethodRateLimitConfig."""
import pytest

from src.ozonapi.seller.core.method_rate_limiter import MethodRateLimitConfig


class TestMethodRateLimitConfigInitialization:
    """Тесты инициализации MethodRateLimitConfig."""

    def test_config_initialization(self):
        """Тест инициализации конфигурации ограничителя метода."""
        config = MethodRateLimitConfig(
            limit_requests=15,
            interval_seconds=3.0,
            method_identifier="api.test_method"
        )

        assert config.limit_requests == 15
        assert config.interval_seconds == 3.0
        assert config.method_identifier == "api.test_method"


class TestMethodRateLimitConfigValidation:
    """Тесты валидации MethodRateLimitConfig."""

    def test_config_validation_success(self):
        """Тест успешной валидации конфигурации."""
        MethodRateLimitConfig(
            limit_requests=1,  # Минимальное значение
            interval_seconds=0.1,  # Больше 0
            method_identifier="test"
        )

    def test_config_validation_failure(self):
        """Тест неуспешной валидации конфигурации."""
        with pytest.raises(ValueError):
            MethodRateLimitConfig(
                limit_requests=0,  # Меньше 1
                interval_seconds=1.0,
                method_identifier="test"
            )

        with pytest.raises(ValueError):
            MethodRateLimitConfig(
                limit_requests=5,
                interval_seconds=0,  # Меньше или равно 0
                method_identifier="test"
            )