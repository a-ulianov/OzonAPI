"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpEditTimeslot"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpOrderDirectTimeslotEditRequest(BaseModel):
    """Схема запроса редактирования таймслота в заявке на поставку.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        timeslot_start: Начало нового таймслота поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    timeslot_start: str = Field(
        ..., description="Начало нового таймслота поставки в формате RFC3339."
    )


class FbpOrderDirectTimeslotEditResponse(BaseModel):
    """Схема ответа редактирования таймслота в заявке на поставку.

    Attributes:
        error_reasons: Причины ошибки брони таймслота (`REQUEST_VALIDATION`,
            `INVALID_RESERVE`, `LOGISTICS_REASON`, `SCHEDULE_REASON`)
        row_version: Версия записи
    """

    error_reasons: list[str] = Field(
        default_factory=list,
        description="Причины ошибки брони таймслота (набор открытый — тип `str`)."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
