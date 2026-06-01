import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsUpdateInstallmentParameters,
    SellerActionsUpdateInstallmentRequest,
    SellerActionsUpdateInstallmentResponse,
)


class TestSellerActionsUpdateInstallment:
    """Тесты для метода seller_actions_update_installment."""

    @pytest.mark.asyncio
    async def test_seller_actions_update_installment(self, api, mock_api_request):
        """Тестирует метод seller_actions_update_installment."""

        mock_api_request.return_value = {}

        request = SellerActionsUpdateInstallmentRequest(
            action_id=123456,
            action_parameters=SellerActionsUpdateInstallmentParameters(
                title="Рассрочка на технику",
                date_start="2026-07-01T00:00:00Z",
            ),
        )

        response = await api.seller_actions_update_installment(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/installment",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsUpdateInstallmentResponse)
