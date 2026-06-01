from ...core import APIManager
from ...schemas.beta import (
    ActionsDiscountsTaskListRequest,
    ActionsDiscountsTaskListResponse,
)


class ActionsDiscountsTaskListMixin(APIManager):
    """Реализует метод /v2/actions/discounts-task/list"""

    async def actions_discounts_task_list(
            self: "ActionsDiscountsTaskListMixin",
            request: ActionsDiscountsTaskListRequest
    ) -> ActionsDiscountsTaskListResponse:
        """Возвращает список заявок покупателей на скидку.

        Notes:
            • Пагинация по `last_id`: передайте полученный `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetDiscountTaskListV2

        Args:
            request: Запрос по схеме `ActionsDiscountsTaskListRequest`

        Returns:
            Список заявок по схеме `ActionsDiscountsTaskListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_discounts_task_list(
                    ActionsDiscountsTaskListRequest(status="NEW", limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="actions/discounts-task/list",
            payload=request.model_dump()
        )
        return ActionsDiscountsTaskListResponse(**response)
