import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSPickUpPlanningListResponse,
)


class TestWarehouseFBSPickUpPlanningList:
    """Тесты для метода warehouse_fbs_pickup_planning_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_pickup_planning_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_pickup_planning_list."""

        mock_api_request.return_value = {
            "result": {
                "warehouses": [
                    {
                        "can_modify_pickup_plan": True,
                        "has_postings_to_be_planned": True,
                        "is_pickup_planned": False,
                        "last_pickup_plan_date_at": "2026-06-01T10:00:00Z",
                        "warehouse_id": 123,
                        "warehouse_name": "Склад",
                    }
                ]
            }
        }

        response = await api.warehouse_fbs_pickup_planning_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/planning/list",
            payload={}
        )

        assert isinstance(response, WarehouseFBSPickUpPlanningListResponse)
        assert response.result.warehouses[0].warehouse_id == 123
        assert response.result.warehouses[0].can_modify_pickup_plan is True
