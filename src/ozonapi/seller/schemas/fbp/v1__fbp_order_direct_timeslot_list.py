"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpAvailableTimeslotList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpTimeslot


class FbpOrderDirectTimeslotListRequest(BaseModel):
    """Схема запроса списка таймслотов для поставки.

    Attributes:
        supply_id: Идентификатор поставки
        interval_start: Начало интервала поиска таймслотов
        interval_end: Конец интервала поиска таймслотов
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    interval_start: str = Field(
        ..., description="Начало интервала поиска таймслотов в формате RFC3339."
    )
    interval_end: str = Field(
        ..., description="Конец интервала поиска таймслотов в формате RFC3339."
    )


class FbpOrderDirectTimeslotListResponse(BaseModel):
    """Схема ответа со списком таймслотов для поставки.

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
