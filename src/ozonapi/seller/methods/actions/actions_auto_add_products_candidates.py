from ...core import APIManager
from ...schemas.actions import (
    ActionsAutoAddProductsCandidatesRequest,
    ActionsAutoAddProductsCandidatesResponse,
)


class ActionsAutoAddProductsCandidatesMixin(APIManager):
    """Реализует метод /v1/actions/auto-add/products/candidates"""

    async def actions_auto_add_products_candidates(
            self: "ActionsAutoAddProductsCandidatesMixin",
            request: ActionsAutoAddProductsCandidatesRequest,
    ) -> ActionsAutoAddProductsCandidatesResponse:
        """Получает список доступных для автодобавления в акцию товаров.

        Notes:
            • Автодобавление автоматически включает товары в акцию Ozon на указанную дату.
            • Пагинация выполняется через `limit` и `offset`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionsAutoAddProductsCandidates

        Args:
            request: Идентификатор акции и параметры выборки по схеме
                `ActionsAutoAddProductsCandidatesRequest`

        Returns:
            Список доступных товаров по схеме `ActionsAutoAddProductsCandidatesResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_auto_add_products_candidates(
                    ActionsAutoAddProductsCandidatesRequest(action_id=123456, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/auto-add/products/candidates",
            payload=request.model_dump(),
        )
        return ActionsAutoAddProductsCandidatesResponse(**response)
