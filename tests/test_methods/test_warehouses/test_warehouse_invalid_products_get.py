import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseInvalidProductsGetRequest,
    WarehouseInvalidProductsGetResponse,
)


class TestWarehouseInvalidProductsGet:
    """Тесты для метода warehouse_invalid_products_get."""

    @pytest.mark.asyncio
    async def test_warehouse_invalid_products_get(self, api, mock_api_request):
        """Тестирует метод warehouse_invalid_products_get."""

        mock_api_request.return_value = {
            "has_next": False,
            "last_id": 0,
            "warehouse_id": 123,
            "validation_results": [
                {
                    "item": {
                        "sku": 10,
                        "weight_g": 500.0,
                        "size": {"height_mm": 10, "length_mm": 20, "width_mm": 30},
                    },
                    "state": "INVALID",
                    "validation_errors": [
                        {
                            "characteristic": "WEIGHT",
                            "restriction_price": {"currency": "RUB", "value": 100.0},
                            "type": "RESTRICTION",
                        }
                    ],
                }
            ],
        }

        request = WarehouseInvalidProductsGetRequest(warehouse_id=123)

        response = await api.warehouse_invalid_products_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/invalid-products/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseInvalidProductsGetResponse)
        assert response.validation_results[0].item.sku == 10
