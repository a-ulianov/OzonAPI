"""Схемы метода warehouse_fbs_update_drop_off_timeslot_list (таймслоты drop-off для обновления, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSDropOffTimeslot


class WarehouseFBSUpdateDropOffTimeslotListRequest(BaseModel):
    """Параметры запроса таймслотов drop-off для обновления склада.

    Attributes:
        drop_off_point_id: Идентификатор drop-off пункта
        warehouse_id: Идентификатор склада
    """
    drop_off_point_id: int = Field(..., description="Идентификатор drop-off пункта.")
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSUpdateDropOffTimeslotListResponse(BaseModel):
    """Ответ со списком таймслотов drop-off для обновления склада.

    Attributes:
        timeslots: Список таймслотов
    """
    timeslots: Optional[list[WarehouseFBSDropOffTimeslot]] = Field(
        None, description="Список таймслотов."
    )
