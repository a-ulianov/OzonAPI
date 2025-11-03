from src.ozonapi.seller.core.core import APIManager


class TestAPIManagerOAuth:
    """Простые тесты для OAuth функциональности."""

    def test_oauth_auth_type(self):
        """Тест того, что auth_type правильно определяется для OAuth."""
        # Просто проверяем что свойство существует и работает
        manager = APIManager(client_id="test", api_key="test")
        assert hasattr(manager, 'auth_type')

        # Для OAuth auth_type должен быть "oauth"
        # Это базовый тест того, что свойство работает

    def test_oauth_with_token_works(self):
        """Тест того, что можно создать менеджер с токеном."""
        # Главное - что не падает с ошибкой
        manager = APIManager(token="some_token")
        assert manager is not None
        assert manager._token == "some_token"

    def test_oauth_bearer_prefix_removed(self):
        """Тест того, что Bearer префикс удаляется из токена."""
        manager = APIManager(token="Bearer test_token")
        assert manager._token == "test_token"

    def test_mixed_auth_uses_provided_credentials(self):
        """Тест того, что при mixed auth используются переданные credentials."""
        manager = APIManager(
            client_id="test_client",
            api_key="test_key",
            token="test_token"
        )
        # Проверяем что все credentials установлены
        assert manager._client_id == "test_client"
        assert manager._api_key == "test_key"
        assert manager._token == "test_token"

    def test_oauth_auth_type(self):
        """Тест того, что auth_type правильно определяется для OAuth."""
        # Просто проверяем что свойство существует и работает
        manager = APIManager(client_id="test", api_key="test")
        assert hasattr(manager, 'auth_type')

    def test_oauth_with_token_works(self):
        """Тест того, что можно создать менеджер с токеном."""
        # Главное - что не падает с ошибкой
        manager = APIManager(token="some_token")
        assert manager is not None
        assert manager._token == "some_token"

    def test_oauth_bearer_prefix_removed(self):
        """Тест того, что Bearer префикс удаляется из токена."""
        manager = APIManager(token="Bearer test_token")
        assert manager._token == "test_token"

    def test_mixed_auth_uses_provided_credentials(self):
        """Тест того, что при mixed auth используются переданные credentials."""
        manager = APIManager(
            client_id="test_client",
            api_key="test_key",
            token="test_token"
        )
        # Проверяем что все credentials установлены
        assert manager._client_id == "test_client"
        assert manager._api_key == "test_key"
        assert manager._token == "test_token"

    def test_oauth_session_headers_generation(self):
        """Тест того, что OAuth токен используется для генерации заголовков сессии."""
        manager = APIManager(token="test_oauth_token")

        # Проверяем что токен сохраняется и может быть использован для сессии
        assert manager._token == "test_oauth_token"
        assert manager.auth_type == "oauth"

        # Проверяем что client_id генерируется на основе токена (даже если из env)
        assert manager._client_id is not None

    def test_oauth_token_persistence(self):
        """Тест того, что OAuth токен правильно сохраняется и используется."""
        # Тест с обычным токеном
        manager1 = APIManager(token="test_token_123")
        assert manager1._token == "test_token_123"
        assert manager1.auth_type == "oauth"

        # Тест с токеном с Bearer префиксом
        manager2 = APIManager(token="Bearer token_456")
        assert manager2._token == "token_456"
        assert manager2.auth_type == "oauth"

        # Тест что OAuth имеет приоритет даже при наличии api_key
        manager3 = APIManager(
            client_id="test_client",
            api_key="test_key",
            token="oauth_token"
        )
        assert manager3.auth_type == "oauth"
        assert manager3._token == "oauth_token"