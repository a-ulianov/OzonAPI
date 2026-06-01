import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsUpdateDiscountParameters,
    SellerActionsUpdateDiscountRequest,
    SellerActionsUpdateDiscountResponse,
)


class TestSellerActionsUpdateDiscount:
    """Тесты для метода seller_actions_update_discount."""

    @pytest.mark.asyncio
    async def test_seller_actions_update_discount(self, api, mock_api_request):
        """Тестирует метод seller_actions_update_discount."""

        mock_api_request.return_value = {}

        request = SellerActionsUpdateDiscountRequest(
            action_id=123456,
            action_parameters=SellerActionsUpdateDiscountParameters(
                title="Летняя распродажа",
                date_start="2026-07-01T00:00:00Z",
                date_end="2026-08-15T23:59:59Z",
            ),
        )

        response = await api.seller_actions_update_discount(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/discount",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsUpdateDiscountResponse)
