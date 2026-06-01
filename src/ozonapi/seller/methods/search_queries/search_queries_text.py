from ...core import APIManager
from ...schemas.search_queries import (
    SearchQueriesTextRequest,
    SearchQueriesTextResponse,
)


class SearchQueriesTextMixin(APIManager):
    """Реализует метод /v1/search-queries/text"""

    async def search_queries_text(
            self: "SearchQueriesTextMixin",
            request: SearchQueriesTextRequest = SearchQueriesTextRequest(),
    ) -> SearchQueriesTextResponse:
        """Получает список поисковых запросов по тексту (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • `limit` и `offset` передаются строками (int64 в строковом виде).
            • Возвращаются метрики по каждому запросу: показы, добавления в корзину,
              конверсия, средняя цена, число продавцов и уникальных пользователей.

        References:
            https://docs.ozon.ru/api/seller/#operation/SearchQueriesAPI_SearchQueriesText

        Args:
            request: Параметры поиска по схеме `SearchQueriesTextRequest`

        Returns:
            Список поисковых запросов по схеме `SearchQueriesTextResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.search_queries_text(
                    SearchQueriesTextRequest(text="чехол", limit="50")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="search-queries/text",
            payload=request.model_dump(),
        )
        return SearchQueriesTextResponse(**response)
