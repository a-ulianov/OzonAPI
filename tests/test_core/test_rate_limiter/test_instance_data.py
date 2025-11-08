import time

from src.ozonapi.seller.core.rate_limiter import InstanceData


class TestInstanceData:
    """Тесты для класса InstanceData."""

    def test_instance_data_initialization(self, mock_api_manager):
        """Тест инициализации InstanceData."""
        instance_data = InstanceData(instance=mock_api_manager)

        assert instance_data.client_id == mock_api_manager.client_id
        assert instance_data.config == mock_api_manager.config
        assert instance_data.limiter is not None
        assert instance_data.updated_at > 0

    def test_instance_data_update_method(self, mock_api_manager):
        """Тест метода update()."""
        instance_data = InstanceData(instance=mock_api_manager)

        original_monotonic = time.monotonic
        time.monotonic = lambda: 1000.0
        instance_data.update()
        first_time = instance_data.updated_at

        time.monotonic = lambda: 1001.0
        instance_data.update()
        second_time = instance_data.updated_at

        time.monotonic = original_monotonic

        assert second_time > first_time
        assert second_time == 1001.0
        assert first_time == 1000.0