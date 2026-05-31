import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsDiscountsTaskListRequest,
    ActionsDiscountsTaskListResponse,
)


class TestActionsDiscountsTaskList:
    """Тесты для метода actions_discounts_task_list."""

    @pytest.mark.asyncio
    async def test_actions_discounts_task_list(self, api, mock_api_request):
        """Тестирует метод actions_discounts_task_list."""
        mock_api_request.return_value = {
            "result": [
                {
                    "id": 1,
                    "sku": 635548518,
                    "requested_price": 800.0,
                    "original_price": 1000.0,
                    "discount_percent": 20.0,
                }
            ]
        }

        request = ActionsDiscountsTaskListRequest(status="NEW", page=1, limit=50)
        response = await api.actions_discounts_task_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, ActionsDiscountsTaskListResponse)
        assert response.result[0].id == 1
        assert response.result[0].requested_price == 800.0
