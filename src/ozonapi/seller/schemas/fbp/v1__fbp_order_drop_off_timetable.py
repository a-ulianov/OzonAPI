"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderDropOffTimetable"""
from pydantic import BaseModel, Field

from .v1__fbp_draft_drop_off_point_timetable import FbpTimetableCalendar


class FbpOrderDropOffTimetableRequest(BaseModel):
    """Схема запроса графика работы drop-off пункта для поставки.

    Attributes:
        warehouse_id: Идентификатор склада
        province_uuid: Идентификатор провинции
        drop_off_point_id: Идентификатор drop-off пункта
    """

    warehouse_id: int = Field(..., description="Идентификатор склада.")
    province_uuid: str = Field(..., description="Идентификатор провинции.")
    drop_off_point_id: int = Field(..., description="Идентификатор drop-off пункта.")


class FbpOrderDropOffTimetableResponse(BaseModel):
    """Схема ответа с графиком работы drop-off пункта.

    Attributes:
        calendar: Расписание по дням недели
    """

    calendar: list[FbpTimetableCalendar] = Field(
        default_factory=list, description="Расписание по дням недели."
    )
