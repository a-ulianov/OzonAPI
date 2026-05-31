"""Общие вложенные модели раздела Возвраты."""
__all__ = [
    "ReturnsMoney",
    "ReturnsTimeRange",
    "ReturnsPlace",
    "ReturnsStatus",
    "ReturnsRfbsProduct",
]

from .returns_money import ReturnsMoney
from .returns_place import ReturnsPlace
from .returns_rfbs_product import ReturnsRfbsProduct
from .returns_status import ReturnsStatus
from .returns_time_range import ReturnsTimeRange
