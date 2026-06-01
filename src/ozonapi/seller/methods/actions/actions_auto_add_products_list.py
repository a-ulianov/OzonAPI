from ...core import APIManager
from ...schemas.actions import (
    ActionsAutoAddProductsListRequest,
    ActionsAutoAddProductsListResponse,
)


class ActionsAutoAddProductsListMixin(APIManager):
    """Реализует метод /v1/actions/auto-add/products/list"""

    async def actions_auto_add_products_list(
            self: "ActionsAutoAddProductsListMixin",
            request: ActionsAutoAddProductsListRequest,
    ) -> ActionsAutoAddProductsListResponse:
        """Получает список товаров из автодобавления в акцию.

        Notes:
            • Возвращает товары, которые автоматически добавляются в акцию на указанную дату.
            • Пагинация выполняется через `limit` и `offset`.
            • Поле `add_mode` товара показывает режим добавления.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsList

        Args:
            request: Идентификатор акции и параметры выборки по схеме
                `ActionsAutoAddProductsListRequest`

        Returns:
            Список товаров автодобавления по схеме `ActionsAutoAddProductsListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_auto_add_products_list(
                    ActionsAutoAddProductsListRequest(action_id=123456, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/list",
            payload=request.model_dump(),
        )
        return ActionsAutoAddProductsListResponse(**response)
