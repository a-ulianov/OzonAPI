"""Схемы метода product_visibility_set (настройка видимости товара, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.beta import ProductPlacement


class ProductVisibilitySetItemPlacement(BaseModel):
    """Настройка размещения товара.

    Attributes:
        placement: Витрина размещения
        sku: Идентификатор товара в системе Ozon — SKU
    """
    placement: Optional[ProductPlacement] = Field(
        None, description="Витрина размещения."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class ProductVisibilitySetRequest(BaseModel):
    """Параметры запроса настройки видимости товара.

    Attributes:
        item_placement: Настройки размещения товаров
    """
    item_placement: Optional[list[ProductVisibilitySetItemPlacement]] = Field(
        None, description="Настройки размещения товаров."
    )


class ProductVisibilitySetItem(BaseModel):
    """Результат настройки видимости товара.

    Attributes:
        select_permission: Право размещения на Ozon Селект
        seller_item_placement: Текущее размещение товара продавцом
        seller_item_placement_list: Список размещений товара продавцом
        showcases_visibility: Видимость на витринах
        showcases_visibility_list: Список видимости на витринах
        sku: Идентификатор товара в системе Ozon — SKU
        warnings: Предупреждения
    """
    select_permission: Optional[str] = Field(
        None, description="Право размещения на Ozon Селект."
    )
    seller_item_placement: Optional[str] = Field(
        None, description="Текущее размещение товара продавцом."
    )
    seller_item_placement_list: Optional[list[str]] = Field(
        None, description="Список размещений товара продавцом."
    )
    showcases_visibility: Optional[str] = Field(
        None, description="Видимость на витринах."
    )
    showcases_visibility_list: Optional[list[str]] = Field(
        None, description="Список видимости на витринах."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    warnings: Optional[list[str]] = Field(None, description="Предупреждения.")


class ProductVisibilitySetItemError(BaseModel):
    """Ошибка настройки видимости товара.

    Attributes:
        code: Код ошибки
        sku: Идентификатор товара в системе Ozon — SKU
    """
    code: Optional[str] = Field(None, description="Код ошибки.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class ProductVisibilitySetResponse(BaseModel):
    """Ответ на настройку видимости товара.

    Attributes:
        items: Результаты настройки
        items_errors: Ошибки настройки
    """
    items: Optional[list[ProductVisibilitySetItem]] = Field(
        None, description="Результаты настройки."
    )
    items_errors: Optional[list[ProductVisibilitySetItemError]] = Field(
        None, description="Ошибки настройки."
    )
