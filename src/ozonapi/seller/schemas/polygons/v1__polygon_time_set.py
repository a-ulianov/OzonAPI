"""https://docs.ozon.ru/api/seller/#operation/PolygonTimeSet"""
from pydantic import BaseModel, Field

from ...common.enumerations.polygons import PolygonDeliveryTime


class PolygonTimeSetRequest(BaseModel):
    """Схема запроса установки нового времени доставки в полигоне.

    Attributes:
        current_time: Текущее время доставки, минуты (15, 30, 45, 60, 90, 120, 150)
        new_time: Новое время доставки, минуты (15, 30, 45, 60, 90, 120, 150)
        delivery_method_id: Идентификатор метода доставки
        polygon_id: Идентификатор полигона
        warehouse_id: Идентификатор склада
    """

    current_time: PolygonDeliveryTime = Field(
        ...,
        description="Текущее время доставки, минуты "
                    "(допустимые значения: 15, 30, 45, 60, 90, 120, 150)."
    )
    new_time: PolygonDeliveryTime = Field(
        ...,
        description="Новое время доставки, минуты "
                    "(допустимые значения: 15, 30, 45, 60, 90, 120, 150)."
    )
    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    polygon_id: int = Field(
        ..., description="Идентификатор полигона."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class PolygonTimeSetResponse(BaseModel):
    """Схема ответа установки нового времени доставки в полигоне.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
