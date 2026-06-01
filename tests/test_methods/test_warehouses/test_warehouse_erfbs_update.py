import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSOperationResponse,
    WarehouseERFBSUpdateRequest,
)


class TestWarehouseERFBSUpdate:
    """Тесты для метода warehouse_erfbs_update."""

    @pytest.mark.asyncio
    async def test_warehouse_erfbs_update(self, api, mock_api_request):
        """Тестирует метод warehouse_erfbs_update."""

        mock_api_request.return_value = {"operation_id": "op-erfbs-upd-1"}

        request = WarehouseERFBSUpdateRequest(
            warehouse_id=123,
            name="Новое имя",
            min_order_value=1000,
            timetable_warehouse={
                "working_days": [{"day": "FRIDAY", "from": "10:00", "to": "20:00"}],
            },
        )

        response = await api.warehouse_erfbs_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/update",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-erfbs-upd-1"
