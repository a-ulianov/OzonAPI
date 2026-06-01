import pytest

from src.ozonapi.seller.schemas.delivery import (
    DeliveryPointInfoRequest,
    DeliveryPointInfoResponse,
)


class TestDeliveryPointInfo:
    """Тесты для метода delivery_point_info."""

    @pytest.mark.asyncio
    async def test_delivery_point_info(self, api, mock_api_request):
        """Тестирует метод delivery_point_info."""

        mock_api_request.return_value = {
            "points": [
                {
                    "delivery_method": {
                        "address": "Москва, ул. Пушкина",
                        "address_details": {
                            "city": "Москва",
                            "house": "1",
                            "region": "Москва",
                            "street": "Пушкина",
                        },
                        "coordinates": {"lat": 55.75, "long": 37.61},
                        "delivery_type": {"id": 1, "name": "ПВЗ"},
                        "map_point_id": 123,
                        "name": "ПВЗ-1",
                        "properties": [{"enabled": True, "name": "примерочная"}],
                        "pvz_rating": 5,
                        "storage_period": 7,
                        "working_hours": [
                            {
                                "date": "2026-06-01T00:00:00Z",
                                "periods": [
                                    {
                                        "max": {"hours": 21, "minutes": 0},
                                        "min": {"hours": 9, "minutes": 0},
                                    }
                                ],
                            }
                        ],
                    },
                    "enabled": True,
                }
            ]
        }

        request = DeliveryPointInfoRequest(map_point_ids=["123"])

        response = await api.delivery_point_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery/point/info",
            payload=request.model_dump()
        )

        assert isinstance(response, DeliveryPointInfoResponse)
        point = response.points[0]
        assert point.enabled is True
        assert point.delivery_method.map_point_id == 123
        assert point.delivery_method.delivery_type.name == "ПВЗ"
        assert point.delivery_method.working_hours[0].periods[0].min.hours == 9
