import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSCreateDropOffTimeslotListRequest,
    WarehouseFBSCreateDropOffTimeslotListResponse,
)


class TestWarehouseFBSCreateDropOffTimeslotList:
    """Тесты для метода warehouse_fbs_create_drop_off_timeslot_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_create_drop_off_timeslot_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_create_drop_off_timeslot_list."""

        mock_api_request.return_value = {
            "timeslots": [
                {
                    "acceptance_end_time_local": "18:00",
                    "acceptance_start_time_local": "09:00",
                    "from": "10:00",
                    "id": 7,
                    "to": "12:00",
                }
            ]
        }

        request = WarehouseFBSCreateDropOffTimeslotListRequest(drop_off_point_id=123)

        response = await api.warehouse_fbs_create_drop_off_timeslot_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/drop-off/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSCreateDropOffTimeslotListResponse)
        assert response.timeslots[0].id == 7
        assert response.timeslots[0].from_ == "10:00"
        assert response.timeslots[0].to_ == "12:00"
