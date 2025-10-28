from ...core import APIManager
from ...schemas.fbs import PostingFBSCancelReasonRequest, PostingFBSCancelReasonResponse


class PostingFBSCancelReasonMixin(APIManager):
    """Реализует метод /v1/posting/fbs/cancel-reason"""

    async def posting_fbs_cancel_reason(
            self: "PostingFBSCancelReasonMixin",
            request: PostingFBSCancelReasonRequest
    ) -> PostingFBSCancelReasonResponse:
        """Метод для получения списка причин отмены для конкретных отправлений FBS.

        Notes:
            • Возвращает список причин отмены для указанных номеров отправлений.
            • Каждое отправление может иметь несколько возможных причин отмены.
            • Причины отмены различаются по инициатору (покупатель или продавец).

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetPostingFbsCancelReasonV1

        Args:
            request: Запрос на получение причин отмены отправлений по схеме `PostingFBSCancelReasonRequest`

        Returns:
            Список причин отмены для указанных отправлений по схеме `PostingFBSCancelReasonResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_cancel_reason(
                    PostingFBSCancelReasonRequest(
                        related_posting_numbers=["73837363-0010-3", ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/cancel-reason",
            payload=request.model_dump()
        )
        return PostingFBSCancelReasonResponse(**response)