import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSPickUpCourierCreateRequest,
    WarehouseFBSPickUpCourierCreateResponse,
)


class TestWarehouseFBSPickUpCourierCreate:
    """Тесты для метода warehouse_fbs_pickup_courier_create."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_pickup_courier_create(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_pickup_courier_create."""

        mock_api_request.return_value = {}

        request = WarehouseFBSPickUpCourierCreateRequest(warehouse_id=123)

        response = await api.warehouse_fbs_pickup_courier_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/courier/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSPickUpCourierCreateResponse)
