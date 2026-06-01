import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseArchiveRequest,
    WarehouseArchiveResponse,
)


class TestWarehouseArchive:
    """Тесты для метода warehouse_archive."""

    @pytest.mark.asyncio
    async def test_warehouse_archive(self, api, mock_api_request):
        """Тестирует метод warehouse_archive."""

        mock_api_request.return_value = {"operation_id": "op-arch-1"}

        request = WarehouseArchiveRequest(warehouse_id=123, reason="closed")

        response = await api.warehouse_archive(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/archive",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseArchiveResponse)
        assert response.operation_id == "op-arch-1"
