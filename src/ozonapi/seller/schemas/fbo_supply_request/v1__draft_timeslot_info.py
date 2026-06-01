"""Схемы метода draft_timeslot_info_v1 (доступные таймслоты, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class DraftTimeslotInfoV1Request(BaseModel):
    """Параметры запроса доступных таймслотов (версия 1).

    Attributes:
        date_from: Дата начала периода
        date_to: Дата окончания периода
        draft_id: Идентификатор черновика
        warehouse_ids: Идентификаторы складов
    """
    date_from: str = Field(..., description="Дата начала периода.")
    date_to: str = Field(..., description="Дата окончания периода.")
    draft_id: int = Field(..., description="Идентификатор черновика.")
    warehouse_ids: list[str] = Field(
        ..., description="Идентификаторы складов."
    )


class DraftTimeslotV1Slot(BaseModel):
    """Таймслот.

    Attributes:
        from_in_timezone: Начало таймслота
        to_in_timezone: Конец таймслота
    """
    from_in_timezone: Optional[str] = Field(
        None, description="Начало таймслота."
    )
    to_in_timezone: Optional[str] = Field(
        None, description="Конец таймслота."
    )


class DraftTimeslotV1Day(BaseModel):
    """Таймслоты по дате.

    Attributes:
        date_in_timezone: Дата таймслотов
        timeslots: Таймслоты
    """
    date_in_timezone: Optional[str] = Field(
        None, description="Дата таймслотов."
    )
    timeslots: Optional[list[DraftTimeslotV1Slot]] = Field(
        None, description="Таймслоты."
    )


class DraftTimeslotV1Warehouse(BaseModel):
    """Таймслоты склада.

    Attributes:
        current_time_in_timezone: Текущее время в часовом поясе склада
        days: Таймслоты по датам
        drop_off_warehouse_id: Идентификатор склада
        warehouse_timezone: Часовой пояс склада
    """
    current_time_in_timezone: Optional[str] = Field(
        None, description="Текущее время в часовом поясе склада."
    )
    days: Optional[list[DraftTimeslotV1Day]] = Field(
        None, description="Таймслоты по датам."
    )
    drop_off_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )
    warehouse_timezone: Optional[str] = Field(
        None, description="Часовой пояс склада."
    )


class DraftTimeslotInfoV1Response(BaseModel):
    """Ответ с доступными таймслотами (версия 1).

    Attributes:
        drop_off_warehouse_timeslots: Таймслоты складов
        requested_date_from: Дата начала запрошенного периода
        requested_date_to: Дата окончания запрошенного периода
    """
    drop_off_warehouse_timeslots: Optional[list[DraftTimeslotV1Warehouse]] = Field(
        None, description="Таймслоты складов."
    )
    requested_date_from: Optional[str] = Field(
        None, description="Дата начала запрошенного периода."
    )
    requested_date_to: Optional[str] = Field(
        None, description="Дата окончания запрошенного периода."
    )
