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


class AnalyticsProductQueriesSortBy(str, Enum):
    """Поле сортировки в отчётах по запросам товаров (Premium).

    Attributes:
        BY_SEARCHES: по количеству поисковых запросов
        BY_VIEWS: по количеству показов
        BY_POSITION: по средней позиции
        BY_CONVERSION: по конверсии в просмотр
        BY_GMV: по обороту (GMV)
    """
    BY_SEARCHES = "BY_SEARCHES"
    BY_VIEWS = "BY_VIEWS"
    BY_POSITION = "BY_POSITION"
    BY_CONVERSION = "BY_CONVERSION"
    BY_GMV = "BY_GMV"


class AnalyticsProductQueriesSortDir(str, Enum):
    """Направление сортировки в отчётах по запросам товаров (Premium).

    Attributes:
        ASCENDING: по возрастанию
        DESCENDING: по убыванию
    """
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"
