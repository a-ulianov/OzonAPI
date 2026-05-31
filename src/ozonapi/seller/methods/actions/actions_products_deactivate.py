from ...core import APIManager
from ...schemas.actions import (
    ActionsProductsDeactivateRequest,
    ActionsProductsDeactivateResponse,
)


class ActionsProductsDeactivateMixin(APIManager):
    """Реализует метод /v1/actions/products/deactivate"""

    async def actions_products_deactivate(
            self: "ActionsProductsDeactivateMixin",
            request: ActionsProductsDeactivateRequest,
    ) -> ActionsProductsDeactivateResponse:
        """Удаляет товары из акции.

        Notes:
            • Передайте идентификатор акции и список идентификаторов товаров для удаления.
            • В ответе возвращаются идентификаторы удалённых товаров и список отклонённых
              с причинами.
            • Участвующие в акции товары можно получить методом `actions_products()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsProductsDeactivate

        Args:
            request: Идентификатор акции и идентификаторы товаров по схеме
                `ActionsProductsDeactivateRequest`

        Returns:
            Результат удаления товаров из акции по схеме `ActionsProductsDeactivateResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_products_deactivate(
                    ActionsProductsDeactivateRequest(
                        action_id=123456,
                        product_ids=[313455276]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/products/deactivate",
            payload=request.model_dump(),
        )
        return ActionsProductsDeactivateResponse(**response)
