from ...core import APIManager
from ...schemas.actions import (
    ActionsDiscountsTaskListRequest,
    ActionsDiscountsTaskListResponse,
)


class ActionsDiscountsTaskListMixin(APIManager):
    """Реализует метод /v1/actions/discounts-task/list"""

    async def actions_discounts_task_list(
            self: "ActionsDiscountsTaskListMixin",
            request: ActionsDiscountsTaskListRequest = ActionsDiscountsTaskListRequest(),
    ) -> ActionsDiscountsTaskListResponse:
        """Получает список заявок покупателей на скидку.

        Notes:
            • Метод доступен продавцам, у которых включена опция «Скидка по запросу».
            • Фильтруйте заявки по статусу (`status`): NEW, SEEN, APPROVED, DECLINED, AUTODECLINED.
            • Для постраничной выборки используйте `page` и `limit`.
            • Согласовать или отклонить заявки можно методами `actions_discounts_task_approve()` и
              `actions_discounts_task_decline()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DiscountTask_List

        Args:
            request: Параметры фильтрации заявок по схеме `ActionsDiscountsTaskListRequest`

        Returns:
            Список заявок на скидку по схеме `ActionsDiscountsTaskListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_discounts_task_list(
                    ActionsDiscountsTaskListRequest(status="NEW", page=1, limit=50)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/list",
            payload=request.model_dump(),
        )
        return ActionsDiscountsTaskListResponse(**response)
