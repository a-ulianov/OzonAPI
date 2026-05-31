import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsDiscountsTaskDeclineRequest,
    ActionsDiscountsTaskDeclineTask,
    DiscountTaskResponse,
)


class TestActionsDiscountsTaskDecline:
    """Тесты для метода actions_discounts_task_decline."""

    @pytest.mark.asyncio
    async def test_actions_discounts_task_decline(self, api, mock_api_request):
        """Тестирует метод actions_discounts_task_decline."""
        mock_api_request.return_value = {
            "result": {"success_count": 1, "fail_count": 0, "fail_details": []}
        }

        request = ActionsDiscountsTaskDeclineRequest(
            tasks=[ActionsDiscountsTaskDeclineTask(id=1, seller_comment="Нет в наличии")]
        )
        response = await api.actions_discounts_task_decline(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/decline",
            payload=request.model_dump(),
        )
        assert isinstance(response, DiscountTaskResponse)
        assert response.result.success_count == 1
