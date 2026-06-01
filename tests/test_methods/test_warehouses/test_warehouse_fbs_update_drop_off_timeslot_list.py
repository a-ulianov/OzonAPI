import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSUpdateDropOffTimeslotListRequest,
    WarehouseFBSUpdateDropOffTimeslotListResponse,
)


class TestWarehouseFBSUpdateDropOffTimeslotList:
    """Тесты для метода warehouse_fbs_update_drop_off_timeslot_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_update_drop_off_timeslot_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_update_drop_off_timeslot_list."""

        mock_api_request.return_value = {
            "timeslots": [
                {
                    "acceptance_end_time_local": "20:00",
                    "acceptance_start_time_local": "08:00",
                    "from": "11:00",
                    "id": 9,
                    "to": "13:00",
                }
            ]
        }

        request = WarehouseFBSUpdateDropOffTimeslotListRequest(
            drop_off_point_id=123, warehouse_id=456
        )

        response = await api.warehouse_fbs_update_drop_off_timeslot_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/drop-off/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSUpdateDropOffTimeslotListResponse)
        assert response.timeslots[0].id == 9
        assert response.timeslots[0].from_ == "11:00"
