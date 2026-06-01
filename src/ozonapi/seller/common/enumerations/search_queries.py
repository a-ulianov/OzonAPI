from enum import Enum


class SearchQueriesSortBy(str, Enum):
    """Поле сортировки списка поисковых запросов по тексту.

    Attributes:
        CLIENT_COUNT: по количеству уникальных пользователей
        ADD_TO_CART: по количеству добавлений в корзину
        CONVERSION_TO_CART: по конверсии в корзину
        AVG_PRICE: по средней цене
    """
    CLIENT_COUNT = "CLIENT_COUNT"
    ADD_TO_CART = "ADD_TO_CART"
    CONVERSION_TO_CART = "CONVERSION_TO_CART"
    AVG_PRICE = "AVG_PRICE"


class SearchQueriesSortDir(str, Enum):
    """Направление сортировки списка поисковых запросов.

    Attributes:
        ASC: по возрастанию
        DESC: по убыванию
    """
    ASC = "ASC"
    DESC = "DESC"
