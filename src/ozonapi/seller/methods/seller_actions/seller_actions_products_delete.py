from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsProductsDeleteRequest,
    SellerActionsProductsDeleteResponse,
)


class SellerActionsProductsDeleteMixin(APIManager):
    """Реализует метод /v1/seller-actions/products/delete"""

    async def seller_actions_products_delete(
            self: "SellerActionsProductsDeleteMixin",
            request: SellerActionsProductsDeleteRequest,
    ) -> SellerActionsProductsDeleteResponse:
        """Удаляет товары из акции продавца.

        Notes:
            • Товары идентифицируются по списку SKU `skus`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsDelete

        Args:
            request: Идентификатор акции и список SKU по схеме
                `SellerActionsProductsDeleteRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsProductsDeleteResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_products_delete(
                    SellerActionsProductsDeleteRequest(
                        action_id=123456, skus=["1234567890"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/delete",
            payload=request.model_dump(),
        )
        return SellerActionsProductsDeleteResponse(**response)
