"""Схемы метода supply_order_content_update (редактирование состава, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderContentUpdateItem(BaseModel):
    """Товар нового товарного состава заявки на поставку.

    Attributes:
        quant: Размер кванта
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    quant: Optional[int] = Field(None, description="Размер кванта.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class SupplyOrderContentUpdateRequest(BaseModel):
    """Параметры запроса редактирования товарного состава.

    Attributes:
        items: Новый товарный состав
        order_id: Идентификатор заявки на поставку
        supply_id: Идентификатор поставки
    """
    items: Optional[list[SupplyOrderContentUpdateItem]] = Field(
        None, description="Новый товарный состав."
    )
    order_id: int = Field(..., description="Идентификатор заявки на поставку.")
    supply_id: int = Field(..., description="Идентификатор поставки.")


class SupplyOrderContentUpdateResponse(BaseModel):
    """Ответ на редактирование товарного состава.

    Attributes:
        errors: Ошибки редактирования
        operation_id: Идентификатор операции редактирования
    """
    errors: Optional[list[str]] = Field(
        None, description="Ошибки редактирования."
    )
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции редактирования."
    )
