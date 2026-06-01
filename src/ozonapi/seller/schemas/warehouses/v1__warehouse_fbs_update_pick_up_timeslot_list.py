"""Схемы метода warehouse_fbs_update_pick_up_timeslot_list (таймслоты pick-up для обновления, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSPickUpTimeslot


class WarehouseFBSUpdatePickUpTimeslotListRequest(BaseModel):
    """Параметры запроса таймслотов pick-up для обновления склада.

    Attributes:
        warehouse_id: Идентификатор склада
    """
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSUpdatePickUpTimeslotListResponse(BaseModel):
    """Ответ со списком таймслотов pick-up для обновления склада.

    Attributes:
        timeslots: Список таймслотов
    """
    timeslots: Optional[list[WarehouseFBSPickUpTimeslot]] = Field(
        None, description="Список таймслотов."
    )
