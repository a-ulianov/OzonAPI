from ...core import APIManager
from ...schemas.fbo import PostingFBOListRequest, PostingFBOListResponse


class PostingFBOListMixin(APIManager):
    """Реализует метод /v3/posting/fbo/list"""

    async def posting_fbo_list(
            self: "PostingFBOListMixin",
            request: PostingFBOListRequest
    ) -> PostingFBOListResponse:
        """Возвращает список отправлений FBO за указанный период времени (API v3).

        Notes:
            • Каноническая версия раздела (v2 — устаревшая `posting_fbo_list_v2()`).
            • Курсорная пагинация: если `has_next` равно true, передайте полученный
              `cursor` в следующий запрос.
            • Период задаётся полями `since` и `to_` в фильтре.
            • Дополнительные поля (аналитика, финансы, юр. информация) — через `with_`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFboList

        Args:
            request: Запрос по схеме `PostingFBOListRequest`

        Returns:
            Список отправлений FBO по схеме `PostingFBOListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbo_list(
                    PostingFBOListRequest(
                        limit=100,
                        filter={"since": "2026-05-01T00:00:00Z", "to": "2026-06-01T00:00:00Z"},
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="posting/fbo/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBOListResponse(**response)
