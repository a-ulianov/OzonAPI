import pytest

from src.ozonapi.seller.schemas.fbo import SupplyOrderGetRequest, SupplyOrderGetResponse


class TestSupplyOrderGet:
    """Тесты для метода supply_order_get."""

    @pytest.mark.asyncio
    async def test_supply_order_get(self, api, mock_api_request):
        """Тестирует метод supply_order_get."""

        mock_response_data = {
            "orders": [
                {
                    "order_id": 1234567890,
                    "order_number": "ORDER-123",
                    "state": "READY_TO_SUPPLY",
                    "created_date": "2026-05-01T10:00:00Z",
                    "state_updated_date": "2026-05-02T10:00:00Z",
                    "data_filling_deadline_utc": "2026-05-10T10:00:00Z",
                    "dropoff_warehouse": {
                        "address": "Москва, ул. Тестовая, 1",
                        "name": "Пункт отгрузки",
                        "warehouse_id": 111,
                    },
                    "order_tags": {
                        "is_econom": False,
                        "is_super_fbo": True,
                        "seller_warehouse_id": 999,
                    },
                    "supplies": [
                        {
                            "supply_id": 555,
                            "bundle_id": "bundle-1",
                            "state": "DATA_FILLING",
                            "is_crossdock": False,
                            "storage_warehouse": {
                                "address": "Склад хранения",
                                "name": "Хоругвино",
                                "warehouse_id": 222,
                            },
                            "supply_tags": {"is_jewelry": False, "is_utd": True},
                        }
                    ],
                    "timeslot": {
                        "timeslot": {
                            "from": "2026-06-01T10:00:00Z",
                            "to": "2026-06-01T12:00:00Z",
                        },
                        "timezone_info": {"iana_name": "Europe/Moscow", "offset": "10800"},
                    },
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderGetRequest(order_ids=[1234567890])

        response = await api.supply_order_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="supply-order/get",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderGetResponse)
        assert len(response.orders) == 1
        order = response.orders[0]
        assert order.order_id == 1234567890
        assert order.state == "READY_TO_SUPPLY"
        assert order.dropoff_warehouse.warehouse_id == 111
        assert order.order_tags.is_super_fbo is True
        assert order.supplies[0].supply_id == 555
        assert order.supplies[0].storage_warehouse.name == "Хоругвино"
        assert order.timeslot.timeslot.from_ is not None
        assert order.timeslot.timezone_info.iana_name == "Europe/Moscow"
