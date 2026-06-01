import pytest

from src.ozonapi.seller.schemas.search_queries import (
    SearchQueriesTopRequest,
    SearchQueriesTopResponse,
)


class TestSearchQueriesTop:
    """Тесты для метода search_queries_top."""

    @pytest.mark.asyncio
    async def test_search_queries_top(self, api, mock_api_request):
        """Тестирует метод search_queries_top."""

        mock_api_request.return_value = {
            "search_queries": [{"query": "наушники", "items_views": 9999.0}],
            "offset": "0",
            "total": "1",
        }

        request = SearchQueriesTopRequest(limit="50")

        response = await api.search_queries_top(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="search-queries/top",
            payload=request.model_dump(),
        )

        assert isinstance(response, SearchQueriesTopResponse)
        assert response.search_queries[0].query == "наушники"
