"""Тесты управления инстансами в RateLimiterManager."""
from src.ozonapi.seller.core.rate_limiter import RateLimiterManager


class TestRateLimiterManagerInstanceManagement:
    """Тесты управления инстансами в RateLimiterManager."""

    def test_get_or_create_client_register(self, mock_api_manager):
        """Тест получения или создания регистра клиента."""
        # Первый вызов создает регистр
        register1 = RateLimiterManager.get_or_create_client_register(mock_api_manager)
        assert mock_api_manager.client_id in RateLimiterManager._clients

        # Второй вызов возвращает существующий регистр
        register2 = RateLimiterManager.get_or_create_client_register(mock_api_manager)
        assert register1 is register2

    def test_get_or_register_instance(self, mock_api_manager):
        """Тест регистрации инстанса."""
        # Первая регистрация
        instance_data1 = RateLimiterManager.get_or_register_instance(mock_api_manager)
        assert instance_data1 is not None

        # Повторная регистрация того же инстанса
        instance_data2 = RateLimiterManager.get_or_register_instance(mock_api_manager)
        assert instance_data1 is instance_data2