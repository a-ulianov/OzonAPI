"""Схемы метода warehouse_erfbs_update (обновление склада rFBS Express, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseERFBSTimetable


class WarehouseERFBSUpdateRequest(BaseModel):
    """Параметры запроса обновления склада rFBS Express.

    Attributes:
        is_auto_assembly: Признак автосборки
        min_order_value: Минимальная стоимость заказа
        name: Название склада
        phone: Номер телефона склада
        timetable_warehouse: Расписание работы склада
        warehouse_id: Идентификатор склада
    """
    is_auto_assembly: Optional[bool] = Field(None, description="Признак автосборки.")
    min_order_value: Optional[int] = Field(
        None, description="Минимальная стоимость заказа."
    )
    name: Optional[str] = Field(None, description="Название склада.")
    phone: Optional[str] = Field(None, description="Номер телефона склада.")
    timetable_warehouse: Optional[WarehouseERFBSTimetable] = Field(
        None, description="Расписание работы склада."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")
