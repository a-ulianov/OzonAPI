import pytest

from src.ozonapi.seller.schemas.beta import (
    ProductVisibilitySetRequest,
    ProductVisibilitySetResponse,
)


class TestProductVisibilitySet:
    """Тесты для метода product_visibility_set."""

    @pytest.mark.asyncio
    async def test_product_visibility_set(self, api, mock_api_request):
        """Тестирует метод product_visibility_set."""

        mock_api_request.return_value = {
            "items": [
                {
                    "sku": 222,
                    "select_permission": "ALLOWED",
                    "seller_item_placement": "OZON_SELECT",
                    "seller_item_placement_list": ["OZON", "SELECT"],
                    "showcases_visibility": "VISIBLE",
                    "showcases_visibility_list": ["OZON"],
                    "warnings": [],
                }
            ],
            "items_errors": [],
        }

        request = ProductVisibilitySetRequest(
            item_placement=[{"placement": "OZON_SELECT", "sku": 222}]
        )

        response = await api.product_visibility_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/visibility/set",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductVisibilitySetResponse)
        assert response.items[0].sku == 222
        assert response.items[0].seller_item_placement == "OZON_SELECT"
