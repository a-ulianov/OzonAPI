"""Схемы метода product_visibility_info (информация о видимости товара, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class ProductVisibilityInfoRequest(BaseModel):
    """Параметры запроса информации о видимости товара.

    Attributes:
        skus: Идентификаторы товаров в системе Ozon — SKU
    """
    skus: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )


class ProductVisibilityInfoItem(BaseModel):
    """Информация о видимости товара.

    Attributes:
        showcases_visibility: Видимость на витринах
        sku: Идентификатор товара в системе Ozon — SKU
    """
    showcases_visibility: Optional[str] = Field(
        None, description="Видимость на витринах."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class ProductVisibilityInfoResponse(BaseModel):
    """Ответ с информацией о видимости товаров.

    Attributes:
        items: Информация о видимости товаров
    """
    items: Optional[list[ProductVisibilityInfoItem]] = Field(
        None, description="Информация о видимости товаров."
    )
