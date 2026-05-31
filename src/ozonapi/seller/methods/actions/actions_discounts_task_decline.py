from ...core import APIManager
from ...schemas.actions import (
    ActionsDiscountsTaskDeclineRequest,
    DiscountTaskResponse,
)


class ActionsDiscountsTaskDeclineMixin(APIManager):
    """Реализует метод /v1/actions/discounts-task/decline"""

    async def actions_discounts_task_decline(
            self: "ActionsDiscountsTaskDeclineMixin",
            request: ActionsDiscountsTaskDeclineRequest,
    ) -> DiscountTaskResponse:
        """Отклоняет заявки покупателей на скидку.

        Notes:
            • За один запрос можно отклонить несколько заявок.
            • При необходимости укажите комментарий продавца (`seller_comment`).
            • В ответе возвращается количество успешно обработанных заявок и детали ошибок.
            • Список заявок можно получить методом `actions_discounts_task_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DiscountTask_Decline

        Args:
            request: Список заявок для отклонения по схеме `ActionsDiscountsTaskDeclineRequest`

        Returns:
            Результат отклонения заявок по схеме `DiscountTaskResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_discounts_task_decline(
                    ActionsDiscountsTaskDeclineRequest(
                        tasks=[
                            ActionsDiscountsTaskDeclineTask(id=1, seller_comment="Нет в наличии")
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/decline",
            payload=request.model_dump(),
        )
        return DiscountTaskResponse(**response)
