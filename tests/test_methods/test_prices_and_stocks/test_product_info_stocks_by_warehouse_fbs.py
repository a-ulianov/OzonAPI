import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoStocksByWarehouseFBSRequest,
    ProductInfoStocksByWarehouseFBSResponse,
)


class TestProductInfoStocksByWarehouseFBS:
    """Тесты для метода product_info_stocks_by_warehouse_fbs (API v2)."""

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbs(self, api, mock_api_request):
        """Тестирует метод product_info_stocks_by_warehouse_fbs."""
        mock_api_request.return_value = {
            "products": [
                {
                    "sku": 9876543210,
                    "offer_id": "OFFER-1",
                    "product_id": 123456,
                    "present": 50,
                    "reserved": 5,
                    "free_stock": 45,
                    "warehouse_id": 15588127982000,
                    "warehouse_name": "Основной склад FBS",
                }
            ],
            "cursor": "next_cursor",
            "has_next": True,
        }

        request = ProductInfoStocksByWarehouseFBSRequest(sku=["9876543210"])
        response = await api.product_info_stocks_by_warehouse_fbs(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="product/info/stocks-by-warehouse/fbs",
            payload=request.model_dump(),
        )
        assert isinstance(response, ProductInfoStocksByWarehouseFBSResponse)
        assert response.has_next is True
        assert response.cursor == "next_cursor"
        assert len(response.products) == 1
        item = response.products[0]
        assert item.sku == 9876543210
        assert item.offer_id == "OFFER-1"
        assert item.free_stock == 45
        assert item.reserved == 5
        assert item.warehouse_name == "Основной склад FBS"

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbs_empty(self, api, mock_api_request):
        """Пустой ответ корректно разбирается."""
        mock_api_request.return_value = {"products": [], "cursor": "", "has_next": False}

        request = ProductInfoStocksByWarehouseFBSRequest(offer_id=["OFFER-1"])
        response = await api.product_info_stocks_by_warehouse_fbs(request)

        assert isinstance(response, ProductInfoStocksByWarehouseFBSResponse)
        assert response.products == []
        assert response.has_next is False
