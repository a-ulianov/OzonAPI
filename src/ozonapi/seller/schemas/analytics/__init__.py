"""Схемы раздела Аналитические отчёты."""
__all__ = [
    "AnalyticsStockOnWarehousesRequest",
    "AnalyticsStockOnWarehousesRow",
    "AnalyticsStockOnWarehousesResult",
    "AnalyticsStockOnWarehousesResponse",
    "AnalyticsTurnoverStocksRequest",
    "AnalyticsTurnoverStocksItem",
    "AnalyticsTurnoverStocksResponse",
]

from .v1__analytics_turnover_stocks import (
    AnalyticsTurnoverStocksItem,
    AnalyticsTurnoverStocksRequest,
    AnalyticsTurnoverStocksResponse,
)
from .v2__analytics_stock_on_warehouses import (
    AnalyticsStockOnWarehousesRequest,
    AnalyticsStockOnWarehousesResponse,
    AnalyticsStockOnWarehousesResult,
    AnalyticsStockOnWarehousesRow,
)
