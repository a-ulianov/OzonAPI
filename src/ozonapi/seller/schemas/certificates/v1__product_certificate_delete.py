"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateDelete"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificateDeleteRequest(BaseModel):
    """Описывает схему запроса на удаление сертификата.

    Attributes:
        certificate_id: Идентификатор сертификата
    """
    certificate_id: int = Field(
        ..., description="Идентификатор сертификата."
    )


class ProductCertificateDeleteResult(BaseModel):
    """Результат удаления сертификата.

    Attributes:
        is_delete: Признак удаления сертификата
        error_message: Описание ошибок при удалении сертификата
    """
    is_delete: Optional[bool] = Field(
        None, description="Удалён ли сертификат: `true` — удалён."
    )
    error_message: Optional[str] = Field(
        None, description="Описание ошибок при удалении сертификата."
    )


class ProductCertificateDeleteResponse(BaseModel):
    """Описывает схему ответа на запрос удаления сертификата.

    Attributes:
        result: Результат удаления сертификата
    """
    result: Optional[ProductCertificateDeleteResult] = Field(
        None, description="Результат удаления сертификата."
    )
