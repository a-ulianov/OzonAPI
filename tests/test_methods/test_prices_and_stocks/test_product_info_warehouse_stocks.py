import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoWarehouseStocksRequest,
    ProductInfoWarehouseStocksResponse,
)


class TestProductInfoWarehouseStocks:
    """Тесты для метода product_info_warehouse_stocks."""

    @pytest.mark.asyncio
    async def test_product_info_warehouse_stocks(self, api, mock_api_request):
        """Тестирует метод product_info_warehouse_stocks."""

        mock_api_request.return_value = {
            "cursor": "next",
            "has_next": True,
            "stocks": [
                {
                    "free_stock": 5,
                    "offer_id": "art-1",
                    "present": 10,
                    "product_id": 111,
                    "reserved": 2,
                    "sku": 222,
                    "updated_at": "2026-06-01T10:00:00Z",
                    "warehouse_id": 333,
                }
            ],
        }

        request = ProductInfoWarehouseStocksRequest(warehouse_id=333, limit=100)

        response = await api.product_info_warehouse_stocks(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/warehouse/stocks",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductInfoWarehouseStocksResponse)
        assert response.has_next is True
        assert response.stocks[0].sku == 222
        assert response.stocks[0].free_stock == 5
