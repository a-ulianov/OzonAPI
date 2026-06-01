"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectTimeslotEdit"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpDraftDirectTimeslotEditRequest(BaseModel):
    """Схема запроса редактирования таймслота в черновике.

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


class FbpDraftDirectTimeslotEditResponse(BaseModel):
    """Схема ответа редактирования таймслота в черновике.

    Attributes:
        error_reasons: Причины ошибки брони таймслота (`REQUEST_VALIDATION`,
            `INVALID_RESERVE`, `LOGISTICS_REASON`, `SCHEDULE_REASON`, `NO_CAPACITY`)
        row_version: Версия записи
    """

    error_reasons: list[str] = Field(
        default_factory=list,
        description="Причины ошибки брони таймслота (набор открытый — тип `str`)."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
