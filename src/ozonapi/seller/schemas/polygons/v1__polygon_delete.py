"""https://docs.ozon.ru/api/seller/#operation/PolygonDelete"""
from pydantic import BaseModel, Field


class PolygonDeleteRequest(BaseModel):
    """Схема запроса удаления полигона из области доставки.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        polygon_id: Идентификатор полигона
        warehouse_id: Идентификатор склада
    """

    delivery_method_id: int = Field(
        ..., description="Идентификатор метода доставки."
    )
    polygon_id: int = Field(
        ..., description="Идентификатор полигона."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )


class PolygonDeleteResponse(BaseModel):
    """Схема ответа удаления полигона из области доставки.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
