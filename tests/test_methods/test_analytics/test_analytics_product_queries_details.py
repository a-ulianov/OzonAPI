import pytest

from src.ozonapi.seller.schemas.analytics import (
    AnalyticsProductQueriesDetailsRequest,
    AnalyticsProductQueriesDetailsResponse,
)


class TestAnalyticsProductQueriesDetails:
    """Тесты для метода analytics_product_queries_details."""

    @pytest.mark.asyncio
    async def test_analytics_product_queries_details(self, api, mock_api_request):
        """Тестирует метод analytics_product_queries_details."""

        mock_api_request.return_value = {
            "analytics_period": {"date_from": "2026-05-01", "date_to": "2026-05-31"},
            "queries": [
                {"sku": 1234567890, "query": "чехол", "gmv": 1500.0, "order_count": 3}
            ],
            "page_count": 1,
            "total": 1,
        }

        request = AnalyticsProductQueriesDetailsRequest(
            date_from="2026-05-01T00:00:00Z",
            date_to="2026-05-31T23:59:59Z",
            skus=["1234567890"],
            limit_by_sku=10,
        )

        response = await api.analytics_product_queries_details(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="analytics/product-queries/details",
            payload=request.model_dump(),
        )

        assert isinstance(response, AnalyticsProductQueriesDetailsResponse)
        assert response.queries[0].query == "чехол"
        assert response.queries[0].order_count == 3
