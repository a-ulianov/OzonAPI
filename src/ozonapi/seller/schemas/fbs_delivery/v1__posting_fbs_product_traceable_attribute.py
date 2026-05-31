"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFbsProductTraceableAttribute"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSProductTraceableAttributeRequest(BaseModel):
    """Описывает схему запроса на получение незаполненных атрибутов прослеживаемых товаров.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )


class PostingFBSProductTraceableAttributeProduct(BaseModel):
    """Товар в отправлении с обязательными атрибутами.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        required_attributes: Обязательные атрибуты
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    required_attributes: Optional[list[str]] = Field(
        None, description="Обязательные атрибуты."
    )


class PostingFBSProductTraceableAttributeResponse(BaseModel):
    """Описывает схему ответа на запрос незаполненных атрибутов прослеживаемых товаров.

    Attributes:
        products: Список товаров в отправлении
    """
    products: Optional[list[PostingFBSProductTraceableAttributeProduct]] = Field(
        None, description="Список товаров в отправлении."
    )
