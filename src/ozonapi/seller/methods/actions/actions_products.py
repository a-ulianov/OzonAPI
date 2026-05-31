from ...core import APIManager
from ...schemas.actions import (
    ActionsProductsRequest,
    ActionsProductsResponse,
)


class ActionsProductsMixin(APIManager):
    """Реализует метод /v1/actions/products"""

    async def actions_products(
            self: "ActionsProductsMixin",
            request: ActionsProductsRequest,
    ) -> ActionsProductsResponse:
        """Получает список товаров, участвующих в акции.

        Notes:
            • Возвращает товары, которые уже добавлены в указанную акцию (`action_id`).
            • Для постраничной выборки используйте `limit` и `last_id` (или `offset`).
            • Добавить товары в акцию можно методом `actions_products_activate()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsProducts

        Args:
            request: Параметры выборки товаров по схеме `ActionsProductsRequest`

        Returns:
            Список участвующих в акции товаров по схеме `ActionsProductsResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_products(
                    ActionsProductsRequest(action_id=123456, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/products",
            payload=request.model_dump(),
        )
        return ActionsProductsResponse(**response)
