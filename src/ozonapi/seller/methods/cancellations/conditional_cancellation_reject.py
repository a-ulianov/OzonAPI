from ...core import APIManager
from ...schemas.cancellations import (
    ConditionalCancellationRejectRequest,
    ConditionalCancellationRejectResponse,
)


class ConditionalCancellationRejectMixin(APIManager):
    """Реализует метод /v2/conditional-cancellation/reject"""

    async def conditional_cancellation_reject(
            self: "ConditionalCancellationRejectMixin",
            request: ConditionalCancellationRejectRequest
    ) -> ConditionalCancellationRejectResponse:
        """Отклоняет заявку на отмену отправления rFBS.

        Notes:
            • Отклоняйте заявку, если успели передать отправление в доставку.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/CancellationAPI_ConditionalCancellationRejectV2

        Args:
            request: Запрос по схеме `ConditionalCancellationRejectRequest`

        Returns:
            Пустой ответ по схеме `ConditionalCancellationRejectResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.conditional_cancellation_reject(
                    ConditionalCancellationRejectRequest(cancellation_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="conditional-cancellation/reject",
            payload=request.model_dump()
        )
        return ConditionalCancellationRejectResponse(**response)
