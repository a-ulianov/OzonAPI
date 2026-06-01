from ...core import APIManager
from ...schemas.beta import PostingDigitalListRequest, PostingDigitalListResponse


class PostingDigitalListMixin(APIManager):
    """Реализует метод /v2/posting/digital/list"""

    async def posting_digital_list(
            self: "PostingDigitalListMixin",
            request: PostingDigitalListRequest
    ) -> PostingDigitalListResponse:
        """Возвращает список отправлений с цифровыми товарами.

        Notes:
            • Курсорная пагинация: если `has_next` равно true, передайте полученный
              `cursor` в следующий запрос.
            • Период задаётся полями `since` и `to_` в фильтре.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingDigitalList

        Args:
            request: Запрос по схеме `PostingDigitalListRequest`

        Returns:
            Список цифровых отправлений по схеме `PostingDigitalListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_digital_list(
                    PostingDigitalListRequest(
                        limit=100,
                        filter={"since": "2026-05-01T00:00:00Z", "to": "2026-06-01T00:00:00Z"},
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/digital/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingDigitalListResponse(**response)
