from ...core import APIManager
from ...schemas.actions import (
    ActionsAutoAddProductsUpdateRequest,
    ActionsAutoAddProductsUpdateResponse,
)


class ActionsAutoAddProductsUpdateMixin(APIManager):
    """Реализует метод /v1/actions/auto-add/products/update"""

    async def actions_auto_add_products_update(
            self: "ActionsAutoAddProductsUpdateMixin",
            request: ActionsAutoAddProductsUpdateRequest,
    ) -> ActionsAutoAddProductsUpdateResponse:
        """Добавляет или обновляет товары в автодобавлении в акцию.

        Notes:
            • Для каждого товара укажите цену по акции `action_price`.
            • В ответе возвращаются успешно обработанные товары (`updated_ids`) и
              списки отклонённых: `rejected`, `below_min_price`, `extremely_low_price`,
              `failed_price`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsUpdate

        Args:
            request: Идентификатор акции и список товаров по схеме
                `ActionsAutoAddProductsUpdateRequest`

        Returns:
            Результат обработки товаров по схеме
            `ActionsAutoAddProductsUpdateResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_auto_add_products_update(
                    ActionsAutoAddProductsUpdateRequest(
                        action_id=123456,
                        to_update=[
                            ActionsAutoAddProductsUpdateProduct(
                                product_id=313455276, action_price=999.0
                            )
                        ],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/update",
            payload=request.model_dump(),
        )
        return ActionsAutoAddProductsUpdateResponse(**response)
