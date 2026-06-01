import pytest

from src.ozonapi.seller.schemas.orders import (
    OrderCancelRequest,
    OrderCancelResponse,
)


class TestOrderCancel:
    """Тесты для метода order_cancel."""

    @pytest.mark.asyncio
    async def test_order_cancel(self, api, mock_api_request):
        """Тестирует метод order_cancel."""

        mock_api_request.return_value = {"message": "ok"}

        request = OrderCancelRequest(
            order_number="123-456", reason_id=352, reason_message="нет товара"
        )

        response = await api.order_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="order/cancel",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, OrderCancelResponse)
        assert response.message == "ok"
