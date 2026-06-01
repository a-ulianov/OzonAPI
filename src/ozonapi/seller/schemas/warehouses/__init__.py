"""Описывает модели методов раздела Склады.
https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
"""
__all__ = [
    "WarehouseListRequest",
    "WarehouseListResponse",
    "WarehouseListItem",
    "WarehouseListAddressInfo",
    "WarehouseListFirstMile",
    "WarehouseListTimetable",
    "WarehouseListWorkingHours",
    "DeliveryMethodListRequest",
    "DeliveryMethodListResponse",
    "DeliveryMethodListFilter",
    "DeliveryMethodListItem",
    "DeliveryMethodListDropOffPoint",
    "DeliveryMethodListAddressCoordinates",
    "WarehouseListV1Request",
    "WarehouseListV1RequestWith",
    "WarehouseListV1FirstMile",
    "WarehouseListV1Item",
    "WarehouseListV1Response",
    "DeliveryMethodListV1Filter",
    "DeliveryMethodListV1Request",
    "DeliveryMethodListV1Item",
    "DeliveryMethodListV1Response",
    "DeliveryMethodReturnSettingsRequest",
    "DeliveryMethodReturnSettingsCourierDetails",
    "DeliveryMethodReturnSettingsTransportCompanyDetails",
    "DeliveryMethodReturnSetting",
    "DeliveryMethodReturnSettingsResponse",
    "WarehouseOperationStatusRequest",
    "WarehouseOperationStatusError",
    "WarehouseOperationStatusResult",
    "WarehouseOperationStatusResponse",
    "WarehouseArchiveRequest",
    "WarehouseArchiveResponse",
    "WarehouseUnarchiveRequest",
    "WarehouseUnarchiveResponse",
    "WarehouseInvalidProductsGetRequest",
    "WarehouseInvalidProductItemSize",
    "WarehouseInvalidProductItem",
    "WarehouseInvalidProductMoney",
    "WarehouseInvalidProductValidationError",
    "WarehouseInvalidProductValidationResult",
    "WarehouseInvalidProductsGetResponse",
    "WarehouseWithInvalidProductsResponse",
]

from .v2__delivery_method_list import (
    DeliveryMethodListRequest,
    DeliveryMethodListResponse,
    DeliveryMethodListFilter,
    DeliveryMethodListItem,
    DeliveryMethodListDropOffPoint,
    DeliveryMethodListAddressCoordinates,
)
from .v2__warehouse_list import (
    WarehouseListRequest,
    WarehouseListResponse,
    WarehouseListItem,
    WarehouseListAddressInfo,
    WarehouseListFirstMile,
    WarehouseListTimetable,
    WarehouseListWorkingHours,
)
from .v1__warehouse_list import (
    WarehouseListV1FirstMile,
    WarehouseListV1Item,
    WarehouseListV1Request,
    WarehouseListV1RequestWith,
    WarehouseListV1Response,
)
from .v1__delivery_method_list import (
    DeliveryMethodListV1Filter,
    DeliveryMethodListV1Item,
    DeliveryMethodListV1Request,
    DeliveryMethodListV1Response,
)
from .v1__delivery_method_return_settings_get import (
    DeliveryMethodReturnSetting,
    DeliveryMethodReturnSettingsCourierDetails,
    DeliveryMethodReturnSettingsRequest,
    DeliveryMethodReturnSettingsResponse,
    DeliveryMethodReturnSettingsTransportCompanyDetails,
)
from .v1__warehouse_operation_status import (
    WarehouseOperationStatusError,
    WarehouseOperationStatusRequest,
    WarehouseOperationStatusResponse,
    WarehouseOperationStatusResult,
)
from .v1__warehouse_archive import (
    WarehouseArchiveRequest,
    WarehouseArchiveResponse,
)
from .v1__warehouse_unarchive import (
    WarehouseUnarchiveRequest,
    WarehouseUnarchiveResponse,
)
from .v1__warehouse_invalid_products_get import (
    WarehouseInvalidProductItem,
    WarehouseInvalidProductItemSize,
    WarehouseInvalidProductMoney,
    WarehouseInvalidProductValidationError,
    WarehouseInvalidProductValidationResult,
    WarehouseInvalidProductsGetRequest,
    WarehouseInvalidProductsGetResponse,
)
from .v1__warehouse_warehouses_with_invalid_products import (
    WarehouseWithInvalidProductsResponse,
)
