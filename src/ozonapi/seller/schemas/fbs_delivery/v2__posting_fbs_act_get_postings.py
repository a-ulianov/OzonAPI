"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActGetPostings"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSActGetPostingsRequest(BaseModel):
    """Описывает схему запроса на получение списка отправлений в акте.

    Attributes:
        id: Идентификатор акта
    """
    id: int = Field(
        ..., description="Идентификатор акта (можно получить методом `posting_fbs_act_create()`)."
    )


class PostingFBSActGetPostingsProduct(BaseModel):
    """Товар в отправлении из акта.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon — SKU
    """
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[str] = Field(
        None, description="Цена товара."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара в отправлении."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class PostingFBSActGetPostingsResult(BaseModel):
    """Информация об отправлении в акте.

    Attributes:
        id: Идентификатор акта
        multi_box_qty: Количество коробок, в которые упакован товар
        posting_number: Номер отправления
        status: Статус отправления
        seller_error: Расшифровка кода ошибки
        updated_at: Дата и время обновления записи об отправлении
        created_at: Дата и время создания записи об отправлении
        products: Список товаров в отправлении
    """
    id: Optional[int] = Field(
        None, description="Идентификатор акта."
    )
    multi_box_qty: Optional[int] = Field(
        None, description="Количество коробок, в которые упакован товар."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    status: Optional[str] = Field(
        None, description="Статус отправления."
    )
    seller_error: Optional[str] = Field(
        None, description="Расшифровка кода ошибки."
    )
    updated_at: Optional[str] = Field(
        None, description="Дата и время обновления записи об отправлении."
    )
    created_at: Optional[str] = Field(
        None, description="Дата и время создания записи об отправлении."
    )
    products: Optional[list[PostingFBSActGetPostingsProduct]] = Field(
        None, description="Список товаров в отправлении."
    )


class PostingFBSActGetPostingsResponse(BaseModel):
    """Описывает схему ответа на запрос списка отправлений в акте.

    Attributes:
        result: Информация об отправлениях
    """
    result: Optional[list[PostingFBSActGetPostingsResult]] = Field(
        None, description="Информация об отправлениях."
    )
