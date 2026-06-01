import pytest

from src.ozonapi.seller.schemas.beta import (
    ProductStairwayDiscountByQuantitySetRequest,
    ProductStairwayDiscountByQuantitySetResponse,
)


class TestProductStairwayDiscountByQuantitySet:
    """Тесты для метода product_stairway_discount_by_quantity_set."""

    @pytest.mark.asyncio
    async def test_product_stairway_discount_by_quantity_set(self, api, mock_api_request):
        """Тестирует метод product_stairway_discount_by_quantity_set."""

        mock_api_request.return_value = {"accepted": True, "errors": [], "warnings": []}

        request = ProductStairwayDiscountByQuantitySetRequest(
            stairways=[
                {
                    "enabled": True,
                    "sku": 123,
                    "stairway": {"steps": [{"discount": 5, "quantity": 2, "step": 1}]},
                }
            ],
            suppress_warnings=False,
        )

        response = await api.product_stairway_discount_by_quantity_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/stairway-discount/by-quantity/set",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductStairwayDiscountByQuantitySetResponse)
        assert response.accepted is True
