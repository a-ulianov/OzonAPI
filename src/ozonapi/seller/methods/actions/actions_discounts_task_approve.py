from ...core import APIManager
from ...schemas.actions import (
    ActionsDiscountsTaskApproveRequest,
    DiscountTaskResponse,
)


class ActionsDiscountsTaskApproveMixin(APIManager):
    """Реализует метод /v1/actions/discounts-task/approve"""

    async def actions_discounts_task_approve(
            self: "ActionsDiscountsTaskApproveMixin",
            request: ActionsDiscountsTaskApproveRequest,
    ) -> DiscountTaskResponse:
        """Согласовывает заявки покупателей на скидку.

        Notes:
            • Для каждой заявки укажите согласованную цену (`approved_price`).
            • За один запрос можно обработать несколько заявок.
            • В ответе возвращается количество успешно обработанных заявок и детали ошибок.
            • Список заявок можно получить методом `actions_discounts_task_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DiscountTask_Approve

        Args:
            request: Список заявок для согласования по схеме `ActionsDiscountsTaskApproveRequest`

        Returns:
            Результат согласования заявок по схеме `DiscountTaskResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_discounts_task_approve(
                    ActionsDiscountsTaskApproveRequest(
                        tasks=[
                            ActionsDiscountsTaskApproveTask(id=1, approved_price=999.0)
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/discounts-task/approve",
            payload=request.model_dump(),
        )
        return DiscountTaskResponse(**response)
