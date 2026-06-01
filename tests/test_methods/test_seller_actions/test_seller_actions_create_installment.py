import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsCreateInstallmentRequest,
    SellerActionsCreateInstallmentResponse,
)


class TestSellerActionsCreateInstallment:
    """Тесты для метода seller_actions_create_installment."""

    @pytest.mark.asyncio
    async def test_seller_actions_create_installment(self, api, mock_api_request):
        """Тестирует метод seller_actions_create_installment."""

        mock_api_request.return_value = {"action_id": 123456}

        request = SellerActionsCreateInstallmentRequest(
            title="Рассрочка на технику",
            date_start="2026-07-01T00:00:00Z",
        )

        response = await api.seller_actions_create_installment(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/installment",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsCreateInstallmentResponse)
        assert response.action_id == 123456
