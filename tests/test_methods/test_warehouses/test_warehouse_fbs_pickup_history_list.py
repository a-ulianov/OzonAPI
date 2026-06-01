import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSPickUpHistoryListRequest,
    WarehouseFBSPickUpHistoryListResponse,
)


class TestWarehouseFBSPickUpHistoryList:
    """Тесты для метода warehouse_fbs_pickup_history_list."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_pickup_history_list(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_pickup_history_list."""

        mock_api_request.return_value = {
            "result": {
                "cursor": "next-cursor",
                "history": [
                    {
                        "planned_date": "2026-06-01",
                        "status": "DONE",
                        "updated_at": "2026-06-01T10:00:00Z",
                        "warehouse_id": 123,
                        "warehouse_name": "Склад",
                        "was_planned": True,
                    }
                ],
            }
        }

        request = WarehouseFBSPickUpHistoryListRequest(
            limit=50, filter={"was_planned": True}
        )

        response = await api.warehouse_fbs_pickup_history_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/history/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSPickUpHistoryListResponse)
        assert response.result.cursor == "next-cursor"
        assert response.result.history[0].warehouse_id == 123
