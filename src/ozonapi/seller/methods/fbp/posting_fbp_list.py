from ...core import APIManager
from ...schemas.fbp import PostingFbpListRequest, PostingFbpListResponse


class PostingFbpListMixin(APIManager):
    """Реализует метод /v1/posting/fbp/list"""

    async def posting_fbp_list(
            self: "PostingFbpListMixin",
            request: PostingFbpListRequest,
    ) -> PostingFbpListResponse:
        """Получает список отправлений FBP.

        Notes:
            • Использует курсорную пагинацию (`cursor`/`limit`).
            • Поддерживает фильтрацию по периоду, статусам и товарам.
            • Даты периода `filter.since`/`filter.to` передаются строками RFC3339.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_PostingFbpList

        Args:
            request: Параметры выборки по схеме `PostingFbpListRequest`

        Returns:
            Список отправлений по схеме `PostingFbpListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbp_list(
                    PostingFbpListRequest(
                        filter=PostingFbpListFilter(
                            since="2026-06-01T00:00:00Z",
                            to="2026-06-30T00:00:00Z",
                        ),
                        limit=100,
                    )
                )

            for posting in result.postings:
                print(posting.posting_number, posting.status)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbp/list",
            payload=request.model_dump(),
        )
        return PostingFbpListResponse(**response)
