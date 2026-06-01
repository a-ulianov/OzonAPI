"""Схемы метода posting_unpaid_legal_product_list (неоплаченные товары ЮЛ, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingUnpaidLegalProductListRequest(BaseModel):
    """Параметры запроса списка неоплаченных товаров юридических лиц.

    Attributes:
        cursor: Указатель для следующей выборки
        limit: Количество значений в ответе
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для следующей выборки."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")


class PostingUnpaidLegalProduct(BaseModel):
    """Неоплаченный товар, заказанный юридическим лицом.

    Attributes:
        product_id: Идентификатор товара
        offer_id: Идентификатор товара в системе продавца — артикул
        quantity: Количество товара
        name: Название товара
        image_url: Ссылка на изображение товара
    """
    product_id: Optional[int] = Field(None, description="Идентификатор товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    quantity: Optional[int] = Field(None, description="Количество товара.")
    name: Optional[str] = Field(None, description="Название товара.")
    image_url: Optional[str] = Field(
        None, description="Ссылка на изображение товара."
    )


class PostingUnpaidLegalProductListResponse(BaseModel):
    """Ответ со списком неоплаченных товаров юридических лиц.

    Attributes:
        products: Неоплаченные товары
        cursor: Указатель для следующей выборки
    """
    products: Optional[list[PostingUnpaidLegalProduct]] = Field(
        None, description="Неоплаченные товары."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для следующей выборки."
    )
