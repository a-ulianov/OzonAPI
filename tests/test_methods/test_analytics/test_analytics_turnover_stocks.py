import pytest

from src.ozonapi.seller.schemas.analytics import (
    AnalyticsTurnoverStocksRequest,
    AnalyticsTurnoverStocksResponse,
)


class TestAnalyticsTurnoverStocks:
    """Тесты для метода analytics_turnover_stocks."""

    @pytest.mark.asyncio
    async def test_analytics_turnover_stocks(self, api, mock_api_request):
        """Тестирует метод analytics_turnover_stocks."""

        mock_api_request.return_value = {
            "items": [
                {
                    "ads": 1.5,
                    "current_stock": 42,
                    "idc": 28.0,
                    "idc_grade": "GRADES_GREEN",
                    "name": "Товар",
                    "offer_id": "art-2",
                    "sku": 456,
                    "turnover": 30.0,
                    "turnover_grade": "GRADES_YELLOW",
                }
            ]
        }

        request = AnalyticsTurnoverStocksRequest(limit=100, offset=0, sku=["456"])

        response = await api.analytics_turnover_stocks(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="analytics/turnover/stocks",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, AnalyticsTurnoverStocksResponse)
        assert response.items[0].sku == 456
        assert response.items[0].idc_grade == "GRADES_GREEN"
        assert response.items[0].turnover_grade == "GRADES_YELLOW"
