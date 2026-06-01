import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSUpdatePickUpTimeslotListRequest,
    WarehouseFBSUpdatePickUpTimeslotListResponse,
)


class TestWarehouseFBSUpdatePickUpTimeslotList:
    """Тесты для метода warehouse_fbs_update_pick_up_timeslot_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_update_pick_up_timeslot_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_update_pick_up_timeslot_list."""

        mock_api_request.return_value = {
            "timeslots": [{"from": "10:00", "id": 2, "to": "19:00"}],
        }

        request = WarehouseFBSUpdatePickUpTimeslotListRequest(warehouse_id=123)

        response = await api.warehouse_fbs_update_pick_up_timeslot_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/pick-up/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSUpdatePickUpTimeslotListResponse)
        assert response.timeslots[0].id == 2
        assert response.timeslots[0].to_ == "19:00"
