from ...core import APIManager
from ...schemas.fbs import PostingFBSListRequest, PostingFBSListResponse


class PostingFBSListMixin(APIManager):
    """Реализует метод /v4/posting/fbs/list"""

    async def posting_fbs_list(
            self: "PostingFBSListMixin",
            request: PostingFBSListRequest = PostingFBSListRequest()
    ) -> PostingFBSListResponse:
        """Возвращает список отправлений FBS за указанный период (актуальная версия 4).

        Notes:
            • Курсорная пагинация: при `has_next` равном true передайте полученный
              `cursor` в следующий запрос.
            • Период задаётся в `filter.since` / `filter.to`.
            • Устаревшая версия 3 доступна как `posting_fbs_list_v3()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingFbsList

        Args:
            request: Запрос списка отправлений по схеме `PostingFBSListRequest`

        Returns:
            Список отправлений FBS по схеме `PostingFBSListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_list(
                    PostingFBSListRequest(
                        filter=PostingFBSListFilter(
                            since="2026-05-01T00:00:00Z", to="2026-06-01T00:00:00Z"
                        ),
                        limit=100,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSListResponse(**response)
