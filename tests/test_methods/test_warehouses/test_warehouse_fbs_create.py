import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSCreateRequest,
    WarehouseFBSCreateResponse,
)


class TestWarehouseFBSCreate:
    """Тесты для метода warehouse_fbs_create."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_create(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_create."""

        mock_api_request.return_value = {"operation_id": "op-create-1"}

        request = WarehouseFBSCreateRequest(
            name="Склад",
            phone="+70000000000",
            first_mile_type="DROP_OFF",
            working_days=["MONDAY", "TUESDAY"],
            options={"is_auto_assembly": True},
        )

        response = await api.warehouse_fbs_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSCreateResponse)
        assert response.operation_id == "op-create-1"
