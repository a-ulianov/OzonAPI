__all__ = ["SellerWarehouseAPI", ]

from .delivery_method_list import DeliveryMethodListMixin
from .delivery_method_list_v1 import DeliveryMethodListV1Mixin
from .delivery_method_return_settings_get import (
    DeliveryMethodReturnSettingsGetMixin,
)
from .warehouse_archive import WarehouseArchiveMixin
from .warehouse_fbs_create import WarehouseFBSCreateMixin
from .warehouse_fbs_create_drop_off_list import WarehouseFBSCreateDropOffListMixin
from .warehouse_fbs_create_drop_off_timeslot_list import (
    WarehouseFBSCreateDropOffTimeslotListMixin,
)
from .warehouse_fbs_create_pick_up_timeslot_list import (
    WarehouseFBSCreatePickUpTimeslotListMixin,
)
from .warehouse_fbs_create_return_point_list import (
    WarehouseFBSCreateReturnPointListMixin,
)
from .warehouse_fbs_first_mile_update import WarehouseFBSFirstMileUpdateMixin
from .warehouse_fbs_pickup_courier_cancel import (
    WarehouseFBSPickUpCourierCancelMixin,
)
from .warehouse_fbs_pickup_courier_create import (
    WarehouseFBSPickUpCourierCreateMixin,
)
from .warehouse_fbs_pickup_history_list import WarehouseFBSPickUpHistoryListMixin
from .warehouse_fbs_pickup_planning_list import (
    WarehouseFBSPickUpPlanningListMixin,
)
from .warehouse_fbs_return_mile_check import WarehouseFBSReturnMileCheckMixin
from .warehouse_fbs_return_mile_info import WarehouseFBSReturnMileInfoMixin
from .warehouse_fbs_update import WarehouseFBSUpdateMixin
from .warehouse_fbs_update_drop_off_list import WarehouseFBSUpdateDropOffListMixin
from .warehouse_fbs_update_drop_off_timeslot_list import (
    WarehouseFBSUpdateDropOffTimeslotListMixin,
)
from .warehouse_fbs_update_pick_up_timeslot_list import (
    WarehouseFBSUpdatePickUpTimeslotListMixin,
)
from .warehouse_fbs_update_return_point_list import (
    WarehouseFBSUpdateReturnPointListMixin,
)
from .warehouse_invalid_products_get import WarehouseInvalidProductsGetMixin
from .warehouse_list import WarehouseListMixin
from .warehouse_list_v1 import WarehouseListV1Mixin
from .warehouse_operation_status import WarehouseOperationStatusMixin
from .warehouse_ozon_list import WarehouseOzonListMixin
from .warehouse_unarchive import WarehouseUnarchiveMixin
from .warehouse_warehouses_with_invalid_products import (
    WarehouseWarehousesWithInvalidProductsMixin,
)


class SellerWarehouseAPI(
    DeliveryMethodListMixin,
    DeliveryMethodListV1Mixin,
    DeliveryMethodReturnSettingsGetMixin,
    WarehouseArchiveMixin,
    WarehouseFBSCreateMixin,
    WarehouseFBSCreateDropOffListMixin,
    WarehouseFBSCreateDropOffTimeslotListMixin,
    WarehouseFBSCreatePickUpTimeslotListMixin,
    WarehouseFBSCreateReturnPointListMixin,
    WarehouseFBSFirstMileUpdateMixin,
    WarehouseFBSPickUpCourierCancelMixin,
    WarehouseFBSPickUpCourierCreateMixin,
    WarehouseFBSPickUpHistoryListMixin,
    WarehouseFBSPickUpPlanningListMixin,
    WarehouseFBSReturnMileCheckMixin,
    WarehouseFBSReturnMileInfoMixin,
    WarehouseFBSUpdateMixin,
    WarehouseFBSUpdateDropOffListMixin,
    WarehouseFBSUpdateDropOffTimeslotListMixin,
    WarehouseFBSUpdatePickUpTimeslotListMixin,
    WarehouseFBSUpdateReturnPointListMixin,
    WarehouseInvalidProductsGetMixin,
    WarehouseListMixin,
    WarehouseListV1Mixin,
    WarehouseOperationStatusMixin,
    WarehouseOzonListMixin,
    WarehouseUnarchiveMixin,
    WarehouseWarehousesWithInvalidProductsMixin,
):
    """Реализует методы раздела Склады.

    References:
        https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
    """
    pass
