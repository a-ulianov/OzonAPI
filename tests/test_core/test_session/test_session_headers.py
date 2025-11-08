"""Тесты генерации заголовков."""
from src.ozonapi.seller.core.sessions import SessionManager


class TestSessionHeaders:
    """Тесты генерации заголовков."""

    def test_oauth_headers_generation(self):
        """Тест заголовков для OAuth авторизации."""
        headers = SessionManager._get_headers(
            client_id="client123",
            api_key="api_key",
            token="oauth_token"
        )

        assert headers == {"Authorization": "Bearer oauth_token"}

    def test_api_key_headers_generation(self):
        """Тест заголовков для API Key авторизации."""
        headers = SessionManager._get_headers(
            client_id="client123",
            api_key="api_key_456",
            token=None
        )

        assert headers == {
            "Client-Id": "client123",
            "Api-Key": "api_key_456"
        }

    def test_headers_generation_validation_error(self):
        """Тест ошибки при недостаточных данных для авторизации."""
        try:
            SessionManager._get_headers(
                client_id=None,
                api_key=None,
                token=None
            )
            assert False, "Expected ValueError"
        except ValueError as e:
            assert "Недостаточно данных для авторизации" in str(e)