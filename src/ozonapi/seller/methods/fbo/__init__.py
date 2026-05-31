"""Композиция миксинов методов раздела FBO (Доставка FBO).

Объединяет все методы группы ``fbo`` в единый класс :class:`SellerFBOAPI`.
"""

from ...core import APIManager
from .posting_fbo_cancel_reason_list import PostingFBOCancelReasonListMixin
from .posting_fbo_get import PostingFBOGetMixin
from .posting_fbo_list import PostingFBOListMixin
from .supplier_available_warehouses import SupplierAvailableWarehousesMixin
from .supply_order_bundle import SupplyOrderBundleMixin
from .supply_order_details import SupplyOrderDetailsMixin
from .supply_order_get import SupplyOrderGetMixin
from .supply_order_list import SupplyOrderListMixin
from .supply_order_pass_create import SupplyOrderPassCreateMixin
from .supply_order_pass_status import SupplyOrderPassStatusMixin
from .supply_order_status_counter import SupplyOrderStatusCounterMixin
from .supply_order_timeslot_get import SupplyOrderTimeslotGetMixin
from .supply_order_timeslot_status import SupplyOrderTimeslotStatusMixin
from .supply_order_timeslot_update import SupplyOrderTimeslotUpdateMixin


class SellerFBOAPI(
    PostingFBOCancelReasonListMixin,
    PostingFBOGetMixin,
    PostingFBOListMixin,
    SupplierAvailableWarehousesMixin,
    SupplyOrderBundleMixin,
    SupplyOrderDetailsMixin,
    SupplyOrderGetMixin,
    SupplyOrderListMixin,
    SupplyOrderPassCreateMixin,
    SupplyOrderPassStatusMixin,
    SupplyOrderStatusCounterMixin,
    SupplyOrderTimeslotGetMixin,
    SupplyOrderTimeslotStatusMixin,
    SupplyOrderTimeslotUpdateMixin,
    APIManager,
):
    """Класс-агрегатор всех методов раздела FBO.

    Notes:
        • Объединяет методы работы с заявками на поставку (supply-order),
          а также вспомогательные методы (доступные склады).

    References:
        • https://docs.ozon.ru/api/seller/#tag/SupplyOrderAPI
    """

    pass
