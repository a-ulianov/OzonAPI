"""Схемы раздела Создание и управление заявками на поставку FBO."""
__all__ = [
    "ClusterListV1Request",
    "ClusterWarehouse",
    "ClusterLogisticCluster",
    "Cluster",
    "ClusterListV1Response",
    "WarehouseFboListRequest",
    "WarehouseFboListCoordinate",
    "WarehouseFboListItem",
    "WarehouseFboListResponse",
    "WarehouseFboSellerCoordinates",
    "WarehouseFboSellerAddress",
    "WarehouseFboSellerContacts",
    "WarehouseFboSellerWorkingDay",
    "WarehouseFboSellerItem",
    "WarehouseFboSellerListResponse",
    "DraftCreateItem",
    "DraftCreateRequest",
    "DraftCreateResponse",
    "DraftCreateInfoV1Request",
    "DraftCreateInfoV1BundleId",
    "DraftCreateInfoV1WarehouseStatus",
    "DraftCreateInfoV1SupplyWarehouse",
    "DraftCreateInfoV1Warehouse",
    "DraftCreateInfoV1Cluster",
    "DraftCreateInfoV1ItemValidation",
    "DraftCreateInfoV1Error",
    "DraftCreateInfoV1Response",
    "DraftCreateInfoRequest",
    "DraftCreateInfoAvailabilityStatus",
    "DraftCreateInfoStorageWarehouse",
    "DraftCreateInfoWarehouse",
    "DraftCreateInfoCluster",
    "DraftCreateInfoRejectedItem",
    "DraftCreateInfoItemValidation",
    "DraftCreateInfoError",
    "DraftCreateInfoResponse",
    "DraftTimeslotInfoV1Request",
    "DraftTimeslotV1Slot",
    "DraftTimeslotV1Day",
    "DraftTimeslotV1Warehouse",
    "DraftTimeslotInfoV1Response",
    "DraftTimeslotInfoSelectedClusterWarehouse",
    "DraftTimeslotInfoRequest",
    "DraftTimeslotSlot",
    "DraftTimeslotDay",
    "DraftTimeslotWarehouseTimeslots",
    "DraftTimeslotInfoResult",
    "DraftTimeslotInfoResponse",
    "DraftTypedItem",
    "DraftTypedClusterInfo",
    "DraftTypedDropOffWarehouse",
    "DraftTypedDeliveryInfo",
    "DraftTypedRejectedItem",
    "DraftTypedItemsValidation",
    "DraftTypedError",
    "DraftTypedCreateResponse",
    "DraftCrossdockCreateRequest",
    "DraftDirectCreateRequest",
    "DraftMultiClusterCreateRequest",
    "DraftSupplyCreateTimeslot",
    "DraftSupplyCreateSelectedClusterWarehouse",
    "DraftSupplyCreateRequest",
    "DraftSupplyCreateResponse",
    "DraftSupplyCreateV1Request",
    "DraftSupplyCreateV1Response",
    "DraftSupplyCreateStatusRequest",
    "DraftSupplyCreateStatusResponse",
    "DraftSupplyCreateStatusV1Request",
    "DraftSupplyCreateStatusV1Result",
    "DraftSupplyCreateStatusV1Response",
    "CargoesCreateItem",
    "CargoesCreateCargoValue",
    "CargoesCreateCargo",
    "CargoesCreateRequest",
    "CargoesCreateItemValidation",
    "CargoesCreateErrors",
    "CargoesCreateResponse",
    "CargoesCreateInfoRequest",
    "CargoesCreateInfoItemValidation",
    "CargoesCreateInfoErrors",
    "CargoesCreateInfoCargoValue",
    "CargoesCreateInfoCargo",
    "CargoesCreateInfoResult",
    "CargoesCreateInfoResponse",
    "CargoesGetV1Request",
    "CargoesGetV1TrackingInfo",
    "CargoesGetV1Cargo",
    "CargoesGetV1Supply",
    "CargoesGetV1Response",
    "CargoesDeleteV1Request",
    "CargoesDeleteV1CargoErrorReason",
    "CargoesDeleteV1Errors",
    "CargoesDeleteV1Response",
    "CargoesDeleteStatusV1Request",
    "CargoesDeleteStatusV1Response",
    "CargoesGetSupplyRequest",
    "CargoesGetRequest",
    "CargoesGetTimezone",
    "CargoesGetArrivalAt",
    "CargoesGetTrackingInfo",
    "CargoesGetCargo",
    "CargoesGetLimits",
    "CargoesGetTransportArrivalAt",
    "CargoesGetTransportTrackingInfo",
    "CargoesGetTransportCargo",
    "CargoesGetSupply",
    "CargoesGetResponse",
    "CargoesDeleteRequest",
    "CargoesDeleteCargoErrorReason",
    "CargoesDeleteTransportCargoErrorReason",
    "CargoesDeleteErrors",
    "CargoesDeleteResponse",
    "CargoesDeleteStatusRequest",
    "CargoesDeleteStatusResponse",
    "CargoesTransportCreateItem",
    "CargoesTransportCreateRequest",
    "CargoesTransportCreateResponse",
    "CargoesTransportCreateStatusRequest",
    "CargoesTransportCreateStatusTransportCargo",
    "CargoesTransportCreateStatusResult",
    "CargoesTransportCreateStatusResponse",
    "CargoesTransportActivateRequest",
    "CargoesTransportActivateResponse",
    "CargoesTransportActivateStatusRequest",
    "CargoesTransportActivateStatusResponse",
    "CargoesTransportBindItem",
    "CargoesTransportBindRequest",
    "CargoesTransportBindResponse",
    "CargoesTransportBindStatusRequest",
    "CargoesTransportBindStatusResponse",
    "CargoesSuppliesGetRequest",
    "CargoesSuppliesGetCargo",
    "CargoesSuppliesGetTransportCargo",
    "CargoesSuppliesGetSupply",
    "CargoesSuppliesGetResponse",
    "CargoesLabelTransportCreateRequest",
    "CargoesLabelTransportCreateResponse",
    "CargoesLabelTransportStatusRequest",
    "CargoesLabelTransportStatusResult",
    "CargoesLabelTransportStatusResponse",
    "CargoesLabelTransportByOrderCreateRequest",
    "CargoesLabelTransportByOrderCreateResponse",
    "CargoesLabelTransportByOrderStatusRequest",
    "CargoesLabelTransportByOrderStatusResult",
    "CargoesLabelTransportByOrderStatusResponse",
    "CargoesRulesGetRequest",
    "CargoesRulesCargoCountPerType",
    "CargoesRulesPresentsRule",
    "CargoesRulesEditDeadlineExpireRule",
    "CargoesRulesExpireDatesPresentedRule",
    "CargoesRulesIsValidDistributionRule",
    "CargoesRulesPackageUnitsWithDistributionRule",
    "CargoesRulesPlacementZonesRule",
    "CargoesRulesSupplyCheck",
    "CargoesRulesGetResponse",
    "CargoesLabelErrors",
    "CargoesLabelCreateCargo",
    "CargoesLabelCreateRequest",
    "CargoesLabelCreateResponse",
    "CargoesLabelGetRequest",
    "CargoesLabelGetResult",
    "CargoesLabelGetResponse",
    "CargoesLabelFileResponse",
    "SupplyOrderCancelRequest",
    "SupplyOrderCancelResponse",
    "SupplyOrderCancelStatusRequest",
    "SupplyOrderCancelStatusSupply",
    "SupplyOrderCancelStatusResult",
    "SupplyOrderCancelStatusResponse",
    "SupplyOrderContentUpdateItem",
    "SupplyOrderContentUpdateRequest",
    "SupplyOrderContentUpdateResponse",
    "SupplyOrderContentUpdateStatusRequest",
    "SupplyOrderContentUpdateStatusResponse",
    "SupplyOrderContentUpdateValidationRequest",
    "SupplyOrderContentUpdateValidationApprovedItem",
    "SupplyOrderContentUpdateValidationRestrictions",
    "SupplyOrderContentUpdateValidationRejectedItem",
    "SupplyOrderContentUpdateValidationAssortment",
    "SupplyOrderContentUpdateValidationResponse",
]

