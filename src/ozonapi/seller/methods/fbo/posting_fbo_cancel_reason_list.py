from async_lru import alru_cache

from ...core import APIManager
from ...schemas.fbo import PostingFBOCancelReasonListResponse


class PostingFBOCancelReasonListMixin(APIManager):
    """Реализует метод v1/posting/fbo/cancel-reason/list"""

    @alru_cache(ttl=86400)
    async def posting_fbo_cancel_reason_list(
        self: "PostingFBOCancelReasonListMixin",
    ) -> PostingFBOCancelReasonListResponse:
        """Метод для получения списка причин отмены для всех отправлений.

        Notes:
            • Метод возвращает полный список доступных причин отмены отправлений.
            • Каждая причина содержит информацию о доступности для отмены и инициаторе отмены.
            • Инициатором отмены может быть как продавец (seller), так и покупатель (buyer).
            • Поле `is_available_for_cancellation` указывает, доступна ли причина для использования при отмене отправления.

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_GetPostingFboCancelReasonList

        Returns:
            Список доступных причин отмены отправлений по схеме `PostingFBOCancelReasonListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbo_cancel_reason_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbo/cancel-reason/list",
        )
        return PostingFBOCancelReasonListResponse(**response)