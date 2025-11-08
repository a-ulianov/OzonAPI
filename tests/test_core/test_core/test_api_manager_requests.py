"""Тесты выполнения запросов APIManager."""
import pytest
from unittest.mock import patch

from src.ozonapi.seller.core.exceptions import APIError


class TestAPIManagerRequestExecution:
    """Тесты выполнения запросов APIManager."""

    @pytest.mark.asyncio
    async def test_request_with_closed_client_fails(self, api_manager):
        """Тест ошибки при запросе с закрытым клиентом."""
        api_manager._closed = True

        with pytest.raises(RuntimeError, match="API-клиент остановлен"):
            await api_manager._request(endpoint="test")

    @pytest.mark.asyncio
    async def test_request_handles_network_errors(self, api_manager):
        """Тест обработки сетевых ошибок."""
        with patch.object(api_manager, '_request') as mock_request:
            mock_request.side_effect = APIError(0, "Network error: Connection failed")

            with pytest.raises(APIError, match="Network error"):
                await api_manager._request(endpoint="test")