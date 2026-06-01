"""Схемы метода warehouse_erfbs_non_integrated_delivery_method_update (метод «Вы или сторонняя служба», v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseERFBSReturnSettings


class WarehouseERFBSNonIntegratedDeliveryMethodUpdateRequest(BaseModel):
    """Параметры запроса обновления метода доставки «Вы или сторонняя служба».

    Attributes:
        courier_cutoff: Время на передачу заказа курьеру в минутах (допустимо: 5, 10, 15, 20, 25, 30, 35, 40, 45)
        cut_in: Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)
        delivery_method_id: Идентификатор метода доставки
        name: Название метода доставки
        return_settings: Настройки возврата
        warehouse_id: Идентификатор склада
    """
    courier_cutoff: Optional[int] = Field(
        None,
        description="Время на передачу заказа курьеру в минутах (допустимо: 5, 10, 15, 20, 25, 30, 35, 40, 45)."
    )
    cut_in: Optional[int] = Field(
        None,
        description="Время на сборку в минутах (допустимо: 15, 30, 60, 120, 180, 240, 300, 360, 420, 480)."
    )
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    name: Optional[str] = Field(None, description="Название метода доставки.")
    return_settings: Optional[WarehouseERFBSReturnSettings] = Field(
        None, description="Настройки возврата."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")
