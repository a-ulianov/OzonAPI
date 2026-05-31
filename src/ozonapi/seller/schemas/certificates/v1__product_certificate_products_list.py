"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateProductsList"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductCertificateProductsListRequest(BaseModel):
    """Описывает схему запроса на получение списка товаров, привязанных к сертификату.

    Attributes:
        certificate_id: Идентификатор сертификата
        page: Номер страницы
        page_size: Количество объектов на странице
        product_status_code: Статус проверки товара при привязке
    """
    certificate_id: int = Field(
        ..., description="Идентификатор сертификата."
    )
    page: int = Field(
        ..., description="Номер страницы, с которой выводить результаты."
    )
    page_size: int = Field(
        ..., description="Количество объектов на странице."
    )
    product_status_code: Optional[str] = Field(
        None, description="Статус проверки товара при привязке к сертификату."
    )


class ProductCertificateProductsListItem(BaseModel):
    """Товар, привязанный к сертификату.

    Attributes:
        product_id: Идентификатор товара в системе Ozon
        product_status_code: Статус обработки товара при привязке
    """
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon."
    )
    product_status_code: Optional[str] = Field(
        None, description="Статус обработки товара при привязке."
    )


class ProductCertificateProductsListResult(BaseModel):
    """Результат запроса списка товаров, привязанных к сертификату.

    Attributes:
        items: Список товаров
        count: Количество найденных товаров
    """
    items: Optional[list[ProductCertificateProductsListItem]] = Field(
        None, description="Список товаров."
    )
    count: Optional[int] = Field(
        None, description="Количество найденных товаров."
    )


class ProductCertificateProductsListResponse(BaseModel):
    """Описывает схему ответа на запрос списка товаров, привязанных к сертификату.

    Attributes:
        result: Результат запроса
    """
    result: Optional[ProductCertificateProductsListResult] = Field(
        None, description="Результат запроса."
    )
