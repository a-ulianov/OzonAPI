from enum import Enum


class VAT(str, Enum):
    """Ставка НДС для товара.

    Attributes:
        PERCENT_0: НДС не облагается
        PERCENT_5: НДС 5%
        PERCENT_7: НДС 7%
        PERCENT_10: НДС 10%
        PERCENT_20: НДС 20%
        PERCENT_22: НДС 22%
    """
    PERCENT_0 = "0"
    PERCENT_5 = "0.05"
    PERCENT_7 = "0.07"
    PERCENT_10 = "0.10"
    PERCENT_20 = "0.20"
    PERCENT_22 = "0.22"


class PromotionType(str, Enum):
    """Типы акций.

    Attributes:
        REVIEWS_PROMO: баллы за отзывы
    """
    REVIEWS_PROMO = "REVIEWS_PROMO"


class PromotionOperation(str, Enum):
    """Действия с акцией.

    Attributes:
        ENABLE: включить
        DISABLE: выключить
        UNKNOWN: ничего не менять
    """
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
    UNKNOWN = "UNKNOWN"


class PricingStrategy(str, Enum):
    """Акционные стратегии.

    Attributes:
        ENABLED: включить
        DISABLED: выключить
        UNKNOWN: ничего не менять
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
    UNKNOWN = "UNKNOWN"


class ColorIndex(str, Enum):
    """Итоговый индекс цены товара.

    Attributes:
        UNSPECIFIED: не определен
        WITHOUT_INDEX: нет индекса
        GREEN: выгодный
        YELLOW: умеренный
        RED: невыгодный
        SUPER: супер-индекс (не указано значение в документации)
    """
    UNSPECIFIED = "COLOR_INDEX_UNSPECIFIED"
    WITHOUT_INDEX = "WITHOUT_INDEX"
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"
    SUPER = "SUPER"


class ColorIndexWithPrefix(str, Enum):
    """Итоговый индекс цены товара.

    Attributes:
        UNSPECIFIED: не определен
        WITHOUT_INDEX: нет индекса
        GREEN: выгодный
        YELLOW: умеренный
        RED: невыгодный
        SUPER: супер-индекс (не указано значение в документации)
    """
    UNSPECIFIED = "COLOR_INDEX_UNSPECIFIED"
    WITHOUT_INDEX = "COLOR_INDEX_WITHOUT_INDEX"
    GREEN = "COLOR_INDEX_GREEN"
    YELLOW = "COLOR_INDEX_YELLOW"
    RED = "COLOR_INDEX_RED"
    SUPER = "COLOR_INDEX_SUPER"
