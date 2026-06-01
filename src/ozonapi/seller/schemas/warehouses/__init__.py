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
    "WarehouseFBSCoordinates",
    "WarehouseFBSTimeOfDay",
    "WarehouseFBSPointSearch",
    "WarehouseFBSDropOffPoint",
    "WarehouseFBSDropOffTimeslot",
    "WarehouseFBSPickUpTimeslot",
    "WarehouseFBSReturnPointWorkingDay",
    "WarehouseFBSReturnPoint",
    "WarehouseFBSOptions",
    "WarehouseFBSCreateDropOffListRequest",
    "WarehouseFBSCreateDropOffListResponse",
    "WarehouseFBSUpdateDropOffListRequest",
    "WarehouseFBSUpdateDropOffListResponse",
    "WarehouseFBSCreateDropOffTimeslotListRequest",
    "WarehouseFBSCreateDropOffTimeslotListResponse",
    "WarehouseFBSUpdateDropOffTimeslotListRequest",
    "WarehouseFBSUpdateDropOffTimeslotListResponse",
    "WarehouseFBSCreatePickUpTimeslotListRequest",
    "WarehouseFBSCreatePickUpTimeslotListResponse",
    "WarehouseFBSUpdatePickUpTimeslotListRequest",
    "WarehouseFBSUpdatePickUpTimeslotListResponse",
    "WarehouseFBSCreateRequest",
    "WarehouseFBSCreateResponse",
    "WarehouseFBSUpdateRequest",
    "WarehouseFBSUpdateResponse",
    "WarehouseFBSFirstMileUpdateRequest",
    "WarehouseFBSFirstMileUpdateResponse",
    "WarehouseFBSCreateReturnPointListRequest",
    "WarehouseFBSCreateReturnPointListResponse",
    "WarehouseFBSUpdateReturnPointListRequest",
    "WarehouseFBSUpdateReturnPointListResponse",
    "WarehouseFBSReturnMileInfoRequest",
    "WarehouseFBSReturnMileSetting",
    "WarehouseFBSReturnMileInfoResponse",
    "WarehouseFBSReturnMileCheckRequest",
    "WarehouseFBSReturnMileCheckResponse",
    "WarehouseFBSPickUpCourierCreateRequest",
    "WarehouseFBSPickUpCourierCreateResponse",
    "WarehouseFBSPickUpCourierCancelRequest",
    "WarehouseFBSPickUpCourierCancelResponse",
    "WarehouseFBSPickUpHistoryListFilter",
    "WarehouseFBSPickUpHistoryListRequest",
    "WarehouseFBSPickUpHistoryEntity",
    "WarehouseFBSPickUpHistoryListResult",
    "WarehouseFBSPickUpHistoryListResponse",
    "WarehouseFBSPickUpPlanningWarehouse",
    "WarehouseFBSPickUpPlanningListResult",
    "WarehouseFBSPickUpPlanningListResponse",
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
from .entities import (
    WarehouseFBSCoordinates,
    WarehouseFBSDropOffPoint,
    WarehouseFBSDropOffTimeslot,
    WarehouseFBSOptions,
    WarehouseFBSPickUpTimeslot,
    WarehouseFBSPointSearch,
    WarehouseFBSReturnPoint,
    WarehouseFBSReturnPointWorkingDay,
    WarehouseFBSTimeOfDay,
)
from .v1__warehouse_fbs_create_drop_off_list import (
    WarehouseFBSCreateDropOffListRequest,
    WarehouseFBSCreateDropOffListResponse,
)
from .v1__warehouse_fbs_update_drop_off_list import (
    WarehouseFBSUpdateDropOffListRequest,
    WarehouseFBSUpdateDropOffListResponse,
)
from .v1__warehouse_fbs_create_drop_off_timeslot_list import (
    WarehouseFBSCreateDropOffTimeslotListRequest,
    WarehouseFBSCreateDropOffTimeslotListResponse,
)
from .v1__warehouse_fbs_update_drop_off_timeslot_list import (
    WarehouseFBSUpdateDropOffTimeslotListRequest,
    WarehouseFBSUpdateDropOffTimeslotListResponse,
)
from .v1__warehouse_fbs_create_pick_up_timeslot_list import (
    WarehouseFBSCreatePickUpTimeslotListRequest,
    WarehouseFBSCreatePickUpTimeslotListResponse,
)
from .v1__warehouse_fbs_update_pick_up_timeslot_list import (
    WarehouseFBSUpdatePickUpTimeslotListRequest,
    WarehouseFBSUpdatePickUpTimeslotListResponse,
)
from .v1__warehouse_fbs_create import (
    WarehouseFBSCreateRequest,
    WarehouseFBSCreateResponse,
)
from .v1__warehouse_fbs_update import (
    WarehouseFBSUpdateRequest,
    WarehouseFBSUpdateResponse,
)
from .v1__warehouse_fbs_first_mile_update import (
    WarehouseFBSFirstMileUpdateRequest,
    WarehouseFBSFirstMileUpdateResponse,
)
from .v1__warehouse_fbs_create_return_point_list import (
    WarehouseFBSCreateReturnPointListRequest,
    WarehouseFBSCreateReturnPointListResponse,
)
from .v1__warehouse_fbs_update_return_point_list import (
    WarehouseFBSUpdateReturnPointListRequest,
    WarehouseFBSUpdateReturnPointListResponse,
)
from .v1__warehouse_fbs_return_mile_info import (
    WarehouseFBSReturnMileInfoRequest,
    WarehouseFBSReturnMileInfoResponse,
    WarehouseFBSReturnMileSetting,
)
from .v1__warehouse_fbs_return_mile_check import (
    WarehouseFBSReturnMileCheckRequest,
    WarehouseFBSReturnMileCheckResponse,
)
from .v1__warehouse_fbs_pickup_courier_create import (
    WarehouseFBSPickUpCourierCreateRequest,
    WarehouseFBSPickUpCourierCreateResponse,
)
from .v1__warehouse_fbs_pickup_courier_cancel import (
    WarehouseFBSPickUpCourierCancelRequest,
    WarehouseFBSPickUpCourierCancelResponse,
)
from .v1__warehouse_fbs_pickup_history_list import (
    WarehouseFBSPickUpHistoryEntity,
    WarehouseFBSPickUpHistoryListFilter,
    WarehouseFBSPickUpHistoryListRequest,
    WarehouseFBSPickUpHistoryListResponse,
    WarehouseFBSPickUpHistoryListResult,
)
from .v1__warehouse_fbs_pickup_planning_list import (
    WarehouseFBSPickUpPlanningListResponse,
    WarehouseFBSPickUpPlanningListResult,
    WarehouseFBSPickUpPlanningWarehouse,
)
