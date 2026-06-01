"""Общие сущности созданных поставок FBP."""
from typing import Optional

from pydantic import BaseModel, Field


class FbpBundleSummary(BaseModel):
    """Сводка по набору товаров поставки.

    Attributes:
        total_item_count: Количество уникальных товаров
        total_quantity: Общее количество единиц товара
        rounded_total_volume_in_litres: Округлённый суммарный объём, л
    """

    total_item_count: Optional[int] = Field(
        None, description="Количество уникальных товаров."
    )
    total_quantity: Optional[int] = Field(
        None, description="Общее количество единиц товара."
    )
    rounded_total_volume_in_litres: Optional[float] = Field(
        None, description="Округлённый суммарный объём набора, л."
    )


class FbpArchiveSkuSummary(BaseModel):
    """Сводка по товарам завершённой поставки FBP.

    Attributes:
        total_items_count: Количество уникальных товаров
        total_quantity: Общее количество единиц товара
        rounded_total_volume_in_litres: Округлённый суммарный объём, л
    """

    total_items_count: Optional[int] = Field(
        None, description="Количество уникальных товаров."
    )
    total_quantity: Optional[int] = Field(
        None, description="Общее количество единиц товара."
    )
    rounded_total_volume_in_litres: Optional[float] = Field(
        None, description="Округлённый суммарный объём, л."
    )


class FbpArchiveDeclineReason(BaseModel):
    """Причина отклонения завершённой поставки FBP.

    Attributes:
        code: Код причины (`CANNOT_CREATE_SUPPLY_ON_TPF`, `DROP_OFF_POINT_CLOSED`,
            `CODE_SUPPLY_LOST`, `COURIER_PICK_UP_REJECTED_BY_SELLER`,
            `BONDED_DOCUMENTS_REJECTED_BY_WAREHOUSE`)
        message: Текст причины
    """

    code: Optional[str] = Field(
        None,
        description="Код причины отклонения (набор открытый — тип `str`)."
    )
    message: Optional[str] = Field(
        None, description="Текст причины отклонения."
    )
