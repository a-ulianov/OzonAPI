from ...core import APIManager
from ...schemas.search_queries import (
    SearchQueriesTopRequest,
    SearchQueriesTopResponse,
)


class SearchQueriesTopMixin(APIManager):
    """Реализует метод /v1/search-queries/top"""

    async def search_queries_top(
            self: "SearchQueriesTopMixin",
            request: SearchQueriesTopRequest = SearchQueriesTopRequest(),
    ) -> SearchQueriesTopResponse:
        """Получает список популярных поисковых запросов (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • `limit` и `offset` передаются строками (int64 в строковом виде).

        References:
            https://docs.ozon.ru/api/seller/#operation/SearchQueriesAPI_SearchQueriesTop

        Args:
            request: Параметры выборки по схеме `SearchQueriesTopRequest`

        Returns:
            Список популярных поисковых запросов по схеме `SearchQueriesTopResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.search_queries_top(
                    SearchQueriesTopRequest(limit="50")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="search-queries/top",
            payload=request.model_dump(),
        )
        return SearchQueriesTopResponse(**response)
