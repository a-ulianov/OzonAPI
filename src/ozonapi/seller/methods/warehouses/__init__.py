__all__ = ["SellerWarehouseAPI", ]

from .delivery_method_list import DeliveryMethodListMixin
from .delivery_method_list_v1 import DeliveryMethodListV1Mixin
from .delivery_method_return_settings_get import (
    DeliveryMethodReturnSettingsGetMixin,
)
from .warehouse_archive import WarehouseArchiveMixin
from .warehouse_invalid_products_get import WarehouseInvalidProductsGetMixin
from .warehouse_list import WarehouseListMixin
from .warehouse_list_v1 import WarehouseListV1Mixin
from .warehouse_operation_status import WarehouseOperationStatusMixin
from .warehouse_unarchive import WarehouseUnarchiveMixin
from .warehouse_warehouses_with_invalid_products import (
    WarehouseWarehousesWithInvalidProductsMixin,
)


class SellerWarehouseAPI(
    DeliveryMethodListMixin,
    DeliveryMethodListV1Mixin,
    DeliveryMethodReturnSettingsGetMixin,
    WarehouseArchiveMixin,
    WarehouseInvalidProductsGetMixin,
    WarehouseListMixin,
    WarehouseListV1Mixin,
    WarehouseOperationStatusMixin,
    WarehouseUnarchiveMixin,
    WarehouseWarehousesWithInvalidProductsMixin,
):
    """Реализует методы раздела Склады.

    References:
        https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
    """
    pass
