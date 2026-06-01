import pytest

from src.ozonapi.seller.schemas.beta import (
    ActionsDiscountsTaskListRequest,
    ActionsDiscountsTaskListResponse,
)


class TestActionsDiscountsTaskList:
    """Тесты для метода actions_discounts_task_list."""

    @pytest.mark.asyncio
    async def test_actions_discounts_task_list(self, api, mock_api_request):
        """Тестирует метод actions_discounts_task_list."""

        mock_api_request.return_value = {
            "tasks": [
                {
                    "id": 77,
                    "sku": 222,
                    "name": "Товар",
                    "status": "NEW",
                    "requested_price": 900.0,
                    "approved_price": 0.0,
                    "is_auto_moderated": False,
                }
            ]
        }

        request = ActionsDiscountsTaskListRequest(status="NEW", limit=50)

        response = await api.actions_discounts_task_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="actions/discounts-task/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ActionsDiscountsTaskListResponse)
        assert response.tasks[0].id == 77
        assert response.tasks[0].status == "NEW"
