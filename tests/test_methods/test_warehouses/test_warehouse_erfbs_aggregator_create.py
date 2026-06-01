import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseERFBSAggregatorCreateRequest,
    WarehouseERFBSOperationResponse,
)


class TestWarehouseERFBSAggregatorCreate:
    """Тесты для метода warehouse_erfbs_aggregator_create."""

    @pytest.mark.asyncio
    async def test_warehouse_erfbs_aggregator_create(self, api, mock_api_request):
        """Тестирует метод warehouse_erfbs_aggregator_create."""

        mock_api_request.return_value = {"operation_id": "op-erfbs-agg-1"}

        request = WarehouseERFBSAggregatorCreateRequest(
            address_coordinates={"latitude": 55.7, "longitude": 37.6},
            is_auto_assembly=True,
            name="Склад Express",
            phone="+70000000000",
            min_order_value=500,
            delivery_method={
                "name": "Партнёры Ozon",
                "cut_in": 60,
                "deliver_to_pvz": True,
                "courier_phones": ["+70000000001"],
                "delivery_costs": {"max_amount": 500, "min_amount": 100, "percent": 5.0},
                "return_settings": {
                    "return_method": "COURIER",
                    "contact_days": 3,
                },
            },
            timetable_warehouse={
                "working_days": [{"day": "MONDAY", "from": "09:00", "to": "18:00"}],
                "holidays": [{"day": "2026-01-01", "from": "00:00", "to": "23:59"}],
            },
        )

        response = await api.warehouse_erfbs_aggregator_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/aggregator/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseERFBSOperationResponse)
        assert response.operation_id == "op-erfbs-agg-1"
        # reserved words from/to serialised via alias in nested timetable
        payload = request.model_dump(by_alias=True)
        assert "from" in payload["timetable_warehouse"]["working_days"][0]
