from ...core import APIManager
from ...schemas.cancellations import (
    ConditionalCancellationListRequest,
    ConditionalCancellationListResponse,
)


class ConditionalCancellationListMixin(APIManager):
    """Реализует метод /v2/conditional-cancellation/list"""

    async def conditional_cancellation_list(
            self: "ConditionalCancellationListMixin",
            request: ConditionalCancellationListRequest
    ) -> ConditionalCancellationListResponse:
        """Возвращает список заявок на отмену отправлений rFBS.

        Notes:
            • Пагинация по `last_id`: передайте полученный `last_id` в следующий запрос.
            • Чтобы получить счётчики заявок по статусам, передайте `with.counter = true`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CancellationAPI_GetConditionalCancellationListV2

        Args:
            request: Запрос по схеме `ConditionalCancellationListRequest`

        Returns:
            Список заявок на отмену по схеме `ConditionalCancellationListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.conditional_cancellation_list(
                    ConditionalCancellationListRequest(limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="conditional-cancellation/list",
            payload=request.model_dump(by_alias=True)
        )
        return ConditionalCancellationListResponse(**response)
