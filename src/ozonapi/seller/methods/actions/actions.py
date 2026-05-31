from ...core import APIManager
from ...schemas.actions import ActionsResponse


class ActionsMixin(APIManager):
    """Реализует метод /v1/actions"""

    async def actions(
            self: "ActionsMixin",
    ) -> ActionsResponse:
        """Получает список акций Ozon, доступных продавцу.

        Notes:
            • Метод возвращает все акции, в которых продавец может участвовать.
            • Для каждой акции доступны тип, даты проведения, размер скидки и счётчики товаров.
            • Идентификатор акции (`id`) используется в методах работы с товарами акции.

        References:
            https://docs.ozon.ru/api/seller/#operation/Promos

        Returns:
            Список доступных акций по схеме `ActionsResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions",
            payload={},
        )
        return ActionsResponse(**response)
