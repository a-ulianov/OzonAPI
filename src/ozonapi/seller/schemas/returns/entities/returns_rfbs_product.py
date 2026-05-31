"""Общая модель товара в rFBS-возвратах."""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsRfbsProduct(BaseModel):
    """Товар в заявке на возврат rFBS.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        sku: Идентификатор товара в системе Ozon — SKU
        price: Цена товара
        currency_code: Валюта цены
    """
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    price: Optional[int] = Field(
        None, description="Цена товара."
    )
    currency_code: Optional[str] = Field(
        None, description="Валюта ваших цен."
    )
