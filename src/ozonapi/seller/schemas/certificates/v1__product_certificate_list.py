"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Certificate


class ProductCertificateListRequest(BaseModel):
    """Описывает схему запроса на получение списка сертификатов.

    Attributes:
        page: Страница, с которой выводить результаты
        page_size: Количество объектов на странице
        offer_id: Идентификатор товара в системе продавца
        status: Статус сертификата
        type: Тип сертификата
    """
    page: int = Field(
        ..., description="Страница, с которой следует выводить результаты."
    )
    page_size: int = Field(
        ..., description="Количество объектов на странице."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    status: Optional[str] = Field(
        None, description="Статус сертификата."
    )
    type: Optional[str] = Field(
        None, description="Тип сертификата."
    )


class ProductCertificateListResult(BaseModel):
    """Результат запроса списка сертификатов.

    Attributes:
        certificates: Информация о сертификатах
        page_count: Количество страниц
    """
    certificates: Optional[list[Certificate]] = Field(
        None, description="Информация о сертификатах."
    )
    page_count: Optional[int] = Field(
        None, description="Количество страниц."
    )


class ProductCertificateListResponse(BaseModel):
    """Описывает схему ответа на запрос списка сертификатов.

    Attributes:
        result: Результат запроса
    """
    result: Optional[ProductCertificateListResult] = Field(
        None, description="Результат запроса."
    )
