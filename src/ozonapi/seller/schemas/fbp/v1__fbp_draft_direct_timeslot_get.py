"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectGetTimeslot"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpTimeslot


class FbpDraftDirectTimeslotGetRequest(BaseModel):
    """Схема запроса списка таймслотов для прямой поставки.

    Attributes:
        bundle_id: Идентификатор набора товаров
        warehouse_id: Идентификатор склада
        interval_start: Начало интервала поиска таймслотов
        interval_end: Конец интервала поиска таймслотов
    """

    bundle_id: str = Field(..., description="Идентификатор набора товаров.")
    warehouse_id: int = Field(..., description="Идентификатор склада.")
    interval_start: str = Field(
        ..., description="Начало интервала поиска таймслотов в формате RFC3339."
    )
    interval_end: str = Field(
        ..., description="Конец интервала поиска таймслотов в формате RFC3339."
    )


class FbpDraftDirectTimeslotGetResponse(BaseModel):
    """Схема ответа со списком таймслотов для прямой поставки.

    Attributes:
        timeslots: Доступные таймслоты
        warehouse_timezone_name: Часовой пояс склада
        reasons: Причины отсутствия таймслотов (`LOGISTICS_UNKNOWN`, `NO_ROUTE`,
            `NO_LOGISTICS_CAPACITY`, `NOT_ENOUGH_CAPACITY` и др.)
    """

    timeslots: list[FbpTimeslot] = Field(
        default_factory=list, description="Доступные таймслоты поставки."
    )
    warehouse_timezone_name: Optional[str] = Field(
        None, description="Часовой пояс склада."
    )
    reasons: list[str] = Field(
        default_factory=list,
        description="Причины отсутствия таймслотов (набор открытый — тип `str`)."
    )
