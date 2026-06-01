import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionDiscountLevel,
    SellerActionsUpdateMultiLevelDiscountParameters,
    SellerActionsUpdateMultiLevelDiscountRequest,
    SellerActionsUpdateMultiLevelDiscountResponse,
)


class TestSellerActionsUpdateMultiLevelDiscount:
    """Тесты для метода seller_actions_update_multi_level_discount."""

    @pytest.mark.asyncio
    async def test_seller_actions_update_multi_level_discount(self, api, mock_api_request):
        """Тестирует метод seller_actions_update_multi_level_discount."""

        mock_api_request.return_value = {}

        request = SellerActionsUpdateMultiLevelDiscountRequest(
            action_id=123456,
            action_parameters=SellerActionsUpdateMultiLevelDiscountParameters(
                title="Чем больше, тем дешевле",
                date_start="2026-07-01T00:00:00Z",
                date_end="2026-08-15T23:59:59Z",
                is_legal_entities_segment=False,
                discount_levels=[
                    SellerActionDiscountLevel(order_amount=3000.0, discount_value=5.0),
                ],
            ),
        )

        response = await api.seller_actions_update_multi_level_discount(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/multi-level-discount",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsUpdateMultiLevelDiscountResponse)
