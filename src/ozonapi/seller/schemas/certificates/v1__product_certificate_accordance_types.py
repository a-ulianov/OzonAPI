"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateAccordanceTypes"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CertificateNameValue


class ProductCertificateAccordanceTypesResponse(BaseModel):
    """Описывает схему ответа на запрос списка типов соответствия требованиям (v1).

    Attributes:
        result: Список типов и названий соответствия требованиям
    """
    result: Optional[list[CertificateNameValue]] = Field(
        None, description="Список типов и названий соответствия требованиям."
    )
