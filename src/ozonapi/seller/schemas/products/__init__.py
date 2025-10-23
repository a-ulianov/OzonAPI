"""Описывает модели методов раздела Загрузка и обновление товаров.
https://docs.ozon.ru/api/seller/?__rr=1#tag/ProductAPI
"""
__all__ = [
    "ProductArchiveRequest",
    "ProductArchiveResponse",
    "ProductAttributesUpdateRequest",
    "ProductAttributesUpdateResponse",
    "ProductAttributesUpdateItem",
    "ProductAttributesUpdateItemAttribute",
    "ProductAttributesUpdateItemAttributeValue",
    "ProductsDeleteRequest",
    "ProductsDeleteResponse",
    "ProductDeleteRequestItem",
    "ProductsDeleteStatusItem",
    "ProductImportBySkuRequest",
    "ProductImportBySkuResponse",
    "ProductImportBySkuRequestItem",
    "ProductImportInfoRequest",
    "ProductImportInfoResponse",
    "ProductImportInfoResult",
    "ProductImportInfoItem",
    "ProductImportInfoItemError",
    "ProductImportRequest",
    "ProductImportResponse",
    "ProductImportItem",
    "ProductImportResponseResult",
    "ProductImportRequestItemPDFListItem",
    "ProductImportRequestItemPromotion",
    "ProductInfoAttributesRequest",
    "ProductInfoAttributesResponse",
    "ProductInfoAttributesItem",
    "ProductInfoAttributesFilter",
    "ProductInfoAttributesPdfFile",
    "ProductInfoAttributesModelInfo",
    "ProductInfoDescriptionRequest",
    "ProductInfoDescriptionResponse",
    "ProductInfoLimitResponse",
    "ProductInfoListRequest",
    "ProductInfoListResponse",
    "ProductInfoListItem",
    "ProductInfoListError",
    "ProductInfoListErrorTexts",
    "ProductInfoListErrorTextsParams",
    "ProductInfoListCommission",
    "ProductInfoListPriceIndexData",
    "ProductInfoListPriceIndexes",
    "ProductInfoListModelInfo",
    "ProductInfoListSource",
    "ProductInfoListStockStatus",
    "ProductInfoListStatuses",
    "ProductInfoListStocks",
    "ProductInfoListVisibilityDetails",
    "ProductInfoSubscriptionRequest",
    "ProductInfoSubscriptionResponse",
    "ProductInfoSubscriptionItem",
    "ProductListRequest",
    "ProductListResponse",
    "ProductListFilter",
    "ProductListResponseItem",
    "ProductListResponseResult",
    "ProductListQuants",
    "ProductPicturesImportRequest",
    "ProductPicturesImportResponse",
    "ProductPicturesInfoRequest",
    "ProductPicturesInfoResponse",
    "ProductPicturesInfoItem",
    "ProductPicturesInfoError",
    "ProductRatingBySkuRequest",
    "ProductRatingBySkuResponse",
    "ProductRatingBySkuItem",
    "ProductRatingBySkuItemGroup",
    "ProductRatingBySkuItemGroupCondition",
    "ProductRatingBySkuItemGroupImproveAttribute",
    "ProductRelatedSkuGetRequest",
    "ProductRelatedSkuGetResponse",
    "ProductRelatedSkuGetItem",
    "ProductRelatedSkuGetError",
    "ProductUnarchiveRequest",
    "ProductUnarchiveResponse",
    "ProductUpdateOfferIdRequest",
    "ProductUpdateOfferIdResponse",
    "ProductUpdateOfferIdRequestItem",
    "ProductUpdateOfferIdError",
]

from .v1__product_archive import ProductArchiveRequest, ProductArchiveResponse
from .v1__product_attributes_update import (
    ProductAttributesUpdateResponse, 
    ProductAttributesUpdateRequest,
    ProductAttributesUpdateItem,
    ProductAttributesUpdateItemAttribute,
    ProductAttributesUpdateItemAttributeValue,
)
from .v1__product_import_by_sku import (
    ProductImportBySkuResponse, 
    ProductImportBySkuRequest,
    ProductImportBySkuRequestItem,
)
from .v1__product_import_info import (
    ProductImportInfoResponse, 
    ProductImportInfoRequest,
    ProductImportInfoResult,
    ProductImportInfoItem,
    ProductImportInfoItemError,
)
from .v1__product_info_description import ProductInfoDescriptionResponse, ProductInfoDescriptionRequest
from .v1__product_info_subscription import (
    ProductInfoSubscriptionResponse, 
    ProductInfoSubscriptionRequest,
    ProductInfoSubscriptionItem,
)
from .v1__product_pictures_import import ProductPicturesImportResponse, ProductPicturesImportRequest
from .v1__product_rating_by_sku import (
    ProductRatingBySkuResponse, 
    ProductRatingBySkuRequest,
    ProductRatingBySkuItem,
    ProductRatingBySkuItemGroup,
    ProductRatingBySkuItemGroupCondition,
    ProductRatingBySkuItemGroupImproveAttribute,
)
from .v1__product_related_sku_get import (
    ProductRelatedSkuGetResponse, 
    ProductRelatedSkuGetRequest,
    ProductRelatedSkuGetItem,
    ProductRelatedSkuGetError,
)
from .v1__product_unarchive import ProductUnarchiveRequest, ProductUnarchiveResponse
from .v1__product_update_offer_id import (
    ProductUpdateOfferIdResponse, 
    ProductUpdateOfferIdRequest,
    ProductUpdateOfferIdRequestItem,
    ProductUpdateOfferIdError,
)
from .v2__product_pictures_info import (
    ProductPicturesInfoResponse, 
    ProductPicturesInfoRequest,
    ProductPicturesInfoItem,
    ProductPicturesInfoError,
)
from .v2__products_delete import (
    ProductsDeleteResponse, 
    ProductsDeleteRequest,
    ProductDeleteRequestItem,
    ProductsDeleteStatusItem,
)
from .v3__product_import import (
    ProductImportResponse, 
    ProductImportRequest,
    ProductImportItem,
    ProductImportResponseResult,
    ProductImportRequestItemPDFListItem,
    ProductImportRequestItemPromotion,
)
from .v3__product_info_list import (
    ProductInfoListResponse, 
    ProductInfoListRequest,
    ProductInfoListItem,
    ProductInfoListError,
    ProductInfoListErrorTexts,
    ProductInfoListErrorTextsParams,
    ProductInfoListCommission,
    ProductInfoListPriceIndexData,
    ProductInfoListPriceIndexes,
    ProductInfoListModelInfo,
    ProductInfoListSource,
    ProductInfoListStockStatus,
    ProductInfoListStatuses,
    ProductInfoListStocks,
    ProductInfoListVisibilityDetails,
)
from .v3__product_list import (
    ProductListResponse, 
    ProductListRequest,
    ProductListFilter,
    ProductListResponseItem,
    ProductListResponseResult,
    ProductListQuants,
)
from .v4__product_info_limit import ProductInfoLimitResponse
from .v4__product_info_attributes import (
    ProductInfoAttributesResponse, 
    ProductInfoAttributesRequest,
    ProductInfoAttributesItem,
    ProductInfoAttributesFilter,
    ProductInfoAttributesPdfFile,
    ProductInfoAttributesModelInfo,
)