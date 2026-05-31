import pytest

from src.ozonapi.seller.common.enumerations.warehouses import (
    CarriageLabelType,
    FirstMileTypeV2,
    WarehouseWorkingDayV2,
)
from src.ozonapi.seller.schemas.warehouses import WarehouseListResponse


class TestWarehouseList:
    """Тесты для метода warehouse_list (API v2)."""

    @pytest.mark.asyncio
    async def test_warehouse_list(self, api, mock_api_request):
        """Тестирует метод warehouse_list."""

        mock_response_data = {
            "cursor": "next_cursor_value",
            "has_next": True,
            "warehouses": [
                {
                    "warehouse_id": 15588127982000,
                    "name": "Основной склад FBS",
                    "status": "created",
                    "warehouse_type": "fbs",
                    "is_rfbs": False,
                    "is_kgt": True,
                    "is_express": False,
                    "has_entrusted_acceptance": True,
                    "has_postings_limit": True,
                    "min_postings_limit": 10,
                    "postings_limit": 100,
                    "carriage_label_type": "BIG",
                    "working_days": ["MONDAY", "TUESDAY"],
                    "address_info": {
                        "address": "Москва, ул. Примерная, 1",
                        "latitude": 55.75,
                        "longitude": 37.61,
                        "utc": "+03:00",
                    },
                    "first_mile": {
                        "dropoff_point_id": "point_123",
                        "first_mile_is_changing": False,
                        "timeslot_id": 456,
                        "type": "DROP_OFF",
                    },
                    "timetable": {
                        "timetable_from": "2023-10-01T08:00:00Z",
                        "timetable_to": "2023-10-01T20:00:00Z",
                        "working_hours": [
                            {"time_from": "2023-10-01T08:00:00Z", "time_to": "2023-10-01T20:00:00Z"}
                        ],
                    },
                }
            ],
        }
        mock_api_request.return_value = mock_response_data

        response = await api.warehouse_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="warehouse/list",
            payload={"limit": 100, "cursor": None, "warehouse_ids": None},
        )
        assert isinstance(response, WarehouseListResponse)
        assert response.cursor == "next_cursor_value"
        assert response.has_next is True
        assert len(response.warehouses) == 1
        warehouse = response.warehouses[0]
        assert warehouse.warehouse_id == 15588127982000
        assert warehouse.name == "Основной склад FBS"
        assert warehouse.is_rfbs is False
        assert warehouse.has_entrusted_acceptance is True
        assert warehouse.warehouse_type == "fbs"
        assert warehouse.carriage_label_type == CarriageLabelType.BIG
        assert warehouse.working_days == [WarehouseWorkingDayV2.MONDAY, WarehouseWorkingDayV2.TUESDAY]
        assert warehouse.first_mile.type == FirstMileTypeV2.DROP_OFF
        assert warehouse.first_mile.dropoff_point_id == "point_123"
        assert warehouse.address_info.address == "Москва, ул. Примерная, 1"
        assert warehouse.timetable.working_hours[0].time_from is not None
