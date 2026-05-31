"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_SplitPosting"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductFbsSplit(BaseModel):
    """Товар в отправлении при разделении заказа.

    Attributes:
        product_id: Идентификатор товара в системе Ozon — SKU
        quantity: Количество экземпляров
    """
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    quantity: Optional[int] = Field(
        None, description="Количество экземпляров."
    )


class PostingFBSSplitRequestPosting(BaseModel):
    """Отправление, на которое поделится заказ.

    Attributes:
        products: Список товаров в заказе
    """
    products: list[ProductFbsSplit] = Field(
        ..., description="Список товаров в заказе."
    )


class PostingFBSSplitRequest(BaseModel):
    """Описывает схему запроса на разделение заказа на отправления без сборки.

    Attributes:
        posting_number: Номер отправления
        postings: Список отправлений, на которые поделится заказ
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    postings: list[PostingFBSSplitRequestPosting] = Field(
        ..., description="Список отправлений, на которые поделится заказ."
    )


class PostingFBSSplitResponsePosting(BaseModel):
    """Отправление, на которое разделился заказ.

    Attributes:
        posting_number: Номер отправления
        products: Список товаров в отправлении
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    products: Optional[list[ProductFbsSplit]] = Field(
        None, description="Список товаров в отправлении."
    )


class PostingFBSSplitResponseParent(BaseModel):
    """Изначальное отправление, которое было разделено.

    Attributes:
        posting_number: Номер изначального отправления
        products: Список товаров в отправлении
    """
    posting_number: Optional[str] = Field(
        None, description="Номер изначального отправления."
    )
    products: Optional[list[ProductFbsSplit]] = Field(
        None, description="Список товаров в отправлении."
    )


class PostingFBSSplitResponse(BaseModel):
    """Описывает схему ответа на запрос разделения заказа.

    Attributes:
        parent_posting: Изначальное отправление
        postings: Список отправлений, на которые разделился заказ
    """
    parent_posting: Optional[PostingFBSSplitResponseParent] = Field(
        None, description="Изначальное отправление."
    )
    postings: Optional[list[PostingFBSSplitResponsePosting]] = Field(
        None, description="Список отправлений, на которые разделился заказ."
    )
