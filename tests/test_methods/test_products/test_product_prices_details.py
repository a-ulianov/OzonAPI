import pytest

from src.ozonapi.seller.schemas.products import (
    ProductPricesDetailsRequest,
    ProductPricesDetailsResponse,
)


class TestProductPricesDetails:
    """Тесты для метода product_prices_details."""

    @pytest.mark.asyncio
    async def test_product_prices_details(self, api, mock_api_request):
        """Тестирует метод product_prices_details."""

        mock_api_request.return_value = {
            "prices": [
                {
                    "sku": 1234567890,
                    "offer_id": "ART-1",
                    "discount_percent": 10.0,
                    "price": {"amount": "1000.00", "currency": "RUB"},
                    "customer_price": {"amount": "900.00", "currency": "RUB"},
                    "price_indexes": [
                        {
                            "external_index_data": {
                                "min_price": {"amount": "950.00", "currency": "RUB"},
                                "price_index": 1.05,
                                "url": "https://example.com",
                            }
                        }
                    ],
                }
            ]
        }

        request = ProductPricesDetailsRequest(skus=["1234567890"])

        response = await api.product_prices_details(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/prices/details",
            payload=request.model_dump(),
        )

        assert isinstance(response, ProductPricesDetailsResponse)
        price = response.prices[0]
        assert price.sku == 1234567890
        assert price.price.amount == "1000.00"
        assert price.price_indexes[0].external_index_data.price_index == 1.05
