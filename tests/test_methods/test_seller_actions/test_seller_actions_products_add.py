import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsProductsAddProduct,
    SellerActionsProductsAddRequest,
    SellerActionsProductsAddResponse,
)


class TestSellerActionsProductsAdd:
    """Тесты для метода seller_actions_products_add."""

    @pytest.mark.asyncio
    async def test_seller_actions_products_add(self, api, mock_api_request):
        """Тестирует метод seller_actions_products_add."""

        mock_api_request.return_value = {}

        request = SellerActionsProductsAddRequest(
            action_id=123456,
            products=[
                SellerActionsProductsAddProduct(
                    sku=1234567890, discount_percent=10.0, currency="RUB"
                )
            ],
        )

        response = await api.seller_actions_products_add(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/add",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsProductsAddResponse)
