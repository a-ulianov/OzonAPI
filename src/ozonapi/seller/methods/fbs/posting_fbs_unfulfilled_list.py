from ...core import APIManager
from ...schemas.fbs import (
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse,
)


class PostingFBSUnfulfilledListMixin(APIManager):
    """Реализует метод /v4/posting/fbs/unfulfilled/list"""

    async def posting_fbs_unfulfilled_list(
            self: "PostingFBSUnfulfilledListMixin",
            request: PostingFBSUnfulfilledListRequest = PostingFBSUnfulfilledListRequest()
    ) -> PostingFBSUnfulfilledListResponse:
        """Возвращает список необработанных отправлений FBS (актуальная версия 4).

        Notes:
            • Поле `filter` обязательно — сервер отклоняет запрос без него.
            • Курсорная пагинация: при `has_next` равном true передайте полученный
              `cursor` в следующий запрос.
            • Устаревшая версия 3 доступна как `posting_fbs_unfulfilled_list_v3()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingFbsUnfulfilledList

        Args:
            request: Запрос по схеме `PostingFBSUnfulfilledListRequest`

        Returns:
            Список необработанных отправлений по схеме `PostingFBSUnfulfilledListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_unfulfilled_list(
                    PostingFBSUnfulfilledListRequest(limit=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/unfulfilled/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSUnfulfilledListResponse(**response)
