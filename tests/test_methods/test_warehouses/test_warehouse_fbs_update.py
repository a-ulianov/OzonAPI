import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSUpdateRequest,
    WarehouseFBSUpdateResponse,
)


class TestWarehouseFBSUpdate:
    """Тесты для метода warehouse_fbs_update."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_update(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_update."""

        mock_api_request.return_value = {"operation_id": "op-update-1"}

        request = WarehouseFBSUpdateRequest(warehouse_id=123, name="Новое имя")

        response = await api.warehouse_fbs_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSUpdateResponse)
        assert response.operation_id == "op-update-1"
