import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    SupplyOrderCancelRequest,
    SupplyOrderCancelResponse,
)


class TestSupplyOrderCancel:
    """Тесты для метода supply_order_cancel."""

    @pytest.mark.asyncio
    async def test_supply_order_cancel(self, api, mock_api_request):
        """Тестирует метод supply_order_cancel."""

        mock_api_request.return_value = {"operation_id": "op-cancel-1"}

        request = SupplyOrderCancelRequest(order_id=123)

        response = await api.supply_order_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/cancel",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, SupplyOrderCancelResponse)
        assert response.operation_id == "op-cancel-1"
