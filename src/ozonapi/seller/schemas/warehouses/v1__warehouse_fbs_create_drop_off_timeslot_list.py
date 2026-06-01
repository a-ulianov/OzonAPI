"""Схемы метода warehouse_fbs_create_drop_off_timeslot_list (таймслоты drop-off для создания, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSDropOffTimeslot


class WarehouseFBSCreateDropOffTimeslotListRequest(BaseModel):
    """Параметры запроса таймслотов drop-off для создания склада.

    Attributes:
        drop_off_point_id: Идентификатор drop-off пункта
    """
    drop_off_point_id: int = Field(..., description="Идентификатор drop-off пункта.")


class WarehouseFBSCreateDropOffTimeslotListResponse(BaseModel):
    """Ответ со списком таймслотов drop-off для создания склада.

    Attributes:
        timeslots: Список таймслотов
    """
    timeslots: Optional[list[WarehouseFBSDropOffTimeslot]] = Field(
        None, description="Список таймслотов."
    )
