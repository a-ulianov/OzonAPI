"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateRejectionReasonsList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CertificateCodeName


class ProductCertificateRejectionReasonsListResponse(BaseModel):
    """Описывает схему ответа на запрос возможных причин отклонения сертификата.

    Attributes:
        result: Причины отклонения сертификата
    """
    result: Optional[list[CertificateCodeName]] = Field(
        None, description="Причины отклонения сертификата."
    )
