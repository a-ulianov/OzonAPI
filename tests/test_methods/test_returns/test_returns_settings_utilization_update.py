import pytest

from src.ozonapi.seller.schemas.returns import (
    ReturnsSettingsUtilizationUpdateRequest,
    ReturnsSettingsUtilizationUpdateResponse,
)
from src.ozonapi.seller.schemas.returns.v1__returns_settings_utilization_update import (
    ReturnsSettingsUtilizationUpdatePrice,
)


class TestReturnsSettingsUtilizationUpdate:
    """Тесты для метода returns_settings_utilization_update."""

    @pytest.mark.asyncio
    async def test_returns_settings_utilization_update(self, api, mock_api_request):
        """Тестирует метод returns_settings_utilization_update."""

        mock_response_data = {}
        mock_api_request.return_value = mock_response_data

        request = ReturnsSettingsUtilizationUpdateRequest(
            utilization_price=ReturnsSettingsUtilizationUpdatePrice(enabled=True, value=100),
            utilization_price_defects=ReturnsSettingsUtilizationUpdatePrice(enabled=False)
        )

        response = await api.returns_settings_utilization_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="returns/settings/utilization/update",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsSettingsUtilizationUpdateResponse)
