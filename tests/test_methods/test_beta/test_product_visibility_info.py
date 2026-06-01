import pytest

from src.ozonapi.seller.schemas.beta import (
    ProductVisibilityInfoRequest,
    ProductVisibilityInfoResponse,
)


class TestProductVisibilityInfo:
    """Тесты для метода product_visibility_info."""

    @pytest.mark.asyncio
    async def test_product_visibility_info(self, api, mock_api_request):
        """Тестирует метод product_visibility_info."""

        mock_api_request.return_value = {
            "items": [{"showcases_visibility": "VISIBLE", "sku": 222}]
        }

        request = ProductVisibilityInfoRequest(skus=["222"])

        response = await api.product_visibility_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/visibility/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductVisibilityInfoResponse)
        assert response.items[0].sku == 222
        assert response.items[0].showcases_visibility == "VISIBLE"
