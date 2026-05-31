from ...core import APIManager
from ...schemas.actions import (
    ActionsCandidatesRequest,
    ActionsCandidatesResponse,
)


class ActionsCandidatesMixin(APIManager):
    """Реализует метод /v1/actions/candidates"""

    async def actions_candidates(
            self: "ActionsCandidatesMixin",
            request: ActionsCandidatesRequest,
    ) -> ActionsCandidatesResponse:
        """Получает список товаров, доступных для добавления в акцию.

        Notes:
            • Возвращает товары, которые можно добавить в указанную акцию (`action_id`).
            • Для каждого товара доступны текущая цена, цена по акции и максимальная цена по акции.
            • Для постраничной выборки используйте `limit` и `last_id` (или `offset`).
            • Список акций можно получить методом `actions()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ActionCandidates

        Args:
            request: Параметры выборки товаров по схеме `ActionsCandidatesRequest`

        Returns:
            Список доступных для акции товаров по схеме `ActionsCandidatesResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.actions_candidates(
                    ActionsCandidatesRequest(action_id=123456, limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="actions/candidates",
            payload=request.model_dump(),
        )
        return ActionsCandidatesResponse(**response)
