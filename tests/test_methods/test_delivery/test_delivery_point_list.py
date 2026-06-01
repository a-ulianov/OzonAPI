import pytest

from src.ozonapi.seller.schemas.delivery import (
    DeliveryPointListRequest,
    DeliveryPointListResponse,
)


class TestDeliveryPointList:
    """Тесты для метода delivery_point_list."""

    @pytest.mark.asyncio
    async def test_delivery_point_list(self, api, mock_api_request):
        """Тестирует метод delivery_point_list."""

        mock_api_request.return_value = {
            "points": [
                {"coordinate": {"lat": 55.75, "long": 37.61}, "map_point_id": 123}
            ]
        }

        request = DeliveryPointListRequest()

        response = await api.delivery_point_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery/point/list",
            payload=request.model_dump()
        )

        assert isinstance(response, DeliveryPointListResponse)
        assert response.points[0].map_point_id == 123
        assert response.points[0].coordinate.long == 37.61
