import pytest

from src.ozonapi.seller.schemas.returns import ReturnsSettingsUtilizationHistoryResponse


class TestReturnsSettingsUtilizationHistory:
    """Тесты для метода returns_settings_utilization_history."""

    @pytest.mark.asyncio
    async def test_returns_settings_utilization_history(self, api, mock_api_request):
        """Тестирует метод returns_settings_utilization_history."""

        mock_response_data = {
            "history": [
                {"descriptions": ["enabled"], "updated_at": "2026-06-01T10:00:00Z", "user_name": "ivan"}
            ]
        }
        mock_api_request.return_value = mock_response_data

        response = await api.returns_settings_utilization_history()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="returns/settings/utilization/history",
            payload={}
        )

        assert isinstance(response, ReturnsSettingsUtilizationHistoryResponse)
        assert response.history[0].user_name == "ivan"
