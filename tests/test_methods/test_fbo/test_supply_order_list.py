import datetime

import pytest

from src.ozonapi.seller.common.enumerations.fbo import (
    SupplyOrderSortDirection,
    SupplyOrderSortField,
    SupplyOrderState,
    TimeslotFilterType,
)
from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderListFilter,
    SupplyOrderListRequest,
    SupplyOrderListResponse,
    SupplyOrderListTimeslotFromRange,
)


class TestSupplyOrderList:
    """Тесты для метода supply_order_list."""

    @pytest.mark.asyncio
    async def test_supply_order_list(self, api, mock_api_request):
        """Тестирует метод supply_order_list."""

        mock_response_data = {
            "order_ids": [1234567890, 1234567891],
            "last_id": "last-456",
        }
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderListRequest(
            filter=SupplyOrderListFilter(
                states=[SupplyOrderState.READY_TO_SUPPLY, SupplyOrderState.IN_TRANSIT],
                dropoff_warehouse_ids=[111, 222],
                order_number_search="ORDER-1",
                timeslot_from_range=SupplyOrderListTimeslotFromRange(
                    from_=datetime.datetime(2026, 6, 1),
                    to=datetime.datetime(2026, 6, 30),
                    timeslot_filter_type=TimeslotFilterType.BY_LOCAL_TIME,
                ),
            ),
            limit=100,
            sort_by=SupplyOrderSortField.ORDER_CREATION,
            sort_dir=SupplyOrderSortDirection.DESC,
        )

        response = await api.supply_order_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="supply-order/list",
            payload=request.model_dump(by_alias=True),
        )

        # Поле `from` (зарезервированное слово) должно сериализоваться под ключом "from".
        sent_payload = mock_api_request.call_args.kwargs["payload"]
        assert "from" in sent_payload["filter"]["timeslot_from_range"]

        assert isinstance(response, SupplyOrderListResponse)
        assert response.order_ids == [1234567890, 1234567891]
        assert response.last_id == "last-456"
