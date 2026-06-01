import pytest

from src.ozonapi.seller.schemas.analytics import (
    AnalyticsProductQueriesRequest,
    AnalyticsProductQueriesResponse,
)


class TestAnalyticsProductQueries:
    """Тесты для метода analytics_product_queries."""

    @pytest.mark.asyncio
    async def test_analytics_product_queries(self, api, mock_api_request):
        """Тестирует метод analytics_product_queries."""

        mock_api_request.return_value = {
            "analytics_period": {"date_from": "2026-05-01", "date_to": "2026-05-31"},
            "items": [
                {"sku": 1234567890, "name": "Товар", "gmv": 5000.0, "position": 3.5}
            ],
            "page_count": 1,
            "total": 1,
        }

        request = AnalyticsProductQueriesRequest(
            date_from="2026-05-01T00:00:00Z",
            date_to="2026-05-31T23:59:59Z",
            skus=["1234567890"],
            page=1,
            page_size=50,
        )

        response = await api.analytics_product_queries(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="analytics/product-queries",
            payload=request.model_dump(),
        )

        assert isinstance(response, AnalyticsProductQueriesResponse)
        assert response.total == 1
        assert response.items[0].sku == 1234567890
        assert response.analytics_period.date_from == "2026-05-01"
