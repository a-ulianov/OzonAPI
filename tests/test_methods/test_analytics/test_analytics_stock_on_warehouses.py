import pytest

from src.ozonapi.seller.common.enumerations.analytics import AnalyticsWarehouseType
from src.ozonapi.seller.schemas.analytics import (
    AnalyticsStockOnWarehousesRequest,
    AnalyticsStockOnWarehousesResponse,
)


class TestAnalyticsStockOnWarehouses:
    """Тесты для метода analytics_stock_on_warehouses."""

    @pytest.mark.asyncio
    async def test_analytics_stock_on_warehouses(self, api, mock_api_request):
        """Тестирует метод analytics_stock_on_warehouses."""

        mock_api_request.return_value = {
            "result": {
                "rows": [
                    {
                        "sku": 123,
                        "item_code": "art-1",
                        "item_name": "Товар",
                        "free_to_sell_amount": 10,
                        "promised_amount": 2,
                        "reserved_amount": 1,
                        "warehouse_name": "Склад",
                    }
                ]
            }
        }

        request = AnalyticsStockOnWarehousesRequest(
            limit=100, offset=0, warehouse_type=AnalyticsWarehouseType.ALL
        )

        response = await api.analytics_stock_on_warehouses(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="analytics/stock_on_warehouses",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, AnalyticsStockOnWarehousesResponse)
        assert response.result.rows[0].sku == 123
        assert response.result.rows[0].free_to_sell_amount == 10
