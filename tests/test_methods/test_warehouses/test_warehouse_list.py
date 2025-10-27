import pytest

from src.ozonapi.seller.common.enumerations.warehouses import WarehouseWorkingDays, WarehouseStatus
from src.ozonapi.seller.schemas.warehouses import WarehouseListResponse


class TestWarehouseList:
    """Тесты для метода warehouse_list."""

    @pytest.mark.asyncio
    async def test_warehouse_list(self, api, mock_api_request):
        """Тестирует метод warehouse_list."""

        mock_response_data = {
            "result": [
                {
                    "has_entrusted_acceptance": True,
                    "is_rfbs": False,
                    "name": "Основной склад FBS",
                    "warehouse_id": 15588127982000,
                    "can_print_act_in_advance": True,
                    "first_mile_type": {
                        "dropoff_point_id": "point_123",
                        "dropoff_timeslot_id": 456,
                        "first_mile_is_changing": False,
                        "first_mile_type": "DropOff"
                    },
                    "has_postings_limit": True,
                    "is_karantin": False,
                    "is_kgt": True,
                    "is_economy": False,
                    "is_timetable_editable": True,
                    "min_postings_limit": 10,
                    "postings_limit": 100,
                    "min_working_days": 5,
                    "status": WarehouseStatus.CREATED,
                    "working_days": [
                        WarehouseWorkingDays.MONDAY,
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        response = await api.warehouse_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/list",
        )
        assert isinstance(response, WarehouseListResponse)
        assert len(response.result) == 1
        warehouse = response.result[0]
        assert warehouse.warehouse_id == 15588127982000
        assert warehouse.name == "Основной склад FBS"
        assert warehouse.is_rfbs is False
        assert warehouse.has_entrusted_acceptance is True
        assert warehouse.first_mile_type.first_mile_type == "DropOff"