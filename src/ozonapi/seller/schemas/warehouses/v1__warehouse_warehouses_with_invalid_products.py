"""Схемы метода warehouse_warehouses_with_invalid_products (склады с ограничениями, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseWithInvalidProductsResponse(BaseModel):
    """Ответ со списком складов с ограниченными для доставки товарами.

    Attributes:
        warehouse_ids: Идентификаторы складов
    """
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )
