"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateAccordanceTypesV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificateAccordanceType(BaseModel):
    """Тип соответствия требованиям.

    Attributes:
        code: Код типа соответствия требованиям
        title: Описание типа соответствия требованиям
    """
    code: Optional[str] = Field(
        None, description="Код типа соответствия требованиям."
    )
    title: Optional[str] = Field(
        None, description="Описание типа соответствия требованиям."
    )


class ProductCertificateAccordanceTypesListResult(BaseModel):
    """Типы соответствия требованиям.

    Attributes:
        base: Основные типы соответствия требованиям
        hazard: Типы соответствия требованиям для опасных товаров
    """
    base: Optional[list[ProductCertificateAccordanceType]] = Field(
        None, description="Основные типы соответствия требованиям."
    )
    hazard: Optional[list[ProductCertificateAccordanceType]] = Field(
        None, description="Типы соответствия требованиям для опасных товаров."
    )


class ProductCertificateAccordanceTypesListResponse(BaseModel):
    """Описывает схему ответа на запрос списка типов соответствия требованиям (v2).

    Attributes:
        result: Типы соответствия требованиям
    """
    result: Optional[ProductCertificateAccordanceTypesListResult] = Field(
        None, description="Типы соответствия требованиям."
    )
