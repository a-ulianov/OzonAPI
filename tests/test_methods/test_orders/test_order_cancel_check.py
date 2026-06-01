import pytest

from src.ozonapi.seller.schemas.orders import (
    OrderCancelCheckRequest,
    OrderCancelCheckResponse,
)


class TestOrderCancelCheck:
    """Тесты для метода order_cancel_check."""

    @pytest.mark.asyncio
    async def test_order_cancel_check(self, api, mock_api_request):
        """Тестирует метод order_cancel_check."""

        mock_api_request.return_value = {
            "cancellable": True,
            "order_number": "123-456",
            "posting_groups": [{"posting_numbers": ["123-456-1"]}],
            "postings": [
                {
                    "cancellable": True,
                    "posting_number": "123-456-1",
                    "why_not_cancellable": "",
                }
            ],
        }

        request = OrderCancelCheckRequest(order_number="123-456")

        response = await api.order_cancel_check(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="order/cancel/check",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, OrderCancelCheckResponse)
        assert response.cancellable is True
        assert response.postings[0].posting_number == "123-456-1"
