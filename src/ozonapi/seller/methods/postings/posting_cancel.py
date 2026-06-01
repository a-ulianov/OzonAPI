from ...core import APIManager
from ...schemas.postings import (
    PostingCancelRequest,
    PostingCancelResponse,
)


class PostingCancelMixin(APIManager):
    """Реализует метод /v1/posting/cancel"""

    async def posting_cancel(
            self: "PostingCancelMixin",
            request: PostingCancelRequest
    ) -> PostingCancelResponse:
        """Отменяет отправление из заказа.

        Notes:
            • Отменить можно только отправления в статусе `awaiting_deliver`.
            • Список доступных причин отмены `reason_id` возвращает метод
              `posting_fbs_cancel_reason_list()`.
            • Если `reason_id` равен 402, поле `reason_message` обязательно.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingCancel

        Args:
            request: Запрос на отмену отправления по схеме `PostingCancelRequest`

        Returns:
            Результат отмены отправления по схеме `PostingCancelResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_cancel(
                    PostingCancelRequest(
                        posting_number="0001-1",
                        reason_id=402,
                        reason_message="Нет товара на складе"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/cancel",
            payload=request.model_dump()
        )
        return PostingCancelResponse(**response)
