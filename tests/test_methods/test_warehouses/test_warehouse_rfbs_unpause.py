import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSOperationResponse,
    WarehouseRfbsUnpauseRequest,
)


class TestWarehouseRfbsUnpause:
    """Тесты для метода warehouse_rfbs_unpause."""

    @pytest.mark.asyncio
    async def test_warehouse_rfbs_unpause(self, api, mock_api_request):
        """Тестирует метод warehouse_rfbs_unpause."""

        mock_api_request.return_value = {"operation_id": "op-unpause-1"}

        request = WarehouseRfbsUnpauseRequest(warehouse_id=123)

        response = await api.warehouse_rfbs_unpause(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/rfbs/unpause",
            payload=request.model_dump()
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-unpause-1"
