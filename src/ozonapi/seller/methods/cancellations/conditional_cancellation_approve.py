from ...core import APIManager
from ...schemas.cancellations import (
    ConditionalCancellationApproveRequest,
    ConditionalCancellationApproveResponse,
)


class ConditionalCancellationApproveMixin(APIManager):
    """Реализует метод /v2/conditional-cancellation/approve"""

    async def conditional_cancellation_approve(
            self: "ConditionalCancellationApproveMixin",
            request: ConditionalCancellationApproveRequest
    ) -> ConditionalCancellationApproveResponse:
        """Подтверждает заявку на отмену отправления rFBS.

        Notes:
            • Подтверждение отменяет отправление; вернуть его в работу нельзя.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/CancellationAPI_ConditionalCancellationApproveV2

        Args:
            request: Запрос по схеме `ConditionalCancellationApproveRequest`

        Returns:
            Пустой ответ по схеме `ConditionalCancellationApproveResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.conditional_cancellation_approve(
                    ConditionalCancellationApproveRequest(cancellation_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="conditional-cancellation/approve",
            payload=request.model_dump()
        )
        return ConditionalCancellationApproveResponse(**response)
