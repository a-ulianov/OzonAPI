import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsChangeActivityRequest,
    SellerActionsChangeActivityResponse,
)


class TestSellerActionsChangeActivity:
    """Тесты для метода seller_actions_change_activity."""

    @pytest.mark.asyncio
    async def test_seller_actions_change_activity(self, api, mock_api_request):
        """Тестирует метод seller_actions_change_activity."""

        mock_api_request.return_value = {}

        request = SellerActionsChangeActivityRequest(action_id=123456, is_turn_on=True)

        response = await api.seller_actions_change_activity(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/change-activity",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsChangeActivityResponse)
