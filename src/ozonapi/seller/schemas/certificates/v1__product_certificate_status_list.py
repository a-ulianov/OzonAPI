"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateStatusList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CertificateCodeName


class ProductCertificateStatusListResponse(BaseModel):
    """Описывает схему ответа на запрос возможных статусов сертификатов.

    Attributes:
        result: Список возможных статусов сертификатов
    """
    result: Optional[list[CertificateCodeName]] = Field(
        None, description="Список возможных статусов сертификатов."
    )
