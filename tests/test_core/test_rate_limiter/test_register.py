"""Тесты для класса Register."""
import weakref

from src.ozonapi.seller.core.rate_limiter import Register, InstanceData


class TestRegister:
    """Тесты для класса Register."""

    def test_register_initialization(self):
        """Тест инициализации Register."""
        register = Register()

        assert register.data == {}
        assert register.limiter is not None
        assert register.limiter.max_rate > 0

    def test_register_data_management(self, mock_api_manager):
        """Тест управления данными в Register."""
        register = Register()
        instance_data = InstanceData(instance=mock_api_manager)
        instance_ref = weakref.ref(mock_api_manager)

        register.data[instance_ref] = instance_data

        assert instance_ref in register.data
        assert register.data[instance_ref] == instance_data