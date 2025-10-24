from async_lru import alru_cache

from ...core import APIManager
from ...schemas.fbs import PostingFBSCancelReasonListResponse


class PostingFBSCancelReasonListMixin(APIManager):
    """Реализует метод v2/posting/fbs/cancel-reason/list"""

    @alru_cache(ttl=86400)
    async def posting_fbs_cancel_reason_list(
        self: "PostingFBSCancelReasonListMixin",
    ) -> PostingFBSCancelReasonListResponse:
        """Метод для получения списка причин отмены для всех отправлений.

        Notes:
            • Метод возвращает полный список доступных причин отмены отправлений.
            • Каждая причина содержит информацию о доступности для отмены и инициаторе отмены.
            • Инициатором отмены может быть как продавец (seller), так и покупатель (buyer).
            • Поле `is_available_for_cancellation` указывает, доступна ли причина для использования при отмене отправления.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetPostingFbsCancelReasonList

        Returns:
            Список доступных причин отмены отправлений по схеме `PostingFBSCancelReasonListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_cancel_reason_list()
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/cancel-reason/list",
        )
        return PostingFBSCancelReasonListResponse(**response)