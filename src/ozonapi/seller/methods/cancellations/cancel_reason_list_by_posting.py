from ...core import APIManager
from ...schemas.cancellations import (
    CancelReasonListByPostingRequest,
    CancelReasonListByPostingResponse,
)


class CancelReasonListByPostingMixin(APIManager):
    """Реализует метод /v1/cancel-reason/list-by-posting"""

    async def cancel_reason_list_by_posting(
            self: "CancelReasonListByPostingMixin",
            request: CancelReasonListByPostingRequest,
    ) -> CancelReasonListByPostingResponse:
        """Получает динамический список причин отмены для отправления из заказа.

        Notes:
            • Возвращает причины отмены, доступные для конкретного отправления.

        References:
            https://docs.ozon.ru/api/seller/#operation/CancelReasonAPI_CancelReasonListByPosting

        Args:
            request: Номер отправления по схеме `CancelReasonListByPostingRequest`

        Returns:
            Список причин отмены по схеме `CancelReasonListByPostingResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cancel_reason_list_by_posting(
                    CancelReasonListByPostingRequest(
                        posting_number="0001-1234567-0000001"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cancel-reason/list-by-posting",
            payload=request.model_dump(),
        )
        return CancelReasonListByPostingResponse(**response)
