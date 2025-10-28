import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import ProductInfoPricesRequest, ProductInfoPricesResponse


class TestProductInfoPrices:
    """Тесты для метода product_info_prices."""

    @pytest.mark.asyncio
    async def test_product_info_prices(self, api, mock_api_request):
        """Тестирует метод product_info_prices."""
        mock_response_data = {
            "items": [],
            "cursor": "test_cursor",
            "total": 0
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoPricesRequest()
        response = await api.product_info_prices(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v5",
            endpoint="product/info/prices",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductInfoPricesResponse)
        assert response.cursor == "test_cursor"
