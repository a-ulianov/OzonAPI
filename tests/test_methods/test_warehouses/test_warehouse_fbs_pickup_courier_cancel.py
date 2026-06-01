import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSPickUpCourierCancelRequest,
    WarehouseFBSPickUpCourierCancelResponse,
)


class TestWarehouseFBSPickUpCourierCancel:
    """Тесты для метода warehouse_fbs_pickup_courier_cancel."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_pickup_courier_cancel(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_pickup_courier_cancel."""

        mock_api_request.return_value = {}

        request = WarehouseFBSPickUpCourierCancelRequest(warehouse_id=123)

        response = await api.warehouse_fbs_pickup_courier_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/courier/cancel",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSPickUpCourierCancelResponse)
