import pytest

from src.ozonapi.seller.schemas.beta import (
    AnalyticsManageStocksRequest,
    AnalyticsManageStocksResponse,
)


class TestAnalyticsManageStocks:
    """Тесты для метода analytics_manage_stocks."""

    @pytest.mark.asyncio
    async def test_analytics_manage_stocks(self, api, mock_api_request):
        """Тестирует метод analytics_manage_stocks."""

        mock_api_request.return_value = {
            "items": [
                {
                    "defect_stock_count": 1,
                    "expiring_stock_count": 2,
                    "name": "Товар",
                    "offer_id": "art-1",
                    "sku": 222,
                    "valid_stock_count": 10,
                    "waitingdocs_stock_count": 0,
                    "warehouse_name": "Склад",
                }
            ]
        }

        request = AnalyticsManageStocksRequest(
            filter={"skus": ["222"]}, limit=100, offset=0
        )

        response = await api.analytics_manage_stocks(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="analytics/manage/stocks",
            payload=request.model_dump()
        )

        assert isinstance(response, AnalyticsManageStocksResponse)
        assert response.items[0].sku == 222
        assert response.items[0].valid_stock_count == 10
