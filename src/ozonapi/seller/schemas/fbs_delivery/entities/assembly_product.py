"""Общая модель товара в списках сборки отгрузок и отправлений FBS."""
from typing import Optional

from pydantic import BaseModel, Field


class AssemblyProduct(BaseModel):
    """Товар в списке сборки.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        product_name: Название товара
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
        picture_url: Ссылка на изображение товара
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_name: Optional[str] = Field(
        None, description="Название товара."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    picture_url: Optional[str] = Field(
        None, description="Ссылка на изображение товара."
    )
