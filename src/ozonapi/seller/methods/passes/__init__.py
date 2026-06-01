"""Композиция миксинов методов раздела Пропуски.

Объединяет методы работы с пропусками на склады Ozon
в единый класс :class:`SellerPassAPI`.
"""

from ...core import APIManager
from .carriage_pass_create import CarriagePassCreateMixin
from .carriage_pass_delete import CarriagePassDeleteMixin
from .carriage_pass_update import CarriagePassUpdateMixin
from .pass_list import PassListMixin
from .return_pass_create import ReturnPassCreateMixin
from .return_pass_delete import ReturnPassDeleteMixin
from .return_pass_update import ReturnPassUpdateMixin


class SellerPassAPI(
    CarriagePassCreateMixin,
    CarriagePassDeleteMixin,
    CarriagePassUpdateMixin,
    PassListMixin,
    ReturnPassCreateMixin,
    ReturnPassDeleteMixin,
    ReturnPassUpdateMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Пропуски.

    Notes:
        • Работа с пропусками на склады Ozon: список пропусков, создание/обновление/
          удаление пропусков для перевозок FBS и для вывоза возвратов.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Pass
    """

    pass
