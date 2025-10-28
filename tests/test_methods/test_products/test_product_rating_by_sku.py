import pytest

from src.ozonapi.seller.schemas.products import ProductRatingBySkuRequest, ProductRatingBySkuResponse


class TestProductRatingBySku:
    """Тесты для метода product_rating_by_sku."""

    @pytest.mark.asyncio
    async def test_product_rating_by_sku(self, api, mock_api_request):
        """Тестирует метод product_rating_by_sku."""
        mock_response_data = {
            "products": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductRatingBySkuRequest(
            skus=[179737222, 179737223]
        )
        response = await api.product_rating_by_sku(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/rating-by-sku",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductRatingBySkuResponse)
        assert response.products == []
