"""Схемы раздела Аналитические отчёты."""
__all__ = [
    "AnalyticsStockOnWarehousesRequest",
    "AnalyticsStockOnWarehousesRow",
    "AnalyticsStockOnWarehousesResult",
    "AnalyticsStockOnWarehousesResponse",
    "AnalyticsTurnoverStocksRequest",
    "AnalyticsTurnoverStocksItem",
    "AnalyticsTurnoverStocksResponse",
    "AnalyticsDataFilter",
    "AnalyticsDataSorting",
    "AnalyticsDataRequest",
    "AnalyticsDataRowDimension",
    "AnalyticsDataRow",
    "AnalyticsDataResult",
    "AnalyticsDataResponse",
    "AnalyticsPeriod",
    "AnalyticsProductQueriesRequest",
    "AnalyticsProductQueriesItem",
    "AnalyticsProductQueriesResponse",
    "AnalyticsProductQueriesDetailsRequest",
    "AnalyticsProductQueriesDetailsQuery",
    "AnalyticsProductQueriesDetailsResponse",
]

from .v1__analytics_data import (
    AnalyticsDataFilter,
    AnalyticsDataRequest,
    AnalyticsDataResponse,
    AnalyticsDataResult,
    AnalyticsDataRow,
    AnalyticsDataRowDimension,
    AnalyticsDataSorting,
)
from .v1__analytics_product_queries import (
    AnalyticsPeriod,
    AnalyticsProductQueriesItem,
    AnalyticsProductQueriesRequest,
    AnalyticsProductQueriesResponse,
)
from .v1__analytics_product_queries_details import (
    AnalyticsProductQueriesDetailsQuery,
    AnalyticsProductQueriesDetailsRequest,
    AnalyticsProductQueriesDetailsResponse,
)
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
