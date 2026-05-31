import pytest

from src.ozonapi.seller.schemas.returns import ReturnsSettingsUtilizationInfoResponse


class TestReturnsSettingsUtilizationInfo:
    """Тесты для метода returns_settings_utilization_info."""

    @pytest.mark.asyncio
    async def test_returns_settings_utilization_info(self, api, mock_api_request):
        """Тестирует метод returns_settings_utilization_info."""

        mock_response_data = {
            "min_price": {"amount": "50", "currency": "RUB"},
            "utilization_settings": {
                "utilization_price": {"amount": "100", "currency": "RUB"},
                "utilization_price_defects": {"amount": "0", "currency": "RUB"}
            }
        }
        mock_api_request.return_value = mock_response_data

        response = await api.returns_settings_utilization_info()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="returns/settings/utilization/info",
            payload={}
        )

        assert isinstance(response, ReturnsSettingsUtilizationInfoResponse)
        assert response.min_price.amount == "50"
        assert response.utilization_settings.utilization_price.amount == "100"
