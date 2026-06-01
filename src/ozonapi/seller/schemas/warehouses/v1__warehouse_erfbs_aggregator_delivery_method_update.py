"""Схемы метода warehouse_erfbs_aggregator_delivery_method_update (метод доставки «Партнёры Ozon», v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseERFBSDeliveryCosts, WarehouseERFBSReturnSettings


class WarehouseERFBSAggregatorDeliveryMethodUpdateRequest(BaseModel):
    """Параметры запроса обновления метода доставки «Партнёры Ozon».

    Attributes:
        courier_comment: Комментарий для курьера
        courier_phones: Телефоны для связи с курьером
        cut_in: Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)
        deliver_to_pvz: Доставлять в пункт выдачи
        delivery_costs: Стоимость доставки
        delivery_method_id: Идентификатор метода доставки
        name: Название метода доставки
        return_settings: Настройки возврата
        warehouse_id: Идентификатор склада
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
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    name: Optional[str] = Field(None, description="Название метода доставки.")
    return_settings: Optional[WarehouseERFBSReturnSettings] = Field(
        None, description="Настройки возврата."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")
