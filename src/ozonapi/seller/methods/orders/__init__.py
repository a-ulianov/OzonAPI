"""Композиция миксинов методов раздела Заказы."""
from ...core import APIManager
from .order_cancel import OrderCancelMixin
from .order_cancel_check import OrderCancelCheckMixin
from .order_cancel_status import OrderCancelStatusMixin
from .order_create import OrderCreateMixin


class SellerOrderAPI(
    OrderCancelMixin,
    OrderCancelCheckMixin,
    OrderCancelStatusMixin,
    OrderCreateMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Заказы.

    Notes:
        • Отмена заказа rFBS (целиком), проверка возможности и статуса отмены,
          создание заказа.

    References:
        • https://docs.ozon.ru/api/seller/#tag/OrderAPI
    """

    pass
