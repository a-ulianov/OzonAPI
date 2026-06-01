"""Схемы метода warehouse_fbs_create (создание склада FBS, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import FirstMileTypeV2, WarehouseWorkingDayV2
from .entities import WarehouseFBSCoordinates, WarehouseFBSOptions


class WarehouseFBSCreateRequest(BaseModel):
    """Параметры запроса создания склада FBS.

    Attributes:
        address_coordinates: Координаты адреса склада
        cut_in_time: Время на отгрузку в минутах
        drop_off_point_id: Идентификатор drop-off пункта
        first_mile_type: Тип первой мили
        is_kgt: Признак приёма крупногабаритных товаров
        name: Название склада
        options: Дополнительные настройки склада
        phone: Номер телефона склада
        timeslot_id: Идентификатор таймслота
        return_point_id: Идентификатор пункта возврата
        working_days: Рабочие дни склада
    """
    address_coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты адреса склада."
    )
    cut_in_time: Optional[int] = Field(
        None, description="Время на отгрузку в минутах."
    )
    drop_off_point_id: Optional[int] = Field(
        None, description="Идентификатор drop-off пункта."
    )
    first_mile_type: Optional[FirstMileTypeV2] = Field(
        None, description="Тип первой мили."
    )
    is_kgt: Optional[bool] = Field(
        None, description="Признак приёма крупногабаритных товаров."
    )
    name: Optional[str] = Field(None, description="Название склада.")
    options: Optional[WarehouseFBSOptions] = Field(
        None, description="Дополнительные настройки склада."
    )
    phone: Optional[str] = Field(None, description="Номер телефона склада.")
    timeslot_id: Optional[int] = Field(None, description="Идентификатор таймслота.")
    return_point_id: Optional[int] = Field(
        None, description="Идентификатор пункта возврата."
    )
    working_days: Optional[list[WarehouseWorkingDayV2]] = Field(
        None, description="Рабочие дни склада."
    )


class WarehouseFBSCreateResponse(BaseModel):
    """Ответ на создание склада FBS.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(None, description="Идентификатор операции.")
