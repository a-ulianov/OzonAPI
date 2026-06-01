import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSCreateReturnPointListRequest,
    WarehouseFBSCreateReturnPointListResponse,
)


class TestWarehouseFBSCreateReturnPointList:
    """Тесты для метода warehouse_fbs_create_return_point_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_create_return_point_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_create_return_point_list."""

        mock_api_request.return_value = {
            "has_next": False,
            "is_selected_point_available": True,
            "last_id": 10,
            "points": [
                {
                    "address": "Москва",
                    "coordinates": {"latitude": 55.7, "longitude": 37.6},
                    "id": 100,
                    "name": "ПВЗ-1",
                    "type": "PVZ",
                    "utc_offset": 180,
                    "working_days": [
                        {"day": "MONDAY", "from": "09:00", "to": "18:00"}
                    ],
                }
            ],
        }

        request = WarehouseFBSCreateReturnPointListRequest(country_code="RU", limit=20)

        response = await api.warehouse_fbs_create_return_point_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/create/return-point/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSCreateReturnPointListResponse)
        assert response.points[0].id == 100
        assert response.points[0].working_days[0].from_ == "09:00"
        assert response.points[0].working_days[0].day == "MONDAY"
