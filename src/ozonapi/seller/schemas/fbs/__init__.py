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
    "PostingFBSFinancialData",
    "PostingFBSFinancialDataProducts",
    "PostingFBSLegalInfo",
    "PostingFBSOptional",
    "PostingFBSPosting",
    "PostingFBSProducts",
    "PostingFBSRequirements",
    "PostingFBSTariffication",
    "PostingFBSListRequestFilterLastChangedStatusDate",
    "PostingFBSListFilterWith",
    "PostingFBSListFilter",
    "PostingFBSListRequest",
    "PostingFBSListResult",
    "PostingFBSListResponse",
    "PostingFBSUnfulfilledListRequest",
    "PostingFBSUnfulfilledListResponse",
    "PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate",
    "PostingFBSUnfulfilledListFilterWith",
    "PostingFBSUnfulfilledListFilter",
    "PostingFBSUnfulfilledListResult",
]

from .entities import PostingFBSAddressee, PostingFBSAnalyticsData, PostingFBSBarcodes, PostingFBSCancellation, \
    PostingFBSCustomer, PostingFBSCustomerAddress, PostingFBSDeliveryMethod, PostingFBSFinancialData, \
    PostingFBSFinancialDataProducts, PostingFBSLegalInfo, PostingFBSOptional, PostingFBSPosting, PostingFBSProducts, \
    PostingFBSRequirements, PostingFBSTariffication
from .v3__posting_fbs_list import PostingFBSListRequestFilterLastChangedStatusDate, PostingFBSListFilterWith, \
    PostingFBSListFilter, PostingFBSListRequest, PostingFBSListResult, PostingFBSListResponse
from .v3__posting_fbs_unfulfilled_list import (
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse,
    PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate,
    PostingFBSUnfulfilledListFilterWith,
    PostingFBSUnfulfilledListFilter,
    PostingFBSUnfulfilledListResult,
)