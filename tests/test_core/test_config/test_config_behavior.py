"""Тесты поведения APIConfig."""

from src.ozonapi.seller.core import APIConfig


class TestAPIConfigBehavior:
    """Тесты поведения APIConfig."""

    def test_base_url_trailing_slash_removal(self):
        """Тест удаления завершающего слеша из base_url."""
        config = APIConfig(base_url="https://api-seller.ozon.ru/")
        assert config.base_url == "https://api-seller.ozon.ru"

    def test_extra_fields_ignored(self):
        """Тест игнорирования дополнительных полей."""
        config = APIConfig(
            client_id="test_client",
            unknown_field="should_be_ignored",  # type: ignore
            another_unknown=123  # type: ignore
        )

        assert config.client_id == "test_client"
        assert not hasattr(config, "unknown_field")
        assert not hasattr(config, "another_unknown")