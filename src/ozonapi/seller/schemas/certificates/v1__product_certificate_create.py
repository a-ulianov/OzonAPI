"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateCreate"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificateCreateRequest(BaseModel):
    """Описывает схему запроса на добавление сертификатов для товаров.

    Notes:
        • Запрос отправляется как `multipart/form-data`: текстовые поля плюс файлы `files`.

    Attributes:
        files: Массив сертификатов для товара (содержимое файлов в виде байтов)
        name: Название сертификата (максимум 100 символов)
        number: Номер сертификата (максимум 100 символов)
        type_code: Тип сертификата
        issue_date: Дата начала действия сертификата
        accordance_type_code: Тип соответствия требованиям
        expire_date: Дата окончания действия сертификата
    """
    files: list[bytes] = Field(
        ..., description="Массив сертификатов для товара (содержимое файлов в виде байтов)."
    )
    name: str = Field(
        ..., description="Название сертификата. Максимум 100 символов."
    )
    number: str = Field(
        ..., description="Номер сертификата. Максимум 100 символов."
    )
    type_code: str = Field(
        ..., description="Тип сертификата."
    )
    issue_date: str = Field(
        ..., description="Дата начала действия сертификата."
    )
    accordance_type_code: Optional[str] = Field(
        None, description="Тип соответствия требованиям."
    )
    expire_date: Optional[str] = Field(
        None, description="Дата окончания действия сертификата."
    )


class ProductCertificateCreateResponse(BaseModel):
    """Описывает схему ответа на запрос добавления сертификатов.

    Attributes:
        id: Идентификатор созданного сертификата
    """
    id: Optional[int] = Field(
        None, description="Идентификатор созданного сертификата."
    )
