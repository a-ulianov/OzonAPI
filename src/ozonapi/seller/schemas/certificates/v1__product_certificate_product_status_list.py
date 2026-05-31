"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateProductStatusList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CertificateCodeName


class ProductCertificateProductStatusListResponse(BaseModel):
    """Описывает схему ответа на запрос списка возможных статусов товаров.

    Attributes:
        result: Список статусов товаров
    """
    result: Optional[list[CertificateCodeName]] = Field(
        None, description="Список статусов товаров."
    )
