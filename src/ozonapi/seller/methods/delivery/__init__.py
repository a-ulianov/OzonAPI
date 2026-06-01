"""Композиция миксинов методов раздела Доставка."""
from ...core import APIManager
from .delivery_check import DeliveryCheckMixin
from .delivery_checkout import DeliveryCheckoutMixin
from .delivery_map import DeliveryMapMixin
from .delivery_point_info import DeliveryPointInfoMixin
from .delivery_point_list import DeliveryPointListMixin


class SellerDeliveryAPI(
    DeliveryCheckMixin,
    DeliveryCheckoutMixin,
    DeliveryMapMixin,
    DeliveryPointInfoMixin,
    DeliveryPointListMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Доставка.

    Notes:
        • Проверка доступности доставки, расчёт вариантов доставки, точки
          самовывоза на карте и их подробная информация.

    References:
        • https://docs.ozon.ru/api/seller/#tag/DeliveryFBS
    """

    pass
