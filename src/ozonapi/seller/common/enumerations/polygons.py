from enum import IntEnum


class PolygonDeliveryTime(IntEnum):
    """Время доставки в полигоне, минуты.

    Attributes:
        MIN_15: 15 минут
        MIN_30: 30 минут
        MIN_45: 45 минут
        MIN_60: 60 минут
        MIN_90: 90 минут
        MIN_120: 120 минут
        MIN_150: 150 минут
    """
    MIN_15 = 15
    MIN_30 = 30
    MIN_45 = 45
    MIN_60 = 60
    MIN_90 = 90
    MIN_120 = 120
    MIN_150 = 150
