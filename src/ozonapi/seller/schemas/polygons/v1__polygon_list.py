"""https://docs.ozon.ru/api/seller/#operation/PolygonList"""
from typing import Optional

from pydantic import BaseModel, Field


class PolygonListRequest(BaseModel):
    """Схема запроса списка полигонов метода доставки.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        warehouse_id: Идентификатор склада
    """

    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class PolygonListPolygon(BaseModel):
    """Полигон доставки с координатами и временем.

    Attributes:
        polygon_id: Идентификатор полигона
        coordinates: Координаты полигона (строка с JSON-массивом)
        time: Время доставки в полигоне, минуты
    """

    polygon_id: Optional[int] = Field(
        None, description="Идентификатор полигона."
    )
    coordinates: Optional[str] = Field(
        None, description="Координаты полигона (строка с JSON-массивом координат)."
    )
    time: Optional[int] = Field(
        None, description="Время доставки в полигоне, минуты."
    )


class PolygonListResponse(BaseModel):
    """Схема ответа со списком полигонов метода доставки.

    Attributes:
        polygons: Список установленных полигонов
    """

    polygons: list[PolygonListPolygon] = Field(
        default_factory=list,
        description="Список установленных на метод доставки полигонов."
    )
