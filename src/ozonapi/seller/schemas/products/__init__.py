"""Описывает модели методов раздела Загрузка и обновление товаров.
https://docs.ozon.ru/api/seller/?__rr=1#tag/ProductAPI
"""
__all__ = [
    "ProductArchiveRequest",
    "ProductArchiveResponse",
    "ProductAttributesUpdateRequest",
    "ProductAttributesUpdateResponse",
    "ProductsDeleteRequest",
    "ProductsDeleteResponse",
    "ProductImportBySkuRequest",
    "ProductImportBySkuResponse",
    "ProductImportInfoRequest",
    "ProductImportInfoResponse",
    "ProductImportRequest",
    "ProductImportResponse",
    "ProductInfoAttributesRequest",
    "ProductInfoAttributesResponse",
    "ProductInfoListRequest",
    "ProductInfoListResponse",
    "ProductInfoSubscriptionRequest",
    "ProductInfoSubscriptionResponse",
    "ProductListRequest",
    "ProductListResponse",
    "ProductPicturesInfoRequest",
    "ProductPicturesInfoResponse",
    "ProductRatingBySkuRequest",
    "ProductRatingBySkuResponse",
    "ProductRelatedSkuGetRequest",
    "ProductRelatedSkuGetResponse",
    "ProductUnarchiveRequest",
    "ProductUnarchiveResponse",
    "ProductUpdateOfferIdRequest",
    "ProductUpdateOfferIdResponse",
]

from .v1__product_archive import ProductArchiveRequest, ProductArchiveResponse
from .v1__product_attributes_update import ProductAttributesUpdateResponse, ProductAttributesUpdateRequest
from .v1__product_import_by_sku import ProductImportBySkuResponse, ProductImportBySkuRequest
from .v1__product_import_info import ProductImportInfoResponse, ProductImportInfoRequest
from .v1__product_info_subscription import ProductInfoSubscriptionResponse, ProductInfoSubscriptionRequest
from .v1__product_rating_by_sku import ProductRatingBySkuResponse, ProductRatingBySkuRequest
from .v1__product_related_sku_get import ProductRelatedSkuGetResponse, ProductRelatedSkuGetRequest
from .v1__product_unarchive import ProductUnarchiveRequest, ProductUnarchiveResponse
from .v1__product_update_offer_id import ProductUpdateOfferIdResponse, ProductUpdateOfferIdRequest
from .v2__product_pictures_info import ProductPicturesInfoResponse, ProductPicturesInfoRequest
from .v2__products_delete import ProductsDeleteResponse, ProductsDeleteRequest
from .v3__product_import import ProductImportResponse, ProductImportRequest
from .v3__product_info_list import ProductInfoListResponse, ProductInfoListRequest
from .v3__product_list import ProductListResponse, ProductListRequest
from .v4__product_info_attributes import ProductInfoAttributesResponse, ProductInfoAttributesRequest
