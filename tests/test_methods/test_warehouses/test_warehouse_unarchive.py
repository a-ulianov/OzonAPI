import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseUnarchiveRequest,
    WarehouseUnarchiveResponse,
)


class TestWarehouseUnarchive:
    """Тесты для метода warehouse_unarchive."""

    @pytest.mark.asyncio
    async def test_warehouse_unarchive(self, api, mock_api_request):
        """Тестирует метод warehouse_unarchive."""

        mock_api_request.return_value = {"operation_id": "op-unarch-1"}

        request = WarehouseUnarchiveRequest(warehouse_id=123)

        response = await api.warehouse_unarchive(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/unarchive",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseUnarchiveResponse)
        assert response.operation_id == "op-unarch-1"
