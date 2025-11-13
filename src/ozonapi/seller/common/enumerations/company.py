from enum import Enum


class TaxSystem(str, Enum):
    """Система налогообложения.

    Attributes:
        OSNO: ОСНО
        USN: УСН
        NPD: НПД
        AUSN: АУСН
        PSN: ПСН
        UNKNOWN: неизвестная
        UNSPECIFIED: не определена
    """
    OSNO = "OSNO"
    USN = "USN"
    NPD = "NPD"
    AUSN = "AUSN"
    PSN = "PSN"
    UNKNOWN = "UNKNOWN"
    UNSPECIFIED = "UNSPECIFIED"


class RatingStatus(str, Enum):
    """Статус рейтинга.

    Attributes:
        UNKNOWN: не определён
        OK: хороший
        WARNING: показатели требуют внимания
        CRITICAL: критичный
    """
    UNKNOWN = "UNKNOWN"
    OK = "OK"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"


class RatingValueType(str, Enum):
    """Тип значения.

    Attributes:
        UNKNOWN: не определён
        INDEX: индекс
        PERCENT: процент
        TIME: время
        RATIO: коэффициент
        REVIEW_SCORE: оценка
        COUNT: счёт
    """

    UNKNOWN = "UNKNOWN"
    INDEX = "INDEX"
    PERCENT = "PERCENT"
    TIME = "TIME"
    RATIO = "RATIO"
    REVIEW_SCORE = "REVIEW_SCORE"
    COUNT = "COUNT"


class SubscriptionType(str, Enum):
    """Тип подписки.

    Attributes:
        UNKNOWN — неизвестный
        UNSPECIFIED — нет подписки
        PREMIUM — Premium
        PREMIUM_LITE — Premium Lite
        PREMIUM_PLUS — Premium Plus
        PREMIUM_PRO — Premium Pro
    """
    UNKNOWN = "UNKNOWN"
    UNSPECIFIED = "UNSPECIFIED"
    PREMIUM = "PREMIUM"
    PREMIUM_LITE = "PREMIUM_LITE"
    PREMIUM_PLUS = "PREMIUM_PLUS"
    PREMIUM_PRO = "PREMIUM_PRO"