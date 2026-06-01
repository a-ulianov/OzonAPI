"""https://docs.ozon.ru/api/seller/#operation/PolygonBind"""
from pydantic import BaseModel, Field

from ...common.enumerations.polygons import PolygonDeliveryTime


class PolygonBindRequest(BaseModel):
    """Схема запроса привязки полигона к методу доставки.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        polygon_id: Идентификатор полигона
        time: Время доставки в полигоне, минуты (15, 30, 45, 60, 90, 120, 150)
        warehouse_id: Идентификатор склада
    """

    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    polygon_id: int = Field(
        ..., description="Идентификатор полигона."
    )
    time: PolygonDeliveryTime = Field(
        ...,
        description="Время доставки в полигоне, минуты "
                    "(допустимые значения: 15, 30, 45, 60, 90, 120, 150)."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class PolygonBindResponse(BaseModel):
    """Схема ответа привязки полигона к методу доставки.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
