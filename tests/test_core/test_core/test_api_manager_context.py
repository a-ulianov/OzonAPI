"""Тесты контекстного менеджера APIManager."""
import pytest


class TestAPIManagerContext:
    """Тесты контекстного менеджера APIManager."""

    @pytest.mark.asyncio
    async def test_context_manager_enters_and_exits(self, api_manager):
        """Тест входа и выхода из контекстного менеджера."""
        async with api_manager as manager:
            assert manager == api_manager
            assert not manager.is_closed

        assert api_manager.is_closed

    @pytest.mark.asyncio
    async def test_context_manager_with_closed_client_fails(self, api_manager):
        """Тест ошибки при использовании закрытого клиента."""
        api_manager._closed = True

        with pytest.raises(RuntimeError, match="Невозможно использовать закрытый API-клиент"):
            async with api_manager:
                pass