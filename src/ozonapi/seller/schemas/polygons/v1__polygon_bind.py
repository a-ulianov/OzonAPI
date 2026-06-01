"""https://docs.ozon.ru/api/seller/#operation/PolygonAPI_BindPolygon"""
from pydantic import BaseModel, Field


class PolygonBindV1Polygon(BaseModel):
    """Полигон и время доставки для привязки (v1).

    Attributes:
        polygon_id: Идентификатор полигона
        time: Время доставки в полигоне, минуты
    """

    polygon_id: int = Field(
        ..., description="Идентификатор полигона."
    )
    time: int = Field(
        ..., description="Время доставки в полигоне, минуты."
    )


class PolygonBindV1WarehouseLocation(BaseModel):
    """Координаты склада (v1).

    Attributes:
        lat: Широта склада
        lon: Долгота склада
    """

    lat: str = Field(
        ..., description="Широта склада."
    )
    lon: str = Field(
        ..., description="Долгота склада."
    )


class PolygonBindV1Request(BaseModel):
    """Схема запроса привязки полигонов к методу доставки (v1).

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        polygons: Список полигонов с временем доставки
        warehouse_location: Координаты склада
    """

    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    polygons: list[PolygonBindV1Polygon] = Field(
        default_factory=list,
        description="Список полигонов с временем доставки."
    )
    warehouse_location: PolygonBindV1WarehouseLocation = Field(
        ..., description="Координаты склада."
    )


class PolygonBindV1Response(BaseModel):
    """Схема ответа привязки полигонов к методу доставки (v1).

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
