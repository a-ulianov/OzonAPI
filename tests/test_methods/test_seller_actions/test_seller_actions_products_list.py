import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsProductsListRequest,
    SellerActionsProductsListResponse,
)


class TestSellerActionsProductsList:
    """Тесты для метода seller_actions_products_list."""

    @pytest.mark.asyncio
    async def test_seller_actions_products_list(self, api, mock_api_request):
        """Тестирует метод seller_actions_products_list."""

        mock_api_request.return_value = {
            "cursor": "",
            "has_next": False,
            "products": [
                {
                    "product_id": 313455276,
                    "offer_id": "ART-1",
                    "action_price": 900.0,
                    "is_active": True,
                    "currency": "RUB",
                    "sku": [1807538302],
                }
            ],
        }

        request = SellerActionsProductsListRequest(action_id=123456, limit=100)

        response = await api.seller_actions_products_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/list",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsProductsListResponse)
        assert response.has_next is False
        assert response.products[0].is_active is True
