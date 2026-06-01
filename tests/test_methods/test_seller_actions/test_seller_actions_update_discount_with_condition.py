import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsUpdateDiscountWithConditionParameters,
    SellerActionsUpdateDiscountWithConditionRequest,
    SellerActionsUpdateDiscountWithConditionResponse,
)


class TestSellerActionsUpdateDiscountWithCondition:
    """Тесты для метода seller_actions_update_discount_with_condition."""

    @pytest.mark.asyncio
    async def test_seller_actions_update_discount_with_condition(self, api, mock_api_request):
        """Тестирует метод seller_actions_update_discount_with_condition."""

        mock_api_request.return_value = {}

        request = SellerActionsUpdateDiscountWithConditionRequest(
            action_id=123456,
            action_parameters=SellerActionsUpdateDiscountWithConditionParameters(
                title="Скидка от 5000",
                date_start="2026-07-01T00:00:00Z",
                date_end="2026-08-15T23:59:59Z",
                discount_value=20.0,
                min_order_amount=5000.0,
            ),
        )

        response = await api.seller_actions_update_discount_with_condition(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/discount-with-condition",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsUpdateDiscountWithConditionResponse)
