import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseListV1Request,
    WarehouseListV1Response,
)


class TestWarehouseListV1:
    """Тесты для метода warehouse_list_v1."""

    @pytest.mark.asyncio
    async def test_warehouse_list_v1(self, api, mock_api_request):
        """Тестирует метод warehouse_list_v1."""

        mock_api_request.return_value = {
            "result": [{"warehouse_id": 1, "name": "Склад", "status": "created"}]
        }

        request = WarehouseListV1Request(limit=10, offset=0)

        response = await api.warehouse_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseListV1Response)
        assert response.result[0].warehouse_id == 1
