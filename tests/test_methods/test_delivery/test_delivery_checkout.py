import pytest

from src.ozonapi.seller.schemas.delivery import (
    DeliveryCheckoutRequest,
    DeliveryCheckoutResponse,
)


class TestDeliveryCheckout:
    """Тесты для метода delivery_checkout."""

    @pytest.mark.asyncio
    async def test_delivery_checkout(self, api, mock_api_request):
        """Тестирует метод delivery_checkout."""

        mock_api_request.return_value = {
            "splits": [
                {
                    "delivery_method": {
                        "delivery_time_zone_offset": 180,
                        "delivery_type": "PVZ",
                        "id": 1,
                        "name": "Пункт выдачи",
                        "timeslots": [
                            {
                                "client_date_range": {
                                    "from": "2026-06-02T09:00:00Z",
                                    "to": "2026-06-02T21:00:00Z",
                                },
                                "logistic_date_range": {
                                    "from": "2026-06-01T09:00:00Z",
                                    "to": "2026-06-01T21:00:00Z",
                                },
                                "timeslot_id": 77,
                            }
                        ],
                        "unavailable_reason": "UNSPECIFIED",
                        "warehouse_time_zone_offset": 180,
                    },
                    "delivery_schema": "FBS",
                    "items": [{"offer_id": "art-1", "quantity": 1, "sku": 222}],
                    "unavailable_reason": "UNSPECIFIED",
                    "warehouse_id": 333,
                }
            ]
        }

        request = DeliveryCheckoutRequest(
            buyer_phone="+70000000000",
            delivery_schema="FBS",
            delivery_type={"pick_up": {"map_point_id": 555}},
            items=[{"sku": 222, "quantity": 1}],
        )

        response = await api.delivery_checkout(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="delivery/checkout",
            payload=request.model_dump()
        )

        assert isinstance(response, DeliveryCheckoutResponse)
        split = response.splits[0]
        assert split.warehouse_id == 333
        assert split.delivery_method.timeslots[0].timeslot_id == 77
        assert split.delivery_method.timeslots[0].client_date_range.from_ is not None
