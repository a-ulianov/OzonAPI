import datetime

import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderTimeslot,
    SupplyOrderTimeslotUpdateRequest,
    SupplyOrderTimeslotUpdateResponse,
)


class TestSupplyOrderTimeslotUpdate:
    """Тесты для метода supply_order_timeslot_update."""

    @pytest.mark.asyncio
    async def test_supply_order_timeslot_update(self, api, mock_api_request):
        """Тестирует метод supply_order_timeslot_update."""

        mock_response_data = {"operation_id": "operation-123", "errors": []}
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderTimeslotUpdateRequest(
            supply_order_id=1234567890,
            timeslot=SupplyOrderTimeslot(
                from_=datetime.datetime(2026, 6, 1, 10, 0),
                to=datetime.datetime(2026, 6, 1, 12, 0),
            ),
        )

        response = await api.supply_order_timeslot_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/timeslot/update",
            payload=request.model_dump(by_alias=True),
        )

        # Поле `from` (зарезервированное слово) должно сериализоваться под ключом "from".
        sent_payload = mock_api_request.call_args.kwargs["payload"]
        assert "from" in sent_payload["timeslot"] and "from_" not in sent_payload["timeslot"]

        assert isinstance(response, SupplyOrderTimeslotUpdateResponse)
        assert response.operation_id == "operation-123"
        assert response.errors == []
