from ...core import APIManager
from ...schemas.returns import (
    ReturnsRfbsActionSetRequest,
    ReturnsRfbsActionSetResponse,
)


class ReturnsRfbsActionSetMixin(APIManager):
    """Реализует метод /v1/returns/rfbs/action/set"""

    async def returns_rfbs_action_set(
            self: "ReturnsRfbsActionSetMixin",
            request: ReturnsRfbsActionSetRequest
    ) -> ReturnsRfbsActionSetResponse:
        """Метод для передачи доступных действий для rFBS возвратов.

        Notes:
            • Выполняет указанное действие с заявкой на возврат (одобрение, отклонение,
              компенсация, возврат денег и т.д.) по идентификатору действия `id`.
            • Идентификаторы доступных действий возвращает метод `returns_rfbs_get()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsActionSet

        Args:
            request: Запрос на выполнение действия по схеме `ReturnsRfbsActionSetRequest`

        Returns:
            Результат выполнения действия по схеме `ReturnsRfbsActionSetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_action_set(
                    ReturnsRfbsActionSetRequest(
                        return_id=12345,
                        id=1
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="returns/rfbs/action/set",
            payload=request.model_dump()
        )
        return ReturnsRfbsActionSetResponse(**response)
