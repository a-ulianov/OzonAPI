"""Описывает модели бета-методов.
https://docs.ozon.com/api/seller/?#tag/BetaMethod
"""

__all__ = [
    "AnalyticsStocksRequest",
    "AnalyticsStocksResponse",
    "AnalyticsStocksItem",
]

from .v1__analytics_stocks import AnalyticsStocksResponse, AnalyticsStocksRequest, AnalyticsStocksItem