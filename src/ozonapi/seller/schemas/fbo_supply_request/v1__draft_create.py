"""Схемы метода draft_create (создать черновик заявки на поставку, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyCreateType


class DraftCreateItem(BaseModel):
    """Товар в черновике заявки на поставку.

    Attributes:
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    quantity: int = Field(..., description="Количество товара.")
    sku: int = Field(..., description="Идентификатор товара в системе Ozon — SKU.")


class DraftCreateRequest(BaseModel):
    """Параметры запроса создания черновика заявки на поставку.

    Attributes:
        cluster_ids: Идентификаторы кластеров
        drop_off_point_warehouse_id: Идентификатор точки отгрузки
        items: Товары
        type: Тип поставки
    """
    cluster_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы кластеров."
    )
    drop_off_point_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор точки отгрузки."
    )
    items: list[DraftCreateItem] = Field(..., description="Товары.")
    type: SupplyCreateType = Field(..., description="Тип поставки.")


class DraftCreateResponse(BaseModel):
    """Ответ с идентификатором операции создания черновика.

    Attributes:
        operation_id: Идентификатор операции создания черновика
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции создания черновика."
    )
