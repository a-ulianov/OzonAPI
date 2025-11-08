"""Тесты загрузки из .env файла в APIConfig."""
from src.ozonapi.seller.core import APIConfig


class TestAPIConfigEnvFileLoading:
    """Тесты загрузки из .env файла APIConfig."""

    def test_env_file_loading(self, temp_env_file):
        """Тест загрузки из .env файла."""
        # Временное переопределение env_file через наследование
        class TempAPIConfig(APIConfig):
            model_config = APIConfig.model_config.copy()
            model_config['env_file'] = temp_env_file

        config = TempAPIConfig()

        assert config.client_id == "file_client"
        assert config.api_key == "file_key"
        assert config.base_url == "https://file-api.ozon.ru"
        assert config.max_requests_per_second == 40