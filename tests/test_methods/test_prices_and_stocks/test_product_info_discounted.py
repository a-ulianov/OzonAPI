import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoDiscountedRequest,
    ProductInfoDiscountedResponse,
)


class TestProductInfoDiscounted:
    """Тесты для метода product_info_discounted."""

    @pytest.mark.asyncio
    async def test_product_info_discounted(self, api, mock_api_request):
        """Тестирует метод product_info_discounted."""
        mock_response_data = {
            "items": [
                {
                    "comment_reason_damaged": "",
                    "condition": "used",
                    "condition_estimation": "4",
                    "defects": "",
                    "discounted_sku": 635548518,
                    "mechanical_damage": "",
                    "package_damage": "",
                    "packaging_violation": "",
                    "reason_damaged": "",
                    "repair": "",
                    "shortage": "",
                    "sku": 318096811,
                    "warranty_type": ""
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ProductInfoDiscountedRequest(discounted_skus=["635548518"])
        response = await api.product_info_discounted(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/discounted",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductInfoDiscountedResponse)
        assert len(response.items) == 1
        assert response.items[0].discounted_sku == 635548518
        assert response.items[0].sku == 318096811
        assert response.items[0].condition_estimation == "4"
