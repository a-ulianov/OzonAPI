import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsCreateDiscountRequest,
    SellerActionsCreateDiscountResponse,
)


class TestSellerActionsCreateDiscount:
    """Тесты для метода seller_actions_create_discount."""

    @pytest.mark.asyncio
    async def test_seller_actions_create_discount(self, api, mock_api_request):
        """Тестирует метод seller_actions_create_discount."""

        mock_api_request.return_value = {"action_id": 123456}

        request = SellerActionsCreateDiscountRequest(
            title="Летняя распродажа",
            date_start="2026-07-01T00:00:00Z",
            date_end="2026-07-31T23:59:59Z",
            min_action_percent=10.0,
        )

        response = await api.seller_actions_create_discount(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/discount",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsCreateDiscountResponse)
        assert response.action_id == 123456
