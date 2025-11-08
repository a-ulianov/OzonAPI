"""Тесты инициализации APIConfig."""
from src.ozonapi.seller.core import APIConfig


class TestAPIConfigInitialization:
    """Тесты базовой инициализации APIConfig."""

    def test_config_creation_with_custom_values(self):
        """Тест создания конфигурации с пользовательскими значениями."""
        config = APIConfig(
            client_id="test_client",
            api_key="test_key",
            base_url="https://test-api.ozon.ru",
            max_requests_per_second=25
        )

        assert config.client_id == "test_client"
        assert config.api_key == "test_key"
        assert config.base_url == "https://test-api.ozon.ru"
        assert config.max_requests_per_second == 25

    def test_config_creation_with_default_values(self):
        """Тест создания конфигурации со значениями по умолчанию."""
        config = APIConfig()

        assert config.base_url == "https://api-seller.ozon.ru"
        assert config.max_requests_per_second == 27
        assert config.connector_limit == 100