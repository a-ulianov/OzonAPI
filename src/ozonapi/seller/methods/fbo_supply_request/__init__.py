"""Композиция миксинов методов раздела заявок на поставку FBO.

Объединяет методы создания и управления заявками на поставку FBO в единый класс
:class:`SellerFboSupplyRequestAPI`.
"""

from ...core import APIManager
from .cluster_list import ClusterListMixin
from .warehouse_fbo_list import WarehouseFboListMixin
from .warehouse_fbo_seller_list import WarehouseFboSellerListMixin


class SellerFboSupplyRequestAPI(
    ClusterListMixin,
    WarehouseFboListMixin,
    WarehouseFboSellerListMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела заявок на поставку FBO.

    Notes:
        • Справочные методы для подбора кластеров и складов отгрузки при создании
          черновика заявки на поставку FBO.

    References:
        • https://docs.ozon.ru/api/seller/#tag/FboSupplyRequestAPI
    """

    pass
