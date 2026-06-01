from ...core import APIManager
from ...schemas.actions import (
    ActionsAutoAddProductsDeleteRequest,
    ActionsAutoAddProductsDeleteResponse,
)


class ActionsAutoAddProductsDeleteMixin(APIManager):
    """Реализует метод /v1/actions/auto-add/products/delete"""

    async def actions_auto_add_products_delete(
            self: "ActionsAutoAddProductsDeleteMixin",
            request: ActionsAutoAddProductsDeleteRequest,
    ) -> ActionsAutoAddProductsDeleteResponse:
        """Удаляет товары из автодобавления в акцию.

        Notes:
            • Товары идентифицируются по списку `product_ids`.
            • В ответе возвращаются идентификаторы удалённых товаров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsDelete

        Args:
            request: Идентификатор акции и список товаров по схеме
                `ActionsAutoAddProductsDeleteRequest`

        Returns:
            Идентификаторы удалённых товаров по схеме
            `ActionsAutoAddProductsDeleteResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_auto_add_products_delete(
                    ActionsAutoAddProductsDeleteRequest(
                        action_id=123456, product_ids=["313455276"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/delete",
            payload=request.model_dump(),
        )
        return ActionsAutoAddProductsDeleteResponse(**response)
