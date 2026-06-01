import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsUpdateVoucherParameters,
    SellerActionsUpdateVoucherRequest,
    SellerActionsUpdateVoucherResponse,
)


class TestSellerActionsUpdateVoucher:
    """Тесты для метода seller_actions_update_voucher."""

    @pytest.mark.asyncio
    async def test_seller_actions_update_voucher(self, api, mock_api_request):
        """Тестирует метод seller_actions_update_voucher."""

        mock_api_request.return_value = {}

        request = SellerActionsUpdateVoucherRequest(
            action_id=123456,
            action_parameters=SellerActionsUpdateVoucherParameters(
                title="Промокод на лето",
                date_start="2026-07-01T00:00:00Z",
                date_end="2026-08-15T23:59:59Z",
                discount_value=15.0,
                budget=100000,
            ),
        )

        response = await api.seller_actions_update_voucher(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/voucher",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsUpdateVoucherResponse)