from .entities import (
    DraftTypedClusterInfo,
    DraftTypedCreateResponse,
    DraftTypedDeliveryInfo,
    DraftTypedDropOffWarehouse,
    DraftTypedError,
    DraftTypedItem,
    DraftTypedItemsValidation,
    DraftTypedRejectedItem,
)
from .v1__cluster_list import (
    Cluster,
    ClusterListV1Request,
    ClusterListV1Response,
    ClusterLogisticCluster,
    ClusterWarehouse,
)
from .v1__draft_create import (
    DraftCreateItem,
    DraftCreateRequest,
    DraftCreateResponse,
)
from .v1__draft_crossdock_create import DraftCrossdockCreateRequest
from .v1__draft_direct_create import DraftDirectCreateRequest
from .v1__draft_multi_cluster_create import DraftMultiClusterCreateRequest
from .v1__cargoes_create import (
    CargoesCreateCargo,
    CargoesCreateCargoValue,
    CargoesCreateErrors,
    CargoesCreateItem,
    CargoesCreateItemValidation,
    CargoesCreateRequest,
    CargoesCreateResponse,
)
from .v2__cargoes_create_info import (
    CargoesCreateInfoCargo,
    CargoesCreateInfoCargoValue,
    CargoesCreateInfoErrors,
    CargoesCreateInfoItemValidation,
    CargoesCreateInfoRequest,
    CargoesCreateInfoResponse,
    CargoesCreateInfoResult,
)
from .v1__cargoes_get import (
    CargoesGetV1Cargo,
    CargoesGetV1Request,
    CargoesGetV1Response,
    CargoesGetV1Supply,
    CargoesGetV1TrackingInfo,
)
from .v1__cargoes_delete import (
    CargoesDeleteV1CargoErrorReason,
    CargoesDeleteV1Errors,
    CargoesDeleteV1Request,
    CargoesDeleteV1Response,
)
from .v1__cargoes_delete_status import (
    CargoesDeleteStatusV1Request,
    CargoesDeleteStatusV1Response,
)
from .v2__cargoes_get import (
    CargoesGetArrivalAt,
    CargoesGetCargo,
    CargoesGetLimits,
    CargoesGetRequest,
    CargoesGetResponse,
    CargoesGetSupply,
    CargoesGetSupplyRequest,
    CargoesGetTimezone,
    CargoesGetTrackingInfo,
    CargoesGetTransportArrivalAt,
    CargoesGetTransportCargo,
    CargoesGetTransportTrackingInfo,
)
from .v2__cargoes_delete import (
    CargoesDeleteCargoErrorReason,
    CargoesDeleteErrors,
    CargoesDeleteRequest,
    CargoesDeleteResponse,
    CargoesDeleteTransportCargoErrorReason,
)
from .v2__cargoes_delete_status import (
    CargoesDeleteStatusRequest,
    CargoesDeleteStatusResponse,
)
from .v1__cargoes_transport_create import (
    CargoesTransportCreateItem,
    CargoesTransportCreateRequest,
    CargoesTransportCreateResponse,
)
from .v1__cargoes_transport_create_status import (
    CargoesTransportCreateStatusRequest,
    CargoesTransportCreateStatusResponse,
    CargoesTransportCreateStatusResult,
    CargoesTransportCreateStatusTransportCargo,
)
from .v1__cargoes_transport_activate import (
    CargoesTransportActivateRequest,
    CargoesTransportActivateResponse,
)
from .v1__cargoes_transport_activate_status import (
    CargoesTransportActivateStatusRequest,
    CargoesTransportActivateStatusResponse,
)
from .v1__cargoes_transport_bind import (
    CargoesTransportBindItem,
    CargoesTransportBindRequest,
    CargoesTransportBindResponse,
)
from .v1__cargoes_transport_bind_status import (
    CargoesTransportBindStatusRequest,
    CargoesTransportBindStatusResponse,
)
from .v1__cargoes_supplies_get import (
    CargoesSuppliesGetCargo,
    CargoesSuppliesGetRequest,
    CargoesSuppliesGetResponse,
    CargoesSuppliesGetSupply,
    CargoesSuppliesGetTransportCargo,
)
from .v1__cargoes_label_transport_create import (
    CargoesLabelTransportCreateRequest,
    CargoesLabelTransportCreateResponse,
)
from .v1__cargoes_label_transport_status import (
    CargoesLabelTransportStatusRequest,
    CargoesLabelTransportStatusResponse,
    CargoesLabelTransportStatusResult,
)
from .v1__cargoes_label_transport_by_order_create import (
    CargoesLabelTransportByOrderCreateRequest,
    CargoesLabelTransportByOrderCreateResponse,
)
from .v1__cargoes_label_transport_by_order_status import (
    CargoesLabelTransportByOrderStatusRequest,
    CargoesLabelTransportByOrderStatusResponse,
    CargoesLabelTransportByOrderStatusResult,
)
from .v1__cargoes_rules_get import (
    CargoesRulesCargoCountPerType,
    CargoesRulesEditDeadlineExpireRule,
    CargoesRulesExpireDatesPresentedRule,
    CargoesRulesGetRequest,
    CargoesRulesGetResponse,
    CargoesRulesIsValidDistributionRule,
    CargoesRulesPackageUnitsWithDistributionRule,
    CargoesRulesPlacementZonesRule,
    CargoesRulesPresentsRule,
    CargoesRulesSupplyCheck,
)
from .v1__cargoes_label_create import (
    CargoesLabelCreateCargo,
    CargoesLabelCreateRequest,
    CargoesLabelCreateResponse,
    CargoesLabelErrors,
)
from .v1__cargoes_label_file import CargoesLabelFileResponse
from .v1__supply_order_cancel import (
    SupplyOrderCancelRequest,
    SupplyOrderCancelResponse,
)
from .v1__supply_order_cancel_status import (
    SupplyOrderCancelStatusRequest,
    SupplyOrderCancelStatusResponse,
    SupplyOrderCancelStatusResult,
    SupplyOrderCancelStatusSupply,
)
from .v1__supply_order_content_update import (
    SupplyOrderContentUpdateItem,
    SupplyOrderContentUpdateRequest,
    SupplyOrderContentUpdateResponse,
)
from .v1__supply_order_content_update_status import (
    SupplyOrderContentUpdateStatusRequest,
    SupplyOrderContentUpdateStatusResponse,
)
from .v1__supply_order_content_update_validation import (
    SupplyOrderContentUpdateValidationApprovedItem,
    SupplyOrderContentUpdateValidationAssortment,
    SupplyOrderContentUpdateValidationRejectedItem,
    SupplyOrderContentUpdateValidationRequest,
    SupplyOrderContentUpdateValidationResponse,
    SupplyOrderContentUpdateValidationRestrictions,
)
from .v1__cargoes_label_get import (
    CargoesLabelGetRequest,
    CargoesLabelGetResponse,
    CargoesLabelGetResult,
)
from .v1__draft_supply_create import (
    DraftSupplyCreateV1Request,
    DraftSupplyCreateV1Response,
)
from .v1__draft_supply_create_status import (
    DraftSupplyCreateStatusV1Request,
    DraftSupplyCreateStatusV1Response,
    DraftSupplyCreateStatusV1Result,
)
from .v2__draft_supply_create import (
    DraftSupplyCreateRequest,
    DraftSupplyCreateResponse,
    DraftSupplyCreateSelectedClusterWarehouse,
    DraftSupplyCreateTimeslot,
)
from .v2__draft_supply_create_status import (
    DraftSupplyCreateStatusRequest,
    DraftSupplyCreateStatusResponse,
)
from .v1__draft_create_info import (
    DraftCreateInfoV1BundleId,
    DraftCreateInfoV1Cluster,
    DraftCreateInfoV1Error,
    DraftCreateInfoV1ItemValidation,
    DraftCreateInfoV1Request,
    DraftCreateInfoV1Response,
    DraftCreateInfoV1SupplyWarehouse,
    DraftCreateInfoV1Warehouse,
    DraftCreateInfoV1WarehouseStatus,
)
from .v1__draft_timeslot_info import (
    DraftTimeslotInfoV1Request,
    DraftTimeslotInfoV1Response,
    DraftTimeslotV1Day,
    DraftTimeslotV1Slot,
    DraftTimeslotV1Warehouse,
)
from .v2__draft_create_info import (
    DraftCreateInfoAvailabilityStatus,
    DraftCreateInfoCluster,
    DraftCreateInfoError,
    DraftCreateInfoItemValidation,
    DraftCreateInfoRejectedItem,
    DraftCreateInfoRequest,
    DraftCreateInfoResponse,
    DraftCreateInfoStorageWarehouse,
    DraftCreateInfoWarehouse,
)
from .v2__draft_timeslot_info import (
    DraftTimeslotDay,
    DraftTimeslotInfoRequest,
    DraftTimeslotInfoResponse,
    DraftTimeslotInfoResult,
    DraftTimeslotInfoSelectedClusterWarehouse,
    DraftTimeslotSlot,
    DraftTimeslotWarehouseTimeslots,
)
from .v1__warehouse_fbo_list import (
    WarehouseFboListCoordinate,
    WarehouseFboListItem,
    WarehouseFboListRequest,
    WarehouseFboListResponse,
)
from .v1__warehouse_fbo_seller_list import (
    WarehouseFboSellerAddress,
    WarehouseFboSellerContacts,
    WarehouseFboSellerCoordinates,
    WarehouseFboSellerItem,
    WarehouseFboSellerListResponse,
    WarehouseFboSellerWorkingDay,
)
