"""Композиция миксинов методов раздела Сертификаты качества.

Объединяет методы работы с сертификатами качества товаров
в единый класс :class:`SellerCertificateAPI`.
"""

from ...core import APIManager
from .product_certificate_accordance_types import ProductCertificateAccordanceTypesMixin
from .product_certificate_accordance_types_list import (
    ProductCertificateAccordanceTypesListMixin,
)
from .product_certificate_bind import ProductCertificateBindMixin
from .product_certificate_create import ProductCertificateCreateMixin
from .product_certificate_delete import ProductCertificateDeleteMixin
from .product_certificate_info import ProductCertificateInfoMixin
from .product_certificate_list import ProductCertificateListMixin
from .product_certificate_product_status_list import (
    ProductCertificateProductStatusListMixin,
)
from .product_certificate_products_list import ProductCertificateProductsListMixin
from .product_certificate_rejection_reasons_list import (
    ProductCertificateRejectionReasonsListMixin,
)
from .product_certificate_status_list import ProductCertificateStatusListMixin
from .product_certificate_types import ProductCertificateTypesMixin
from .product_certificate_unbind import ProductCertificateUnbindMixin
from .product_certification_list import ProductCertificationListMixin
from .product_certification_list_v1 import ProductCertificationListV1Mixin


class SellerCertificateAPI(
    ProductCertificateAccordanceTypesMixin,
    ProductCertificateAccordanceTypesListMixin,
    ProductCertificateBindMixin,
    ProductCertificateCreateMixin,
    ProductCertificateDeleteMixin,
    ProductCertificateInfoMixin,
    ProductCertificateListMixin,
    ProductCertificateProductStatusListMixin,
    ProductCertificateProductsListMixin,
    ProductCertificateRejectionReasonsListMixin,
    ProductCertificateStatusListMixin,
    ProductCertificateTypesMixin,
    ProductCertificateUnbindMixin,
    ProductCertificationListMixin,
    ProductCertificationListV1Mixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Сертификаты качества.

    Notes:
        • Объединяет методы работы с сертификатами: справочники, создание, привязка/отвязка
          товаров, список и информация о сертификатах.

    References:
        • https://docs.ozon.ru/api/seller/#tag/CertificateAPI
    """

    pass
