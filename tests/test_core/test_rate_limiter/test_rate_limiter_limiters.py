"""Тесты ограничителей запросов."""


class TestRateLimiterManagerLimiters:
    """Тесты ограничителей запросов."""

    def test_instance_limiter_property(self, rate_limiter_manager):
        """Тест свойства instance_limiter."""
        limiter1 = rate_limiter_manager.instance_limiter
        limiter2 = rate_limiter_manager.instance_limiter

        assert limiter1 is limiter2
        assert limiter1 is not None

    def test_client_limiter_property(self, rate_limiter_manager):
        """Тест свойства client_limiter."""
        limiter = rate_limiter_manager.client_limiter

        assert limiter is not None
        assert limiter is rate_limiter_manager._client_limiter