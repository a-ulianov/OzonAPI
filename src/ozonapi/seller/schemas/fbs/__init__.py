"""Описывает модели методов раздела Обработка заказов FBS и rFBS.
https://docs.ozon.ru/api/seller/?__rr=1#tag/FBS
"""
__all__ = [
    "PostingFBSAddressee",
    "PostingFBSAnalyticsData",
    "PostingFBSArbitrationRequest",
    "PostingFBSArbitrationResponse",
    "PostingFBSAwaitingDeliveryRequest",
    "PostingFBSAwaitingDeliveryResponse",
    "PostingFBSBarcodes",
    "PostingFBSCancelRequest",
    "PostingFBSCancelResponse",
    "PostingFBSCancellation",
    "PostingFBSCancelReasonListResponse",
    "PostingFBSCancelReasonRequest",
    "PostingFBSCancelReasonResponse",
    "PostingFBSCustomer",
    "PostingFBSCustomerAddress",
    "PostingFBSDeliveryMethod",
    "PostingFBSFilterWith",
    "PostingFBSGetByBarcodeRequest",
    "PostingFBSGetByBarcodeResponse",
    "PostingFBSGetRequest",
    "PostingFBSGetResponse",
    "PostingFBSOptional",
    "PostingFBSPackageLabelCreateRequest",
    "PostingFBSPackageLabelCreateResponse",
    "PostingFBSPackageLabelGetRequest",
    "PostingFBSPackageLabelGetResponse",
    "PostingFBSPackageLabelRequest",
    "PostingFBSPackageLabelResponse",
    "PostingFBSPosting",
    "PostingFBSProductCancelItem",
    "PostingFBSProductCancelRequest",
    "PostingFBSProductCancelResponse",
    "PostingFBSProductChangeRequest",
    "PostingFBSProductChangeRequestItem",
    "PostingFBSProductChangeResponse",
    "PostingFBSProductCountrySetRequest",
    "PostingFBSProductCountrySetResponse",
    "PostingFBSProductDetailed",
    "PostingFBSProductCountryListRequest",
    "PostingFBSProductCountryListResponse",
    "PostingFBSRequirements",
    "PostingFBSRestrictionsRequest",
    "PostingFBSRestrictionsResponse",
    "PostingFBSTariffication",
    "PostingFBSListRequestFilterLastChangedStatusDate",
    "PostingFBSListFilter",
    "PostingFBSListRequest",
    "PostingFBSListResult",
    "PostingFBSListResponse",
    "PostingFBSMultiBoxQtySetRequest",
    "PostingFBSMultiBoxQtySetResponse",
    "PostingFBSUnfulfilledListRequest",
    "PostingFBSUnfulfilledListResponse",
    "PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate",
    "PostingFBSUnfulfilledListFilter",
    "PostingFBSUnfulfilledListResult",
]

from .entities import PostingFBSAddressee, PostingFBSAnalyticsData, PostingFBSBarcodes, PostingFBSCancellation, \
    PostingFBSCustomer, PostingFBSCustomerAddress, PostingFBSDeliveryMethod, PostingFBSOptional, PostingFBSPosting, \
    PostingFBSProductDetailed, \
    PostingFBSRequirements, PostingFBSTariffication, PostingFBSFilterWith
from ..entities.postings.legal_info import PostingLegalInfo
from ..entities.postings.product import PostingProduct
from ..entities.postings.financial_data import PostingFinancialData
from ..entities.postings.financial_data_product import PostingFinancialDataProduct
from .v1__posting_fbs_cancel_reason import PostingFBSCancelReasonResponse, PostingFBSCancelReasonRequest
from .v1__posting_fbs_package_label_get import PostingFBSPackageLabelGetResponse, PostingFBSPackageLabelGetRequest
from .v1__posting_fbs_restrictions import PostingFBSRestrictionsResponse, PostingFBSRestrictionsRequest
from .v2__posting_fbs_arbitration import PostingFBSArbitrationRequest, PostingFBSArbitrationResponse
from .v2__posting_fbs_awaiting_delivery import PostingFBSAwaitingDeliveryResponse, PostingFBSAwaitingDeliveryRequest
from .v2__posting_fbs_cancel import PostingFBSCancelRequest, PostingFBSCancelResponse
from .v2__posting_fbs_cancel_reason_list import PostingFBSCancelReasonListResponse
from .v2__posting_fbs_get_by_barcode import PostingFBSGetByBarcodeRequest, PostingFBSGetByBarcodeResponse
from .v2__posting_fbs_package_label import PostingFBSPackageLabelResponse, PostingFBSPackageLabelRequest
from .v2__posting_fbs_package_label_create import PostingFBSPackageLabelCreateResponse, \
    PostingFBSPackageLabelCreateRequest
from .v2__posting_fbs_product_cancel import PostingFBSProductCancelRequest, PostingFBSProductCancelResponse, \
    PostingFBSProductCancelItem
from .v2__posting_fbs_product_change import PostingFBSProductChangeRequestItem, PostingFBSProductChangeRequest, \
    PostingFBSProductChangeResponse
from .v2__posting_fbs_product_country_list import PostingFBSProductCountryListResponse, \
    PostingFBSProductCountryListRequest
from .v2__posting_fbs_product_country_set import PostingFBSProductCountrySetResponse, PostingFBSProductCountrySetRequest
from .v3__posting_fbs_get import PostingFBSGetRequest, PostingFBSGetResponse
from .v3__posting_fbs_list import PostingFBSListRequestFilterLastChangedStatusDate, \
    PostingFBSListFilter, PostingFBSListRequest, PostingFBSListResult, PostingFBSListResponse
from .v3__posting_multiboxqty_set import PostingFBSMultiBoxQtySetResponse, PostingFBSMultiBoxQtySetRequest
from .v3__posting_fbs_unfulfilled_list import (
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse,
    PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate,
    PostingFBSUnfulfilledListFilter,
    PostingFBSUnfulfilledListResult,
)