import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoStocksByWarehouseFBSV1Request,
    ProductInfoStocksByWarehouseFBSV1Response,
)


class TestProductInfoStocksByWarehouseFBSV1:
    """Тесты для метода product_info_stocks_by_warehouse_fbs_v1."""

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbs_v1(self, api, mock_api_request):
        """Тестирует метод product_info_stocks_by_warehouse_fbs_v1."""

        mock_api_request.return_value = {
            "result": [
                {
                    "sku": 222,
                    "offer_id": "art-1",
                    "present": 10,
                    "product_id": 111,
                    "reserved": 2,
                    "warehouse_id": 333,
                    "warehouse_name": "Склад",
                }
            ]
        }

        request = ProductInfoStocksByWarehouseFBSV1Request(sku=["222"])

        response = await api.product_info_stocks_by_warehouse_fbs_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbs",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductInfoStocksByWarehouseFBSV1Response)
        assert response.result[0].sku == 222
        assert response.result[0].warehouse_name == "Склад"
