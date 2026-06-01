import pytest

from src.ozonapi.seller.schemas.search_queries import (
    SearchQueriesTextRequest,
    SearchQueriesTextResponse,
)


class TestSearchQueriesText:
    """Тесты для метода search_queries_text."""

    @pytest.mark.asyncio
    async def test_search_queries_text(self, api, mock_api_request):
        """Тестирует метод search_queries_text."""

        mock_api_request.return_value = {
            "search_queries": [
                {"query": "чехол", "client_count": 100.0, "avg_price": 500.0}
            ],
            "offset": "0",
            "total": "1",
        }

        request = SearchQueriesTextRequest(text="чехол", limit="50")

        response = await api.search_queries_text(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="search-queries/text",
            payload=request.model_dump(),
        )

        assert isinstance(response, SearchQueriesTextResponse)
        assert response.total == "1"
        assert response.search_queries[0].query == "чехол"
