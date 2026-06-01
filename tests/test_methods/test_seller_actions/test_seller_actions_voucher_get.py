import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsVoucherGetRequest,
    SellerActionsVoucherGetResponse,
)


class TestSellerActionsVoucherGet:
    """Тесты для метода seller_actions_voucher_get."""

    @pytest.mark.asyncio
    async def test_seller_actions_voucher_get(self, api, mock_api_request):
        """Тестирует метод seller_actions_voucher_get."""

        mock_api_request.return_value = {
            "file": "https://cdn.ozon.ru/vouchers/123456.csv"
        }

        request = SellerActionsVoucherGetRequest(action_id=123456)

        response = await api.seller_actions_voucher_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/voucher/get",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsVoucherGetResponse)
        assert response.file == "https://cdn.ozon.ru/vouchers/123456.csv"
