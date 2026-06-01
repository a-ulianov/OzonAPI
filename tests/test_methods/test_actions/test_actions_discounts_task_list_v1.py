import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsDiscountsTaskListV1Request,
    ActionsDiscountsTaskListV1Response,
)


class TestActionsDiscountsTaskListV1:
    """Тесты для метода actions_discounts_task_list_v1 (устаревший v1)."""

    @pytest.mark.asyncio
    async def test_actions_discounts_task_list_v1(self, api, mock_api_request):
        """Тестирует метод actions_discounts_task_list_v1."""
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

        request = ActionsDiscountsTaskListV1Request(status="NEW", page=1, limit=50)
        response = await api.actions_discounts_task_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, ActionsDiscountsTaskListV1Response)
        assert response.result[0].id == 1
        assert response.result[0].requested_price == 800.0
