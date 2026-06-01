"""Схемы метода warehouse_erfbs_non_integrated_create (склад «Вы или сторонняя служба», v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    WarehouseERFBSDeliveryPolygon,
    WarehouseERFBSReturnSettings,
    WarehouseERFBSTimetable,
    WarehouseFBSCoordinates,
)


class WarehouseERFBSNonIntegratedCreateDeliveryMethod(BaseModel):
    """Метод доставки «Вы или сторонняя служба» при создании склада.

    Attributes:
        courier_cutoff: Время на передачу заказа курьеру в минутах
        cut_in: Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)
        delivery_polygons: Полигоны доставки
        name: Название метода доставки
        return_settings: Настройки возврата
    """
    courier_cutoff: Optional[int] = Field(
        None, description="Время на передачу заказа курьеру в минутах."
    )
    cut_in: Optional[int] = Field(
        None,
        description="Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)."
    )
    delivery_polygons: Optional[list[WarehouseERFBSDeliveryPolygon]] = Field(
        None, description="Полигоны доставки."
    )
    name: Optional[str] = Field(None, description="Название метода доставки.")
    return_settings: Optional[WarehouseERFBSReturnSettings] = Field(
        None, description="Настройки возврата."
    )


class WarehouseERFBSNonIntegratedCreateRequest(BaseModel):
    """Параметры запроса создания склада с доставкой «Вы или сторонняя служба».

    Attributes:
        address_coordinates: Координаты адреса склада
        is_auto_assembly: Признак автосборки
        delivery_method: Метод доставки «Вы или сторонняя служба»
        min_order_value: Минимальная стоимость заказа
        name: Название склада
        phone: Номер телефона склада
        timetable_warehouse: Расписание работы склада
    """
    address_coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты адреса склада."
    )
    is_auto_assembly: Optional[bool] = Field(None, description="Признак автосборки.")
    delivery_method: Optional[WarehouseERFBSNonIntegratedCreateDeliveryMethod] = Field(
        None, description="Метод доставки «Вы или сторонняя служба»."
    )
    min_order_value: Optional[int] = Field(
        None, description="Минимальная стоимость заказа."
    )
    name: Optional[str] = Field(None, description="Название склада.")
    phone: Optional[str] = Field(None, description="Номер телефона склада.")
    timetable_warehouse: Optional[WarehouseERFBSTimetable] = Field(
        None, description="Расписание работы склада."
    )
