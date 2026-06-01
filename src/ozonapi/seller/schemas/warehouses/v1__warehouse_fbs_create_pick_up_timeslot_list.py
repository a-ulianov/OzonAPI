"""Схемы метода warehouse_fbs_create_pick_up_timeslot_list (таймслоты pick-up для создания, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSCoordinates, WarehouseFBSPickUpTimeslot


class WarehouseFBSCreatePickUpTimeslotListRequest(BaseModel):
    """Параметры запроса таймслотов pick-up для создания склада.

    Attributes:
        address_coordinates: Координаты адреса склада
        is_kgt: Признак приёма крупногабаритных товаров
    """
    address_coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты адреса склада."
    )
    is_kgt: bool = Field(
        ..., description="Признак приёма крупногабаритных товаров."
    )


class WarehouseFBSCreatePickUpTimeslotListResponse(BaseModel):
    """Ответ со списком таймслотов pick-up для создания склада.

    Attributes:
        is_pickup_supported: Признак доступности отгрузки pick-up
        timeslots: Список таймслотов
    """
    is_pickup_supported: Optional[bool] = Field(
        None, description="Признак доступности отгрузки pick-up."
    )
    timeslots: Optional[list[WarehouseFBSPickUpTimeslot]] = Field(
        None, description="Список таймслотов."
    )
