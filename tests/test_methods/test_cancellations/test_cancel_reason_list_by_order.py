import pytest

from src.ozonapi.seller.schemas.cancellations import (
    CancelReasonListByOrderRequest,
    CancelReasonListByOrderResponse,
)


class TestCancelReasonListByOrder:
    """Тесты для метода cancel_reason_list_by_order."""

    @pytest.mark.asyncio
    async def test_cancel_reason_list_by_order(self, api, mock_api_request):
        """Тестирует метод cancel_reason_list_by_order."""

        mock_api_request.return_value = {
            "reasons": [{"id": 352, "name": "Товар закончился"}]
        }

        request = CancelReasonListByOrderRequest(order_number="12345678")

        response = await api.cancel_reason_list_by_order(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cancel-reason/list-by-order",
            payload=request.model_dump(),
        )

        assert isinstance(response, CancelReasonListByOrderResponse)
        assert response.reasons[0].id == 352
