from ...core import APIManager
from ...schemas.fbs import PostingFBSCancelRequest, PostingFBSCancelResponse


class PostingFBSCancelMixin(APIManager):
    """Реализует метод /v2/posting/fbs/cancel"""

    async def posting_fbs_cancel(
            self: "PostingFBSCancelMixin",
            request: PostingFBSCancelRequest
    ) -> PostingFBSCancelResponse:
        """Метод для отмены отправления FBS/rFBS.

        Notes:
            • Меняет статус отправления на `cancelled`.
            • Перед началом работы проверьте причины отмены для конкретного отправления методом `/v1/posting/fbs/cancel-reason`.
            • Условно-доставленные отправления отменить нельзя.
            • Если значение параметра `cancel_reason_id` — 402, заполните поле `cancel_reason_message`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_CancelFbsPosting

        Args:
            request: Запрос на отмену отправления по схеме `PostingFBSCancelRequest`

        Returns:
            Результат обработки запроса по схеме `PostingFBSCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_cancel(
                    PostingFBSCancelRequest(
                        cancel_reason_id=352,
                        cancel_reason_message="Product is out of stock",
                        posting_number="33920113-1231-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/cancel",
            payload=request.model_dump()
        )
        return PostingFBSCancelResponse(**response)