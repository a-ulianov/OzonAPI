import pytest

from src.ozonapi.seller.schemas.beta import (
    ProductStairwayDiscountByQuantityGetRequest,
    ProductStairwayDiscountByQuantityGetResponse,
)


class TestProductStairwayDiscountByQuantityGet:
    """Тесты для метода product_stairway_discount_by_quantity_get."""

    @pytest.mark.asyncio
    async def test_product_stairway_discount_by_quantity_get(self, api, mock_api_request):
        """Тестирует метод product_stairway_discount_by_quantity_get."""

        mock_api_request.return_value = {
            "stairways": [
                {
                    "enabled": True,
                    "sku": 123,
                    "stairway": {"steps": [{"discount": 5, "quantity": 2, "step": 1}]},
                    "status": "SUCCESS",
                }
            ]
        }

        request = ProductStairwayDiscountByQuantityGetRequest(skus=["123"])

        response = await api.product_stairway_discount_by_quantity_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/stairway-discount/by-quantity/get",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductStairwayDiscountByQuantityGetResponse)
        assert response.stairways[0].sku == 123
        assert response.stairways[0].stairway.steps[0].discount == 5
        assert response.stairways[0].status == "SUCCESS"
