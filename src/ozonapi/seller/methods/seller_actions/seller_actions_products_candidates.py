from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsProductsCandidatesRequest,
    SellerActionsProductsCandidatesResponse,
)


class SellerActionsProductsCandidatesMixin(APIManager):
    """Реализует метод /v1/seller-actions/products/candidates"""

    async def seller_actions_products_candidates(
            self: "SellerActionsProductsCandidatesMixin",
            request: SellerActionsProductsCandidatesRequest,
    ) -> SellerActionsProductsCandidatesResponse:
        """Получает список доступных для акции продавца товаров.

        Notes:
            • Метод использует курсорную пагинацию: передайте `cursor` из ответа
              для получения следующей страницы; `has_next` показывает наличие данных.
            • Добавить товары в акцию можно методом `seller_actions_products_add()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsProductsCandidates

        Args:
            request: Идентификатор акции и параметры пагинации по схеме
                `SellerActionsProductsCandidatesRequest`

        Returns:
            Список доступных товаров по схеме `SellerActionsProductsCandidatesResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_products_candidates(
                    SellerActionsProductsCandidatesRequest(action_id=123456, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/products/candidates",
            payload=request.model_dump(),
        )
        return SellerActionsProductsCandidatesResponse(**response)
