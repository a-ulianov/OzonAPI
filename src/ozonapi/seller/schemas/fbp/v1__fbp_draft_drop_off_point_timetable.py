"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffPointTimetable"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpDraftDropOffPointTimetableRequest(BaseModel):
    """Схема запроса расписания работы drop-off пункта.

    Attributes:
        warehouse_id: Идентификатор склада
        province_uuid: Идентификатор провинции
        drop_off_point_id: Идентификатор drop-off пункта
    """

    warehouse_id: int = Field(..., description="Идентификатор склада.")
    province_uuid: str = Field(..., description="Идентификатор провинции.")
    drop_off_point_id: int = Field(..., description="Идентификатор drop-off пункта.")


class FbpTimetableInterval(BaseModel):
    """Временной интервал расписания drop-off пункта.

    Attributes:
        timeslot_start: Начало интервала (время суток)
        timeslot_end: Конец интервала (время суток)
    """

    timeslot_start: Optional[str] = Field(None, description="Начало интервала (время суток).")
    timeslot_end: Optional[str] = Field(None, description="Конец интервала (время суток).")


class FbpTimetableCalendarItem(BaseModel):
    """Расписание дня работы drop-off пункта.

    Attributes:
        opening_hours: Часы работы
        break_hours: Часы перерыва
        is_holiday: Признак выходного дня
    """

    opening_hours: Optional[FbpTimetableInterval] = Field(
        None, description="Часы работы."
    )
    break_hours: Optional[FbpTimetableInterval] = Field(
        None, description="Часы перерыва."
    )
    is_holiday: Optional[bool] = Field(None, description="Признак выходного дня.")


class FbpTimetableCalendar(BaseModel):
    """Расписание дня недели работы drop-off пункта.

    Attributes:
        day_of_week: День недели (`MONDAY`, `TUESDAY`, …, `SUNDAY`)
        calendar_item: Расписание дня
    """

    day_of_week: Optional[str] = Field(
        None,
        description="День недели (`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, "
                    "`FRIDAY`, `SATURDAY`, `SUNDAY`; набор открытый — тип `str`)."
    )
    calendar_item: Optional[FbpTimetableCalendarItem] = Field(
        None, description="Расписание дня."
    )


class FbpDraftDropOffPointTimetableResponse(BaseModel):
    """Схема ответа с расписанием работы drop-off пункта.

    Attributes:
        calendar: Расписание по дням недели
    """

    calendar: list[FbpTimetableCalendar] = Field(
        default_factory=list, description="Расписание по дням недели."
    )
