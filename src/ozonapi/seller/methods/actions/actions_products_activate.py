from ...core import APIManager
from ...schemas.actions import (
    ActionsProductsActivateRequest,
    ActionsProductsActivateResponse,
)


class ActionsProductsActivateMixin(APIManager):
    """Реализует метод /v1/actions/products/activate"""

    async def actions_products_activate(
            self: "ActionsProductsActivateMixin",
            request: ActionsProductsActivateRequest,
    ) -> ActionsProductsActivateResponse:
        """Добавляет товары в акцию.

        Notes:
            • Для каждого товара укажите цену по акции (`action_price`).
            • Доступные для акции товары можно получить методом `actions_candidates()`.
            • В ответе возвращаются идентификаторы добавленных товаров и список отклонённых
              с причинами.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsProductsActivate

        Args:
            request: Идентификатор акции и список товаров по схеме `ActionsProductsActivateRequest`

        Returns:
            Результат добавления товаров в акцию по схеме `ActionsProductsActivateResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_products_activate(
                    ActionsProductsActivateRequest(
                        action_id=123456,
                        products=[
                            ActionsProductsActivateProduct(product_id=313455276, action_price=999.0)
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/products/activate",
            payload=request.model_dump(),
        )
        return ActionsProductsActivateResponse(**response)
