from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsProductsAddRequest,
    SellerActionsProductsAddResponse,
)


class SellerActionsProductsAddMixin(APIManager):
    """Реализует метод /v1/seller-actions/products/add"""

    async def seller_actions_products_add(
            self: "SellerActionsProductsAddMixin",
            request: SellerActionsProductsAddRequest,
    ) -> SellerActionsProductsAddResponse:
        """Добавляет товары в акцию продавца.

        Notes:
            • Доступные для акции товары можно получить методом
              `seller_actions_products_candidates()`.
            • Для каждого товара укажите процент скидки `discount_percent` и валюту.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsAdd

        Args:
            request: Идентификатор акции и список товаров по схеме
                `SellerActionsProductsAddRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsProductsAddResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_products_add(
                    SellerActionsProductsAddRequest(
                        action_id=123456,
                        products=[
                            SellerActionsProductsAddProduct(
                                sku=1234567890, discount_percent=10.0, currency="RUB"
                            )
                        ],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/add",
            payload=request.model_dump(),
        )
        return SellerActionsProductsAddResponse(**response)
