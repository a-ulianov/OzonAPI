import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsCreateVoucherParameter,
    SellerActionsCreateVoucherRequest,
    SellerActionsCreateVoucherResponse,
)


class TestSellerActionsCreateVoucher:
    """Тесты для метода seller_actions_create_voucher."""

    @pytest.mark.asyncio
    async def test_seller_actions_create_voucher(self, api, mock_api_request):
        """Тестирует метод seller_actions_create_voucher."""

        mock_api_request.return_value = {"action_id": 123456}

        request = SellerActionsCreateVoucherRequest(
            title="Промокод на лето",
            date_start="2026-07-01T00:00:00Z",
            date_end="2026-07-31T23:59:59Z",
            discount_type="PERCENT",
            discount_value=10.0,
            voucher_parameters=SellerActionsCreateVoucherParameter(
                type="UNIQUE", count_codes=100, is_private=True
            ),
        )

        response = await api.seller_actions_create_voucher(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/voucher",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsCreateVoucherResponse)
        assert response.action_id == 123456
