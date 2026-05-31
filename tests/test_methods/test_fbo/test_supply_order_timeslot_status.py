import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderTimeslotStatusRequest,
    SupplyOrderTimeslotStatusResponse,
)


class TestSupplyOrderTimeslotStatus:
    """Тесты для метода supply_order_timeslot_status."""

    @pytest.mark.asyncio
    async def test_supply_order_timeslot_status(self, api, mock_api_request):
        """Тестирует метод supply_order_timeslot_status."""

        mock_response_data = {"status": "STATUS_SUCCESS", "errors": []}
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderTimeslotStatusRequest(operation_id="operation-123")

        response = await api.supply_order_timeslot_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/timeslot/status",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderTimeslotStatusResponse)
        assert response.status == "STATUS_SUCCESS"
        assert response.errors == []
