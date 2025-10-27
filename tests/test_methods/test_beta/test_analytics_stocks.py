import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.common.enumerations.products import ItemTag, TurnoverGrade
from src.ozonapi.seller.methods import SellerBetaAPI
from src.ozonapi.seller.schemas.beta import (
    AnalyticsStocksRequest,
    AnalyticsStocksResponse,
)


class TestSellerBetaAPI:
    """Тесты для метода analytics_stocks."""

    @pytest.mark.asyncio
    async def test_analytics_stocks(self, api, mock_api_request):
        """Тестирует метод analytics_stocks."""
        mock_response_data = {
            "items": [
                {
                    "ads": 10.5,
                    "ads_cluster": 8.2,
                    "available_stock_count": 100,
                    "cluster_id": 1,
                    "cluster_name": "test_cluster",
                    "days_without_sales": 0,
                    "days_without_sales_cluster": 0,
                    "excess_stock_count": 5,
                    "expiring_stock_count": 2,
                    "idc": 15.3,
                    "idc_cluster": 12.7,
                    "item_tags": ["ITEM_ATTRIBUTE_NONE"],
                    "name": "Test Product",
                    "offer_id": "test_offer_123",
                    "other_stock_count": 3,
                    "requested_stock_count": 20,
                    "return_from_customer_stock_count": 1,
                    "return_to_seller_stock_count": 0,
                    "sku": 123456789,
                    "stock_defect_stock_count": 0,
                    "transit_defect_stock_count": 0,
                    "transit_stock_count": 15,
                    "turnover_grade": "DEFICIT",
                    "turnover_grade_cluster": "DEFICIT",
                    "valid_stock_count": 85,
                    "waiting_docs_stock_count": 2,
                    "warehouse_id": 101,
                    "warehouse_name": "Test Warehouse"
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = AnalyticsStocksRequest(
            skus=[123456789, 987654321],
            cluster_ids=[1, 2, 3],
            warehouse_ids=[101, 102],
            item_tags=[ItemTag.ITEM_ATTRIBUTE_NONE],
            turnover_grades=[TurnoverGrade.DEFICIT, TurnoverGrade.POPULAR],
        )
        response = await api.analytics_stocks(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="analytics/stocks",
            json=request.model_dump()
        )
        assert isinstance(response, AnalyticsStocksResponse)
        assert len(response.items) == 1
        assert response.items[0].sku == 123456789
        assert response.items[0].offer_id == "test_offer_123"
        assert response.items[0].name == "Test Product"
        assert response.items[0].available_stock_count == 100
        assert response.items[0].turnover_grade == "DEFICIT"