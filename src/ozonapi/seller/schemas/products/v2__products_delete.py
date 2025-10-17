"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_DeleteProducts"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductDeleteRequestItem(BaseModel):
    """Идентификатор товара в системе продавца.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
    """
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )


class ProductsDeleteRequest(BaseModel):
    """Описывает схему запроса на удаление товаров.

    Attributes:
        products: Список товаров для удаления (максимум 500)
    """
    products: list[ProductDeleteRequestItem] = Field(
        ..., description="Список товаров для удаления (максимум 500)",
        max_length=500,
    )


class ProductsDeleteStatusItem(BaseModel):
    """Статус обработки запроса.

    Attributes:
        error: Причина ошибки, если возникла
        is_deleted: Признак успешного удаления товара
        offer_id: Идентификатор товара в системе продавца
    """
    error: Optional[str] = Field(
        None, description="Причина ошибки, если возникла"
    )
    is_deleted: bool = Field(
        ..., description="Если запрос выполнен без ошибок и товары удалены — true."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )


class ProductsDeleteResponse(BaseModel):
    """Описывает схему ответа на запрос об удалении товаров.

    Attributes:
        status: Список статусов обработки запроса
    """
    status: list[ProductsDeleteStatusItem] = Field(
        ..., description="Список статусов обработки запроса."
    )