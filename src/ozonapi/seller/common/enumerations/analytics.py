from enum import Enum


class AnalyticsWarehouseType(str, Enum):
    """Фильтр по типу склада в отчёте по остаткам.

    Attributes:
        ALL: Все склады Ozon
        EXPRESS_DARK_STORE: Склады Ozon с доставкой Fresh
        NOT_EXPRESS_DARK_STORE: Склады Ozon без доставки Fresh
    """
    ALL = "ALL"
    EXPRESS_DARK_STORE = "EXPRESS_DARK_STORE"
    NOT_EXPRESS_DARK_STORE = "NOT_EXPRESS_DARK_STORE"
