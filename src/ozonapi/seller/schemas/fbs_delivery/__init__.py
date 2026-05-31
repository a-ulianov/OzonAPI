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
]

from .entities import DeliveryListError
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
