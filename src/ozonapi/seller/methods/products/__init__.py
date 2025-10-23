__all__ = ["SellerProductAPI", ]

from .product_archive import ProductArchiveMixin
from .product_attributes_update import ProductAttributesUpdateMixin
from .product_delete import ProductDeleteMixin
from .product_import import ProductImportMixin
from .product_import_by_sku import ProductImportBySkuMixin
from .product_import_info import ProductImportInfoMixin
from .product_info_attributes import ProductInfoAttributesMixin
from .product_info_description import ProductInfoDescriptionMixin
from .product_info_limit import ProductInfoLimitMixin
from .product_info_list import ProductInfoListMixin
from .product_info_subscription import ProductInfoSubscriptionMixin
from .product_list import ProductListMixin
from .product_pictures_import import ProductPicturesImportMixin
from .product_pictures_info import ProductPicturesInfoMixin
from .product_rating_by_sku import ProductRatingBySkuMixin
from .product_related_sku_get import ProductRelatedSkuGetMixin
from .product_unarchive import ProductUnarchiveMixin
from .product_update_offer_id import ProductUpdateOfferIdMixin


class SellerProductAPI(
    ProductArchiveMixin,
    ProductAttributesUpdateMixin,
    ProductDeleteMixin,
    ProductImportBySkuMixin,
    ProductImportInfoMixin,
    ProductImportMixin,
    ProductInfoAttributesMixin,
    ProductInfoDescriptionMixin,
    ProductInfoLimitMixin,
    ProductInfoListMixin,
    ProductInfoSubscriptionMixin,
    ProductListMixin,
    ProductPicturesImportMixin,
    ProductPicturesInfoMixin,
    ProductRatingBySkuMixin,
    ProductRelatedSkuGetMixin,
    ProductUnarchiveMixin,
    ProductUpdateOfferIdMixin,
):
    """Реализует методы раздела Загрузка и обновление товаров.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/ProductAPI
    """
    pass