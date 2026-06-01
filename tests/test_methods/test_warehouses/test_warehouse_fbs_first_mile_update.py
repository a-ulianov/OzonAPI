import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSFirstMileUpdateRequest,
    WarehouseFBSFirstMileUpdateResponse,
)


class TestWarehouseFBSFirstMileUpdate:
    """Тесты для метода warehouse_fbs_first_mile_update."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_first_mile_update(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_first_mile_update."""

        mock_api_request.return_value = {"operation_id": "op-fm-1"}

        request = WarehouseFBSFirstMileUpdateRequest(
            warehouse_id=123, first_mile_type="PICK_UP", timeslot_id=5
        )

        response = await api.warehouse_fbs_first_mile_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/first-mile/update",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSFirstMileUpdateResponse)
        assert response.operation_id == "op-fm-1"
