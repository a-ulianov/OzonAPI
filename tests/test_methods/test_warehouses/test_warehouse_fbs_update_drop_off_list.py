import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSUpdateDropOffListRequest,
    WarehouseFBSUpdateDropOffListResponse,
)


class TestWarehouseFBSUpdateDropOffList:
    """Тесты для метода warehouse_fbs_update_drop_off_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_update_drop_off_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_update_drop_off_list."""

        mock_api_request.return_value = {
            "points": [
                {
                    "address": "Москва",
                    "coordinates": {"latitude": 55.7, "longitude": 37.6},
                    "discount_percent": 0.0,
                    "id": "dp-2",
                    "type": "SC",
                }
            ]
        }

        request = WarehouseFBSUpdateDropOffListRequest(warehouse_id=123)

        response = await api.warehouse_fbs_update_drop_off_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/drop-off/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSUpdateDropOffListResponse)
        assert response.points[0].id == "dp-2"
        assert response.points[0].type == "SC"
