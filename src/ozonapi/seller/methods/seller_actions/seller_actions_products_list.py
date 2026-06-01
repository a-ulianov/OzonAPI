from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsProductsListRequest,
    SellerActionsProductsListResponse,
)


class SellerActionsProductsListMixin(APIManager):
    """Реализует метод /v1/seller-actions/products/list"""

    async def seller_actions_products_list(
            self: "SellerActionsProductsListMixin",
            request: SellerActionsProductsListRequest,
    ) -> SellerActionsProductsListResponse:
        """Получает список участвующих в акции продавца товаров.

        Notes:
            • Метод использует курсорную пагинацию: передайте `cursor` из ответа
              для получения следующей страницы; `has_next` показывает наличие данных.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsList

        Args:
            request: Идентификатор акции и параметры пагинации по схеме
                `SellerActionsProductsListRequest`

        Returns:
            Список участвующих товаров по схеме `SellerActionsProductsListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_products_list(
                    SellerActionsProductsListRequest(action_id=123456, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/list",
            payload=request.model_dump(),
        )
        return SellerActionsProductsListResponse(**response)
