import pytest

from src.ozonapi.seller.schemas.products import ProductRelatedSkuGetRequest, ProductRelatedSkuGetResponse


class TestProductRelatedSkuGet:
    """Тесты для метода product_related_sku_get."""

    @pytest.mark.asyncio
    async def test_product_related_sku_get(self, api, mock_api_request):
        """Тестирует метод product_related_sku_get."""
        mock_response_data = {
            "items": [],
            "errors": []
        }
        mock_api_request.return_value = mock_response_data

        request = ProductRelatedSkuGetRequest(
            sku=[123456789, 987654321]
        )
        response = await api.product_related_sku_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/related-sku/get",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductRelatedSkuGetResponse)
        assert response.items == []
