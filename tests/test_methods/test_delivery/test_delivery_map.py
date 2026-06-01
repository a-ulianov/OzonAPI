import pytest

from src.ozonapi.seller.schemas.delivery import (
    DeliveryMapRequest,
    DeliveryMapResponse,
)


class TestDeliveryMap:
    """Тесты для метода delivery_map."""

    @pytest.mark.asyncio
    async def test_delivery_map(self, api, mock_api_request):
        """Тестирует метод delivery_map."""

        mock_api_request.return_value = {
            "clusters": [
                {
                    "coordinate": {"lat": 55.75, "long": 37.61},
                    "is_same_building": False,
                    "map_point_ids": ["1", "2"],
                    "points_count": 2,
                    "viewport": {
                        "left_bottom": {"lat": 55.7, "long": 37.5},
                        "right_top": {"lat": 55.8, "long": 37.7},
                    },
                }
            ]
        }

        request = DeliveryMapRequest(
            viewport={
                "left_bottom": {"lat": 55.7, "long": 37.5},
                "right_top": {"lat": 55.8, "long": 37.7},
            },
            zoom=12,
        )

        response = await api.delivery_map(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery/map",
            payload=request.model_dump()
        )

        assert isinstance(response, DeliveryMapResponse)
        assert response.clusters[0].points_count == 2
        assert response.clusters[0].coordinate.lat == 55.75
        assert response.clusters[0].map_point_ids == ["1", "2"]
