import pytest

from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderDetailsRequest,
    SupplyOrderDetailsResponse,
)


class TestSupplyOrderDetails:
    """Тесты для метода supply_order_details."""

    @pytest.mark.asyncio
    async def test_supply_order_details(self, api, mock_api_request):
        """Тестирует метод supply_order_details."""

        mock_response_data = {
            "order_id": 1234567890,
            "order_number": "ORDER-123",
            "state": "READY_TO_SUPPLY",
            "created_date": "2026-05-01T10:00:00Z",
            "state_updated_date": "2026-05-02T10:00:00Z",
            "data_filling_deadline_utc": "2026-05-10T10:00:00Z",
            "dropoff_warehouse_id": 111,
            "order_tags": {"is_econom": False, "is_super_fbo": True},
            "supplies": [
                {
                    "supply_id": 555,
                    "supply_state": "DATA_FILLING",
                    "is_crossdock": False,
                    "overdue_reason": "UNSPECIFIED",
                    "storage_warehouse": {
                        "name": "Хоругвино",
                        "warehouse_id": 222,
                    },
                    "cancellation_allowability": {
                        "can_set": True,
                        "can_not_set_reasons": [],
                    },
                    "content": {
                        "bundle_id": "bundle-1",
                        "can_set": False,
                        "can_not_set_reasons": ["DEADLINE"],
                    },
                    "ettn_info": {"contains_valid": False, "is_required": False, "is_uploaded": False},
                    "supply_tags": {"is_jewelry": False, "is_utd": True},
                }
            ],
            "timeslot": {
                "can_set": True,
                "can_not_set_reasons": [],
                "value": {
                    "timeslot": {"from": "2026-06-01T10:00:00Z", "to": "2026-06-01T12:00:00Z"},
                    "timezone_info": {"iana_name": "Europe/Moscow", "offset": "10800"},
                },
            },
            "vehicle": {
                "can_set": True,
                "can_not_set_reasons": [],
                "value": {
                    "driver_name": "Иванов Иван",
                    "driver_phone": "+79991234567",
                    "vehicle_model": "ГАЗель",
                    "vehicle_number": "А123БВ777",
                },
            },
        }
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderDetailsRequest(order_id=1234567890)

        response = await api.supply_order_details(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/details",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderDetailsResponse)
        assert response.order_id == 1234567890
        assert response.dropoff_warehouse_id == 111
        assert response.order_tags.is_super_fbo is True
        assert response.supplies[0].supply_id == 555
        assert response.supplies[0].content.can_not_set_reasons == ["DEADLINE"]
        assert response.timeslot.can_set is True
        assert response.timeslot.value.timeslot.from_ is not None
        assert response.vehicle.value.vehicle_number == "А123БВ777"
