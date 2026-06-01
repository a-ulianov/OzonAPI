import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseWithInvalidProductsResponse,
)


class TestWarehouseWarehousesWithInvalidProducts:
    """Тесты для метода warehouse_warehouses_with_invalid_products."""

    @pytest.mark.asyncio
    async def test_warehouse_warehouses_with_invalid_products(self, api, mock_api_request):
        """Тестирует метод warehouse_warehouses_with_invalid_products."""

        mock_api_request.return_value = {"warehouse_ids": ["1", "2"]}

        response = await api.warehouse_warehouses_with_invalid_products()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/warehouses-with-invalid-products",
            payload={}
        )

        assert isinstance(response, WarehouseWithInvalidProductsResponse)
        assert response.warehouse_ids == ["1", "2"]
