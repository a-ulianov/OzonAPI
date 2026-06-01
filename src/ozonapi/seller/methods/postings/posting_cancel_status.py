from ...core import APIManager
from ...schemas.postings import (
    PostingCancelStatusRequest,
    PostingCancelStatusResponse,
)


class PostingCancelStatusMixin(APIManager):
    """Реализует метод /v1/posting/cancel/status"""

    async def posting_cancel_status(
            self: "PostingCancelStatusMixin",
            request: PostingCancelStatusRequest
    ) -> PostingCancelStatusResponse:
        """Проверяет статус отмены отправления.

        Notes:
            • Используйте метод после `posting_cancel()`, чтобы узнать результат отмены.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingCancelStatus

        Args:
            request: Запрос статуса отмены по схеме `PostingCancelStatusRequest`

        Returns:
            Статус отмены отправления по схеме `PostingCancelStatusResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_cancel_status(
                    PostingCancelStatusRequest(posting_number="0001-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/cancel/status",
            payload=request.model_dump()
        )
        return PostingCancelStatusResponse(**response)
