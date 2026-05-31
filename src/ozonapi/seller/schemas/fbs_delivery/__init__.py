"""Описывает модели методов раздела Доставка FBS.
https://docs.ozon.ru/api/seller/#tag/CarriageAPI
"""
__all__ = [
    "DeliveryListError",
    "CarriageCreateRequest",
    "CarriageCreateResponse",
    "CarriageApproveRequest",
    "CarriageApproveResponse",
    "CarriageSetPostingsRequest",
    "CarriageSetPostingsResponse",
    "CarriageSetPostingsResult",
    "CarriageCancelRequest",
    "CarriageCancelResponse",
    "CarriageGetRequest",
    "CarriageGetResponse",
    "CarriageGetCancelAvailability",
    "CarriageDeliveryListRequest",
    "CarriageDeliveryListResponse",
    "CarriageDeliveryListFilter",
    "CarriageDeliveryListMethod",
    "CarriageDeliveryListCarriage",
    "CarriageDeliveryListPickupFee",
    "CarriageDeliveryListV1Request",
    "CarriageDeliveryListV1Response",
    "CarriageDeliveryListV1Result",
    "CarriageDeliveryListV1Carriage",
    "PostingCarriageAvailableListRequest",
    "PostingCarriageAvailableListResponse",
    "PostingCarriageAvailableListResult",
    "PostingCarriageAvailableListError",
    "PostingFBSActCreateRequest",
    "PostingFBSActCreateResponse",
    "PostingFBSActCreateAct",
    "PostingFBSActListRequest",
    "PostingFBSActListResponse",
    "PostingFBSActListFilter",
    "PostingFBSActListResult",
    "PostingFBSActListRelatedDocs",
    "PostingFBSActListRelatedDoc",
    "PostingFBSActCheckStatusRequest",
    "PostingFBSActCheckStatusResponse",
    "PostingFBSActCheckStatusResult",
    "PostingFBSActGetPostingsRequest",
    "PostingFBSActGetPostingsResponse",
    "PostingFBSActGetPostingsResult",
    "PostingFBSActGetPostingsProduct",
    "PostingFBSActGetBarcodeTextRequest",
    "PostingFBSActGetBarcodeTextResponse",
    "PostingFBSDigitalActCheckStatusRequest",
    "PostingFBSDigitalActCheckStatusResponse",
    "CarriageActDiscrepancyPDFRequest",
    "CarriageActDiscrepancyPDFResponse",
]

from .entities import DeliveryListError
from .v1__carriage_act_discrepancy_pdf import (
    CarriageActDiscrepancyPDFRequest,
    CarriageActDiscrepancyPDFResponse,
)
from .v1__carriage_approve import CarriageApproveRequest, CarriageApproveResponse
from .v1__carriage_cancel import CarriageCancelRequest, CarriageCancelResponse
from .v1__carriage_create import CarriageCreateRequest, CarriageCreateResponse
from .v1__carriage_delivery_list import (
    CarriageDeliveryListV1Carriage,
    CarriageDeliveryListV1Request,
    CarriageDeliveryListV1Response,
    CarriageDeliveryListV1Result,
)
from .v1__carriage_get import (
    CarriageGetCancelAvailability,
    CarriageGetRequest,
    CarriageGetResponse,
)
from .v1__carriage_set_postings import (
    CarriageSetPostingsRequest,
    CarriageSetPostingsResponse,
    CarriageSetPostingsResult,
)
from .v1__posting_carriage_available_list import (
    PostingCarriageAvailableListError,
    PostingCarriageAvailableListRequest,
    PostingCarriageAvailableListResponse,
    PostingCarriageAvailableListResult,
)
from .v2__carriage_delivery_list import (
    CarriageDeliveryListCarriage,
    CarriageDeliveryListFilter,
    CarriageDeliveryListMethod,
    CarriageDeliveryListPickupFee,
    CarriageDeliveryListRequest,
    CarriageDeliveryListResponse,
)
from .v2__posting_fbs_act_check_status import (
    PostingFBSActCheckStatusRequest,
    PostingFBSActCheckStatusResponse,
    PostingFBSActCheckStatusResult,
)
from .v2__posting_fbs_act_create import (
    PostingFBSActCreateAct,
    PostingFBSActCreateRequest,
    PostingFBSActCreateResponse,
)
from .v2__posting_fbs_act_get_barcode_text import (
    PostingFBSActGetBarcodeTextRequest,
    PostingFBSActGetBarcodeTextResponse,
)
from .v2__posting_fbs_act_get_postings import (
    PostingFBSActGetPostingsProduct,
    PostingFBSActGetPostingsRequest,
    PostingFBSActGetPostingsResponse,
    PostingFBSActGetPostingsResult,
)
from .v2__posting_fbs_act_list import (
    PostingFBSActListFilter,
    PostingFBSActListRelatedDoc,
    PostingFBSActListRelatedDocs,
    PostingFBSActListRequest,
    PostingFBSActListResponse,
    PostingFBSActListResult,
)
from .v2__posting_fbs_digital_act_check_status import (
    PostingFBSDigitalActCheckStatusRequest,
    PostingFBSDigitalActCheckStatusResponse,
)
