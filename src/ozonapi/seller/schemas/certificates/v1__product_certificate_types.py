"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateTypes"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CertificateNameValue


class ProductCertificateTypesResponse(BaseModel):
    """Описывает схему ответа на запрос справочника типов документов.

    Attributes:
        result: Список типов и названий документов
    """
    result: Optional[list[CertificateNameValue]] = Field(
        None, description="Список типов и названий документов."
    )
