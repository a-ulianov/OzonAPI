import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import ProductInfoStocksRequest, ProductInfoStocksResponse


class TestProductInfoStocks:
    """Тесты для метода product_info_stocks."""

    @pytest.mark.asyncio
    async def test_product_info_stocks(self, api, mock_api_request):
        """Тестирует метод product_info_stocks."""
        mock_response_data = {
            "items": [],
            "cursor": "test_cursor",
            "total": 0
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoStocksRequest()
        response = await api.product_info_stocks(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/stocks",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductInfoStocksResponse)
        assert response.cursor == "test_cursor"
