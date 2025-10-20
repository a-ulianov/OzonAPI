"""Описывает модели методов раздела Обработка заказов FBS и rFBS.
https://docs.ozon.ru/api/seller/?__rr=1#tag/FBS
"""
__all__ = [
    "PostingFBSAddressee",
    "PostingFBSAnalyticsData",
    "PostingFBSBarcodes",
    "PostingFBSCancellation",
    "PostingFBSCustomer",
    "PostingFBSCustomerAddress",
    "PostingFBSDeliveryMethod",
    "PostingFBSFilterWith",
    "PostingFBSFinancialData",
    "PostingFBSFinancialDataProducts",
    "PostingFBSGetByBarcodeRequest",
    "PostingFBSGetByBarcodeResponse",
    "PostingFBSGetRequest",
    "PostingFBSGetResponse",
    "PostingFBSLegalInfo",
    "PostingFBSOptional",
    "PostingFBSPosting",
    "PostingFBSProduct",
    "PostingFBSProductChangeRequest",
    "PostingFBSProductChangeRequestItem",
    "PostingFBSProductChangeResponse",
    "PostingFBSProductDetailed",
    "PostingFBSRequirements",
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
    PostingFBSCustomer, PostingFBSCustomerAddress, PostingFBSDeliveryMethod, PostingFBSFinancialData, \
    PostingFBSFinancialDataProducts, PostingFBSLegalInfo, PostingFBSOptional, PostingFBSPosting, \
    PostingFBSProductDetailed, \
    PostingFBSRequirements, PostingFBSTariffication, PostingFBSFilterWith, PostingFBSProduct
from .v2__posting_fbs_get_by_barcode import PostingFBSGetByBarcodeRequest, PostingFBSGetByBarcodeResponse
from .v2__posting_fbs_product_change import PostingFBSProductChangeRequestItem, PostingFBSProductChangeRequest, \
    PostingFBSProductChangeResponse
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