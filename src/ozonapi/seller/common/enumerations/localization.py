from enum import Enum


class CurrencyCode(str, Enum):
    """Валюты цен.

    Attributes:
        RUB: Российский рубль
        BYN: Белорусский рубль
        KZT: Казахстанский тенге
        EUR: Евро
        USD: Доллар США
        CNY: Китайский юань
        UNSPECIFIED: Не указана
    """
    RUB = "RUB"
    BYN = "BYN"
    KZT = "KZT"
    EUR = "EUR"
    USD = "USD"
    CNY = "CNY"
    UNSPECIFIED = ""


class Language(str, Enum):
    """Языки.

    Attributes:
        EN: английский
        RU: русский
        TR: турецкий
        ZH_HANS: китайский
        DEFAULT: по умолчанию
    """
    EN = "EN"
    RU = "RU"
    TR = "TR"
    ZH_HANS = "ZH_HANS"
    DEFAULT = "DEFAULT"