__all__ = ["SellerWarehouseAPI", ]

from .delivery_method_list import DeliveryMethodListMixin
from .warehouse_list import WarehouseListMixin


class SellerWarehouseAPI(
    DeliveryMethodListMixin,
    WarehouseListMixin,
):
    """Реализует методы раздела Склады.

    References:
        https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
    """
    pass