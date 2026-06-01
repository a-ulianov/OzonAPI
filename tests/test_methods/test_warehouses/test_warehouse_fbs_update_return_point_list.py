import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSUpdateReturnPointListRequest,
    WarehouseFBSUpdateReturnPointListResponse,
)


class TestWarehouseFBSUpdateReturnPointList:
    """Тесты для метода warehouse_fbs_update_return_point_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_update_return_point_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_update_return_point_list."""

        mock_api_request.return_value = {
            "has_next": True,
            "is_selected_point_available": False,
            "last_id": 20,
            "points": [
                {
                    "address": "Санкт-Петербург",
                    "coordinates": {"latitude": 59.9, "longitude": 30.3},
                    "id": 200,
                    "name": "ПВЗ-2",
                    "type": "SC",
                    "utc_offset": 180,
                    "working_days": [
                        {"day": "FRIDAY", "from": "10:00", "to": "20:00"}
                    ],
                }
            ],
        }

        request = WarehouseFBSUpdateReturnPointListRequest(warehouse_id=123, limit=20)

        response = await api.warehouse_fbs_update_return_point_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/update/return-point/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSUpdateReturnPointListResponse)
        assert response.has_next is True
        assert response.points[0].id == 200
        assert response.points[0].working_days[0].to_ == "20:00"
