import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceProductsBuyoutRequest,
    FinanceProductsBuyoutResponse,
)


class TestFinanceProductsBuyout:
    """Тесты для метода finance_products_buyout."""

    @pytest.mark.asyncio
    async def test_finance_products_buyout(self, api, mock_api_request):
        """Тестирует метод finance_products_buyout."""

        mock_api_request.return_value = {
            "products": [
                {
                    "amount": 500.0,
                    "buyout_price": 600.0,
                    "name": "Товар",
                    "offer_id": "art-5",
                    "posting_number": "0003-1",
                    "quantity": 1,
                    "sku": 555,
                    "vat_percent": 20,
                }
            ]
        }

        request = FinanceProductsBuyoutRequest(
            date_from="2026-04-01", date_to="2026-04-30"
        )

        response = await api.finance_products_buyout(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/products/buyout",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceProductsBuyoutResponse)
        assert response.products[0].sku == 555
        assert response.products[0].buyout_price == 600.0
