"""https://docs.ozon.ru/api/seller/#operation/PolygonTimeCoordinatesUpdate"""
from pydantic import BaseModel, Field


class PolygonTimeCoordinatesUpdateRequest(BaseModel):
    """Схема запроса обновления координат полигона доставки.

    Attributes:
        coordinates: Новые координаты полигона (строка с JSON-массивом)
        delivery_method_id: Идентификатор метода доставки
        polygon_id: Идентификатор полигона
        warehouse_id: Идентификатор склада
    """

    coordinates: str = Field(
        ...,
        description="Новые координаты полигона (строка с JSON-массивом координат)."
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


class PolygonTimeCoordinatesUpdateResponse(BaseModel):
    """Схема ответа обновления координат полигона доставки.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
