"""Схемы метода product_stairway_discount_by_quantity_get (информация о скидке от количества, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Stairway


class ProductStairwayDiscountByQuantityGetRequest(BaseModel):
    """Параметры запроса информации о скидке от количества.

    Attributes:
        skus: Идентификаторы товаров в системе Ozon — SKU
    """
    skus: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )


class ProductStairwayDiscountByQuantityGetItem(BaseModel):
    """Информация о скидке от количества для товара.

    Attributes:
        enabled: Признак включения скидки
        sku: Идентификатор товара в системе Ozon — SKU
        stairway: Лестница скидок
        status: Статус настройки скидки
    """
    enabled: Optional[bool] = Field(None, description="Признак включения скидки.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    stairway: Optional[Stairway] = Field(None, description="Лестница скидок.")
    status: Optional[str] = Field(None, description="Статус настройки скидки.")


class ProductStairwayDiscountByQuantityGetResponse(BaseModel):
    """Ответ с информацией о скидке от количества.

    Attributes:
        stairways: Настройки скидок по товарам
    """
    stairways: Optional[list[ProductStairwayDiscountByQuantityGetItem]] = Field(
        None, description="Настройки скидок по товарам."
    )
