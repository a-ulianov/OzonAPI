import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsDiscountsTaskApproveRequest,
    ActionsDiscountsTaskApproveTask,
    DiscountTaskResponse,
)


class TestActionsDiscountsTaskApprove:
    """Тесты для метода actions_discounts_task_approve."""

    @pytest.mark.asyncio
    async def test_actions_discounts_task_approve(self, api, mock_api_request):
        """Тестирует метод actions_discounts_task_approve."""
        mock_api_request.return_value = {
            "result": {"success_count": 1, "fail_count": 0, "fail_details": []}
        }

        request = ActionsDiscountsTaskApproveRequest(
            tasks=[ActionsDiscountsTaskApproveTask(id=1, approved_price=900.0)]
        )
        response = await api.actions_discounts_task_approve(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/approve",
            payload=request.model_dump(),
        )
        assert isinstance(response, DiscountTaskResponse)
        assert response.result.success_count == 1
        assert response.result.fail_count == 0
