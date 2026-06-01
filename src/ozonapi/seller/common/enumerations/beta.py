from enum import Enum


class DiscountTaskStatus(str, Enum):
    """Статус заявки на скидку (фильтр запроса списка заявок).

    Attributes:
        ALL: Все заявки
        NEW: Новые
        APPROVED: Одобренные
        DECLINED: Отклонённые
    """
    ALL = "ALL"
    NEW = "NEW"
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"


class ProductPlacement(str, Enum):
    """Витрина размещения товара.

    Attributes:
        OZON: Витрина Ozon
        SELECT: Витрина Ozon Селект
        OZON_SELECT: Витрины Ozon и Ozon Селект
        NONE: Не размещать
    """
    OZON = "OZON"
    SELECT = "SELECT"
    OZON_SELECT = "OZON_SELECT"
    NONE = "NONE"
