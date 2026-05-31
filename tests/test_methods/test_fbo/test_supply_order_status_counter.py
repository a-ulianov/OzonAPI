import pytest

from src.ozonapi.seller.schemas.fbo import SupplyOrderStatusCounterResponse


class TestSupplyOrderStatusCounter:
    """Тесты для метода supply_order_status_counter."""

    @pytest.mark.asyncio
    async def test_supply_order_status_counter(self, api, mock_api_request):
        """Тестирует метод supply_order_status_counter."""

        mock_response_data = {
            "items": [
                {"count": 5, "order_state": "ORDER_STATE_DATA_FILLING"},
                {"count": 2, "order_state": "ORDER_STATE_COMPLETED"},
            ]
        }
        mock_api_request.return_value = mock_response_data

        response = await api.supply_order_status_counter()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/status/counter",
        )

        assert isinstance(response, SupplyOrderStatusCounterResponse)
        assert len(response.items) == 2
        assert response.items[0].count == 5
        assert response.items[0].order_state == "ORDER_STATE_DATA_FILLING"
        assert response.items[1].count == 2
        assert response.items[1].order_state == "ORDER_STATE_COMPLETED"
