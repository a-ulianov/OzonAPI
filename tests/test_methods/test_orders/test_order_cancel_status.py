import pytest

from src.ozonapi.seller.schemas.orders import (
    OrderCancelStatusRequest,
    OrderCancelStatusResponse,
)


class TestOrderCancelStatus:
    """Тесты для метода order_cancel_status."""

    @pytest.mark.asyncio
    async def test_order_cancel_status(self, api, mock_api_request):
        """Тестирует метод order_cancel_status."""

        mock_api_request.return_value = {
            "order_number": "123-456",
            "posting_number": ["123-456-1"],
            "state": "SUCCESS",
        }

        request = OrderCancelStatusRequest(order_number="123-456")

        response = await api.order_cancel_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="order/cancel/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, OrderCancelStatusResponse)
        assert response.state == "SUCCESS"
        assert response.posting_number == ["123-456-1"]
