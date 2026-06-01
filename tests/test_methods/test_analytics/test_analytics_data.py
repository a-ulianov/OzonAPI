import pytest

from src.ozonapi.seller.schemas.analytics import (
    AnalyticsDataRequest,
    AnalyticsDataResponse,
)


class TestAnalyticsData:
    """Тесты для метода analytics_data."""

    @pytest.mark.asyncio
    async def test_analytics_data(self, api, mock_api_request):
        """Тестирует метод analytics_data."""

        mock_api_request.return_value = {
            "result": {
                "data": [
                    {
                        "dimensions": [{"id": "1234567890", "name": "Товар"}],
                        "metrics": [1000.0, 5.0],
                    }
                ],
                "totals": [1000.0, 5.0],
            },
            "timestamp": "2026-06-01T00:00:00Z",
        }

        request = AnalyticsDataRequest(
            date_from="2026-05-01",
            date_to="2026-05-31",
            dimension=["sku"],
            metrics=["revenue", "ordered_units"],
            limit=100,
        )

        response = await api.analytics_data(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="analytics/data",
            payload=request.model_dump(),
        )

        assert isinstance(response, AnalyticsDataResponse)
        assert response.result.data[0].dimensions[0].name == "Товар"
        assert response.result.data[0].metrics == [1000.0, 5.0]
        assert response.result.totals == [1000.0, 5.0]
