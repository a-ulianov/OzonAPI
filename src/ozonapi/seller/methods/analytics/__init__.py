"""Композиция миксинов методов раздела Аналитические отчёты.

Объединяет аналитические методы продавца в единый класс :class:`SellerAnalyticsAPI`.
"""

from ...core import APIManager
from .analytics_stock_on_warehouses import AnalyticsStockOnWarehousesMixin
from .analytics_turnover_stocks import AnalyticsTurnoverStocksMixin


class SellerAnalyticsAPI(
    AnalyticsStockOnWarehousesMixin,
    AnalyticsTurnoverStocksMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Аналитические отчёты.

    Notes:
        • Объединяет методы отчёта по остаткам на складах и оборачиваемости товаров.

    References:
        • https://docs.ozon.ru/api/seller/#tag/AnalyticsAPI
    """

    pass
