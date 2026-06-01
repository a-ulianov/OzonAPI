import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSOperationResponse,
    WarehouseRfbsPauseRequest,
)


class TestWarehouseRfbsPause:
    """Тесты для метода warehouse_rfbs_pause."""

    @pytest.mark.asyncio
    async def test_warehouse_rfbs_pause(self, api, mock_api_request):
        """Тестирует метод warehouse_rfbs_pause."""

        mock_api_request.return_value = {"operation_id": "op-pause-1"}

        request = WarehouseRfbsPauseRequest(warehouse_id=123)

        response = await api.warehouse_rfbs_pause(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/rfbs/pause",
            payload=request.model_dump()
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-pause-1"
