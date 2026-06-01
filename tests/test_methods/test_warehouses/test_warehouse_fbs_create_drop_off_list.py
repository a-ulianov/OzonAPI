import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSCreateDropOffListRequest,
    WarehouseFBSCreateDropOffListResponse,
)


class TestWarehouseFBSCreateDropOffList:
    """Тесты для метода warehouse_fbs_create_drop_off_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_create_drop_off_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_create_drop_off_list."""

        mock_api_request.return_value = {
            "points": [
                {
                    "address": "Москва",
                    "coordinates": {"latitude": 55.7, "longitude": 37.6},
                    "discount_percent": 5.0,
                    "id": "dp-1",
                    "last_transit_time_local": {"hours": 12, "minutes": 30},
                    "type": "PVZ",
                }
            ]
        }

        request = WarehouseFBSCreateDropOffListRequest(
            country_code="RU",
            is_kgt=False,
            search={"address": "Москва", "types": ["PVZ"]},
        )

        response = await api.warehouse_fbs_create_drop_off_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/drop-off/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSCreateDropOffListResponse)
        assert response.points[0].id == "dp-1"
        assert response.points[0].coordinates.latitude == 55.7
        assert response.points[0].last_transit_time_local.hours == 12
