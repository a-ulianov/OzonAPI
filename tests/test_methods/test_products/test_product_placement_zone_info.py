import pytest

from src.ozonapi.seller.schemas.products import (
    ProductPlacementZoneInfoRequest,
    ProductPlacementZoneInfoResponse,
)


class TestProductPlacementZoneInfo:
    """Тесты для метода product_placement_zone_info."""

    @pytest.mark.asyncio
    async def test_product_placement_zone_info(self, api, mock_api_request):
        """Тестирует метод product_placement_zone_info."""
        mock_response_data = {
            "products_placement": [
                {"sku": 987654321, "placement_zone": "PRODUCTS"},
                {"sku": 123456789, "placement_zone": "OVERSIZE"},
            ],
        }
        mock_api_request.return_value = mock_response_data

        request = ProductPlacementZoneInfoRequest(skus=["987654321", "123456789"])
        response = await api.product_placement_zone_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/placement-zone/info",
            payload=request.model_dump(),
        )
        assert isinstance(response, ProductPlacementZoneInfoResponse)
        assert len(response.products_placement) == 2
        assert response.products_placement[0].sku == 987654321
        assert response.products_placement[0].placement_zone == "PRODUCTS"
        assert response.products_placement[1].placement_zone == "OVERSIZE"
