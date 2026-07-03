import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoStocksByWarehouseFBORequest,
    ProductInfoStocksByWarehouseFBOResponse,
)


class TestProductInfoStocksByWarehouseFBO:
    """Тесты для метода product_info_stocks_by_warehouse_fbo (API v1)."""

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbo(self, api, mock_api_request):
        """Тестирует метод product_info_stocks_by_warehouse_fbo."""
        mock_api_request.return_value = {
            "products": [
                {
                    "sku": 9876543210,
                    "offer_id": "OFFER-1",
                    "product_id": 123456,
                    "present": 50,
                    "reserved": 5,
                    "warehouse_id": 15588127982000,
                }
            ],
            "cursor": "next_cursor",
            "has_next": True,
        }

        request = ProductInfoStocksByWarehouseFBORequest(skus=["9876543210"])
        response = await api.product_info_stocks_by_warehouse_fbo(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbo",
            payload=request.model_dump(),
        )
        assert isinstance(response, ProductInfoStocksByWarehouseFBOResponse)
        assert response.has_next is True
        assert response.cursor == "next_cursor"
        assert len(response.products) == 1
        item = response.products[0]
        assert item.sku == 9876543210
        assert item.offer_id == "OFFER-1"
        assert item.product_id == 123456
        assert item.present == 50
        assert item.reserved == 5
        assert item.warehouse_id == 15588127982000

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbo_empty(self, api, mock_api_request):
        """Пустой ответ корректно разбирается."""
        mock_api_request.return_value = {"products": [], "cursor": "", "has_next": False}

        request = ProductInfoStocksByWarehouseFBORequest(offer_ids=["OFFER-1"])
        response = await api.product_info_stocks_by_warehouse_fbo(request)

        assert isinstance(response, ProductInfoStocksByWarehouseFBOResponse)
        assert response.products == []
        assert response.has_next is False
