"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateInfo"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Certificate


class ProductCertificateInfoRequest(BaseModel):
    """Описывает схему запроса на получение информации о сертификате.

    Attributes:
        certificate_number: Идентификатор сертификата
    """
    certificate_number: str = Field(
        ..., description="Идентификатор сертификата."
    )


class ProductCertificateInfoResponse(BaseModel):
    """Описывает схему ответа на запрос информации о сертификате.

    Attributes:
        result: Информация о сертификате
    """
    result: Optional[Certificate] = Field(
        None, description="Информация о сертификате."
    )
