"""Описывает модели раздела «Сертификаты брендов».
https://docs.ozon.ru/api/seller/#tag/BrandAPI
"""
__all__ = [
    "BrandCertification",
    "BrandCompanyCertificationListRequest",
    "BrandCompanyCertificationListResult",
    "BrandCompanyCertificationListResponse",
]

from .v1__brand_company_certification_list import (
    BrandCertification,
    BrandCompanyCertificationListRequest,
    BrandCompanyCertificationListResponse,
    BrandCompanyCertificationListResult,
)
