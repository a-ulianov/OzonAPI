"""Композиция миксинов методов раздела заявок на поставку FBO.

Объединяет методы создания и управления заявками на поставку FBO в единый класс
:class:`SellerFboSupplyRequestAPI`.
"""

from ...core import APIManager
from .cluster_list import ClusterListMixin
from .draft_create import DraftCreateMixin
from .draft_create_info import DraftCreateInfoMixin
from .draft_create_info_v1 import DraftCreateInfoV1Mixin
from .draft_crossdock_create import DraftCrossdockCreateMixin
from .draft_direct_create import DraftDirectCreateMixin
from .draft_multi_cluster_create import DraftMultiClusterCreateMixin
from .draft_timeslot_info import DraftTimeslotInfoMixin
from .draft_timeslot_info_v1 import DraftTimeslotInfoV1Mixin
from .warehouse_fbo_list import WarehouseFboListMixin
from .warehouse_fbo_seller_list import WarehouseFboSellerListMixin


class SellerFboSupplyRequestAPI(
    ClusterListMixin,
    DraftCreateMixin,
    DraftCreateInfoMixin,
    DraftCreateInfoV1Mixin,
    DraftCrossdockCreateMixin,
    DraftDirectCreateMixin,
    DraftMultiClusterCreateMixin,
    DraftTimeslotInfoMixin,
    DraftTimeslotInfoV1Mixin,
    WarehouseFboListMixin,
    WarehouseFboSellerListMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела заявок на поставку FBO.

    Notes:
        • Справочные методы (кластеры, склады отгрузки), создание черновика заявки
          на поставку, получение информации о черновике и доступных таймслотов.

    References:
        • https://docs.ozon.ru/api/seller/#tag/FboSupplyRequestAPI
    """

    pass
