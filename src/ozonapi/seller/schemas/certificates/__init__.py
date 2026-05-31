"""Описывает модели методов раздела Сертификаты качества.
https://docs.ozon.ru/api/seller/#tag/CertificateAPI
"""
__all__ = [
    "Certificate",
    "CertificateCodeName",
    "CertificateNameValue",
    "ProductCertificateAccordanceTypesResponse",
    "ProductCertificateAccordanceTypesListResponse",
    "ProductCertificateAccordanceTypesListResult",
    "ProductCertificateAccordanceType",
    "ProductCertificateTypesResponse",
    "ProductCertificationListRequest",
    "ProductCertificationListResponse",
    "ProductCertificationListItem",
    "ProductCertificationListV1Request",
    "ProductCertificationListV1Response",
    "ProductCertificationListV1Result",
    "ProductCertificationListV1Item",
    "ProductCertificateInfoRequest",
    "ProductCertificateInfoResponse",
    "ProductCertificateListRequest",
    "ProductCertificateListResponse",
    "ProductCertificateListResult",
    "ProductCertificateProductStatusListResponse",
    "ProductCertificateProductsListRequest",
    "ProductCertificateProductsListResponse",
    "ProductCertificateProductsListResult",
    "ProductCertificateProductsListItem",
    "ProductCertificateRejectionReasonsListResponse",
    "ProductCertificateStatusListResponse",
    "ProductCertificateCreateRequest",
    "ProductCertificateCreateResponse",
    "ProductCertificateBindRequest",
    "ProductCertificateBindResponse",
    "ProductCertificateDeleteRequest",
    "ProductCertificateDeleteResponse",
    "ProductCertificateDeleteResult",
    "ProductCertificateUnbindRequest",
    "ProductCertificateUnbindResponse",
    "ProductCertificateUnbindItem",
]

from .entities import Certificate, CertificateCodeName, CertificateNameValue
from .v1__product_certificate_accordance_types import (
    ProductCertificateAccordanceTypesResponse,
)
from .v1__product_certificate_bind import (
    ProductCertificateBindRequest,
    ProductCertificateBindResponse,
)
from .v1__product_certificate_create import (
    ProductCertificateCreateRequest,
    ProductCertificateCreateResponse,
)
from .v1__product_certificate_delete import (
    ProductCertificateDeleteRequest,
    ProductCertificateDeleteResponse,
    ProductCertificateDeleteResult,
)
from .v1__product_certificate_info import (
    ProductCertificateInfoRequest,
    ProductCertificateInfoResponse,
)
from .v1__product_certificate_list import (
    ProductCertificateListRequest,
    ProductCertificateListResponse,
    ProductCertificateListResult,
)
from .v1__product_certificate_product_status_list import (
    ProductCertificateProductStatusListResponse,
)
from .v1__product_certificate_products_list import (
    ProductCertificateProductsListItem,
    ProductCertificateProductsListRequest,
    ProductCertificateProductsListResponse,
    ProductCertificateProductsListResult,
)
from .v1__product_certificate_rejection_reasons_list import (
    ProductCertificateRejectionReasonsListResponse,
)
from .v1__product_certificate_status_list import (
    ProductCertificateStatusListResponse,
)
from .v1__product_certificate_types import ProductCertificateTypesResponse
from .v1__product_certificate_unbind import (
    ProductCertificateUnbindItem,
    ProductCertificateUnbindRequest,
    ProductCertificateUnbindResponse,
)
from .v1__product_certification_list import (
    ProductCertificationListV1Item,
    ProductCertificationListV1Request,
    ProductCertificationListV1Response,
    ProductCertificationListV1Result,
)
from .v2__product_certificate_accordance_types_list import (
    ProductCertificateAccordanceType,
    ProductCertificateAccordanceTypesListResponse,
    ProductCertificateAccordanceTypesListResult,
)
from .v2__product_certification_list import (
    ProductCertificationListItem,
    ProductCertificationListRequest,
    ProductCertificationListResponse,
)
