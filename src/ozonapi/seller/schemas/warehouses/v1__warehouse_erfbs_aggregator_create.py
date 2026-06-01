"""Схемы метода warehouse_erfbs_aggregator_create (склад с доставкой «Партнёры Ozon», v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    WarehouseERFBSDeliveryCosts,
    WarehouseERFBSReturnSettings,
    WarehouseERFBSTimetable,
    WarehouseFBSCoordinates,
)


class WarehouseERFBSAggregatorCreateDeliveryMethod(BaseModel):
    """Метод доставки «Партнёры Ozon» при создании склада.

    Attributes:
        courier_comment: Комментарий для курьера
        courier_phones: Телефоны для связи с курьером
        cut_in: Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)
        deliver_to_pvz: Доставлять в пункт выдачи
        delivery_costs: Стоимость доставки
        name: Название метода доставки
        return_settings: Настройки возврата
    """
    courier_comment: Optional[str] = Field(None, description="Комментарий для курьера.")
    courier_phones: Optional[list[str]] = Field(
        None, description="Телефоны для связи с курьером."
    )
    cut_in: Optional[int] = Field(
        None,
        description="Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)."
    )
    deliver_to_pvz: Optional[bool] = Field(
        None, description="Доставлять в пункт выдачи."
    )
    delivery_costs: Optional[WarehouseERFBSDeliveryCosts] = Field(
        None, description="Стоимость доставки."
    )
    name: Optional[str] = Field(None, description="Название метода доставки.")
    return_settings: Optional[WarehouseERFBSReturnSettings] = Field(
        None, description="Настройки возврата."
    )


class WarehouseERFBSAggregatorCreateRequest(BaseModel):
    """Параметры запроса создания склада с доставкой «Партнёры Ozon».

    Attributes:
        address_coordinates: Координаты адреса склада
        is_auto_assembly: Признак автосборки
        delivery_method: Метод доставки «Партнёры Ozon»
        min_order_value: Минимальная стоимость заказа
        name: Название склада
        phone: Номер телефона склада
        timetable_warehouse: Расписание работы склада
    """
    address_coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты адреса склада."
    )
    is_auto_assembly: Optional[bool] = Field(None, description="Признак автосборки.")
    delivery_method: Optional[WarehouseERFBSAggregatorCreateDeliveryMethod] = Field(
        None, description="Метод доставки «Партнёры Ozon»."
    )
    min_order_value: Optional[int] = Field(
        None, description="Минимальная стоимость заказа."
    )
    name: Optional[str] = Field(None, description="Название склада.")
    phone: Optional[str] = Field(None, description="Номер телефона склада.")
    timetable_warehouse: Optional[WarehouseERFBSTimetable] = Field(
        None, description="Расписание работы склада."
    )
