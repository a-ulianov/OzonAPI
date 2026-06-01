import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsProductsDeleteRequest,
    SellerActionsProductsDeleteResponse,
)


class TestSellerActionsProductsDelete:
    """Тесты для метода seller_actions_products_delete."""

    @pytest.mark.asyncio
    async def test_seller_actions_products_delete(self, api, mock_api_request):
        """Тестирует метод seller_actions_products_delete."""

        mock_api_request.return_value = {}

        request = SellerActionsProductsDeleteRequest(
            action_id=123456, skus=["1234567890"]
        )

        response = await api.seller_actions_products_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/delete",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsProductsDeleteResponse)
