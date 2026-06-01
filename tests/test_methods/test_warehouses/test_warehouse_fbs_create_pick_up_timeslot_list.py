import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSCreatePickUpTimeslotListRequest,
    WarehouseFBSCreatePickUpTimeslotListResponse,
)


class TestWarehouseFBSCreatePickUpTimeslotList:
    """Тесты для метода warehouse_fbs_create_pick_up_timeslot_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_create_pick_up_timeslot_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_create_pick_up_timeslot_list."""

        mock_api_request.return_value = {
            "is_pickup_supported": True,
            "timeslots": [{"from": "09:00", "id": 1, "to": "18:00"}],
        }

        request = WarehouseFBSCreatePickUpTimeslotListRequest(
            address_coordinates={"latitude": 55.7, "longitude": 37.6}, is_kgt=False
        )

        response = await api.warehouse_fbs_create_pick_up_timeslot_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/pick-up/timeslot/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSCreatePickUpTimeslotListResponse)
        assert response.is_pickup_supported is True
        assert response.timeslots[0].from_ == "09:00"
