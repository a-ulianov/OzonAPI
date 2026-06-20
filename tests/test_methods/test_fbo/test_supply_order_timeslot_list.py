import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderTimeslotListRequest,
    SupplyOrderTimeslotListResponse,
)


class TestSupplyOrderTimeslotList:
    """Тесты для метода supply_order_timeslot_list."""

    @pytest.mark.asyncio
    async def test_supply_order_timeslot_list(self, api, mock_api_request):
        """Тестирует метод supply_order_timeslot_list."""

        mock_response_data = {
            "limit_exceeded": {"changes_limit": 3},
            "timeslot_change_forbidden": {
                "error_reasons": ["INVALID_ORDER_STATE"],
            },
            "timeslots_info": {
                "limitations": {"changes_count": 1, "changes_limit": 3},
                "timeslots": [
                    {"from": "2026-06-01T10:00:00Z", "to": "2026-06-01T12:00:00Z"},
                    {"from": "2026-06-01T12:00:00Z", "to": "2026-06-01T14:00:00Z"},
                ],
                "timezone": {"iana_name": "Europe/Moscow", "offset": 10800},
            },
        }
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderTimeslotListRequest(order_id=1234567890)

        response = await api.supply_order_timeslot_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="supply-order/timeslot/list",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderTimeslotListResponse)
        assert response.limit_exceeded.changes_limit == 3
        assert response.timeslot_change_forbidden.error_reasons == ["INVALID_ORDER_STATE"]
        assert response.timeslots_info.limitations.changes_count == 1
        assert len(response.timeslots_info.timeslots) == 2
        assert response.timeslots_info.timeslots[0].from_ is not None
        assert response.timeslots_info.timeslots[0].to is not None
        assert response.timeslots_info.timezone.iana_name == "Europe/Moscow"
        assert response.timeslots_info.timezone.offset == 10800
