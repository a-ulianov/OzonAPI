import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderTimeslotGetRequest,
    SupplyOrderTimeslotGetResponse,
)


class TestSupplyOrderTimeslotGet:
    """Тесты для метода supply_order_timeslot_get."""

    @pytest.mark.asyncio
    async def test_supply_order_timeslot_get(self, api, mock_api_request):
        """Тестирует метод supply_order_timeslot_get."""

        mock_response_data = {
            "timeslots": [
                {"from": "2026-06-01T10:00:00Z", "to": "2026-06-01T12:00:00Z"},
                {"from": "2026-06-01T12:00:00Z", "to": "2026-06-01T14:00:00Z"},
            ],
            "timezone": "Europe/Moscow",
        }
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderTimeslotGetRequest(supply_order_id=1234567890)

        response = await api.supply_order_timeslot_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/timeslot/get",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderTimeslotGetResponse)
        assert len(response.timeslots) == 2
        assert response.timeslots[0].from_ is not None
        assert response.timeslots[0].to is not None
        assert response.timezone == "Europe/Moscow"
