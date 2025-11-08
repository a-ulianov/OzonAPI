"""Тесты очистки неиспользуемых инстансов."""
import weakref
from unittest.mock import Mock

from src.ozonapi.seller.core.rate_limiter import RateLimiterManager, InstanceData


class TestRateLimiterManagerCleanup:
    """Тесты очистки неиспользуемых инстансов."""

    def test_clear_register_removes_none_weakrefs(self, mock_api_manager):
        """Тест удаления weakref-ов указывающих на None."""

        temp_instance = Mock()
        temp_instance.client_id = "temp_client"
        temp_instance.config = Mock()
        temp_instance.config.max_requests_per_second = 10
        temp_instance.config.min_instance_ttl = 300.0

        register = RateLimiterManager.get_or_create_client_register(temp_instance)
        instance_ref = weakref.ref(temp_instance)

        instance_data = Mock()
        instance_data.updated_at = 1000.0
        instance_data.config = temp_instance.config

        register.data[instance_ref] = instance_data

        assert instance_ref in register.data

        RateLimiterManager.clear_register_by_ttl()

        assert instance_ref in register.data

    def test_clear_register_preserves_active_instances(self, mock_api_manager):
        """Тест что активные инстансы не удаляются при очистке."""

        RateLimiterManager.get_or_register_instance(mock_api_manager)
        client_id = mock_api_manager.client_id

        register = RateLimiterManager._clients[client_id]
        active_instances_before = len([
            ref for ref in register.data.keys()
            if ref() is not None
        ])

        RateLimiterManager.clear_register_by_ttl()

        active_instances_after = len([
            ref for ref in register.data.keys()
            if ref() is not None
        ])

        assert active_instances_after == active_instances_before