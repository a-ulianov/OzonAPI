"""Схемы метода warehouse_fbs_update (обновление склада FBS, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import WarehouseWorkingDayV2
from .entities import WarehouseFBSCoordinates, WarehouseFBSOptions


class WarehouseFBSUpdateRequest(BaseModel):
    """Параметры запроса обновления склада FBS.

    Attributes:
        address_coordinates: Координаты адреса склада
        name: Название склада
        options: Дополнительные настройки склада
        phone: Номер телефона склада
        warehouse_id: Идентификатор склада
        working_days: Рабочие дни склада
    """
    address_coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты адреса склада."
    )
    name: Optional[str] = Field(None, description="Название склада.")
    options: Optional[WarehouseFBSOptions] = Field(
        None, description="Дополнительные настройки склада."
    )
    phone: Optional[str] = Field(None, description="Номер телефона склада.")
    warehouse_id: int = Field(..., description="Идентификатор склада.")
    working_days: Optional[list[WarehouseWorkingDayV2]] = Field(
        None, description="Рабочие дни склада."
    )


class WarehouseFBSUpdateResponse(BaseModel):
    """Ответ на обновление склада FBS.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(None, description="Идентификатор операции.")
