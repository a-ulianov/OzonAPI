from enum import Enum


class ProductsSortingBy(str, Enum):
    """Поле сортировки.

    Attributes:
        SKU: По SKU
        OFFER_ID: По артикулу
        ID: По ID
        TITLE: По названию
    """
    SKU = "sku"
    OFFER_ID = "offer_id"
    ID = "id"
    TITLE = "title"

class SortingDirection(str, Enum):
    """Направление сортировки.

    Attributes:
        ASC: По возрастанию
        DESC: По убыванию
    """
    ASC = "asc"
    DESC = "desc"