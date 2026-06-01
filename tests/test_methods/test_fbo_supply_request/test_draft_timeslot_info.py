import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftTimeslotInfoRequest,
    DraftTimeslotInfoResponse,
    DraftTimeslotInfoSelectedClusterWarehouse,
)


class TestDraftTimeslotInfo:
    """Тесты для метода draft_timeslot_info."""

    @pytest.mark.asyncio
    async def test_draft_timeslot_info(self, api, mock_api_request):
        """Тестирует метод draft_timeslot_info."""

        mock_api_request.return_value = {
            "error_reason": "",
            "result": {
                "drop_off_warehouse_timeslots": {
                    "current_time_in_timezone": "2026-06-01T12:00:00+03:00",
                    "warehouse_timezone": "Europe/Moscow",
                    "days": [
                        {
                            "date_in_timezone": "2026-06-02",
                            "timeslots": [
                                {
                                    "from_in_timezone": "2026-06-02T09:00:00+03:00",
                                    "to_in_timezone": "2026-06-02T12:00:00+03:00",
                                }
                            ],
                        }
                    ],
                },
                "requested_date_from": "2026-06-01",
                "requested_date_to": "2026-06-07",
            },
        }

        request = DraftTimeslotInfoRequest(
            draft_id=123456,
            supply_type=SupplyType.DIRECT,
            date_from="2026-06-01T00:00:00Z",
            date_to="2026-06-07T00:00:00Z",
            selected_cluster_warehouses=[
                DraftTimeslotInfoSelectedClusterWarehouse(
                    macrolocal_cluster_id=1, storage_warehouse_id=2
                )
            ],
        )

        response = await api.draft_timeslot_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="draft/timeslot/info",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftTimeslotInfoResponse)
        slot = response.result.drop_off_warehouse_timeslots.days[0].timeslots[0]
        assert slot.from_in_timezone == "2026-06-02T09:00:00+03:00"
