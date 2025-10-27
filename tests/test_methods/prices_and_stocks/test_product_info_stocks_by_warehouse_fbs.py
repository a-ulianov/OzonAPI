import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import ProductInfoStocksByWarehouseFBSRequest, \
    ProductInfoStocksByWarehouseFBSResponse


class TestProductInfoStocksByWarehouseFBS:
    """Тесты для метода product_info_stocks_by_warehouse_fbs."""

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbs(self, api, mock_api_request):
        """Тестирует метод product_info_stocks_by_warehouse_fbs."""
        mock_response_data = {
            "result": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoStocksByWarehouseFBSRequest(
            sku=[9876543210]
        )
        response = await api.product_info_stocks_by_warehouse_fbs(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbs",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoStocksByWarehouseFBSResponse)
        assert response.result == []
