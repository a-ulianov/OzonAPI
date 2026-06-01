"""https://docs.ozon.ru/api/seller/#operation/PolygonAPI_CreatePolygon"""
from pydantic import BaseModel, Field


class PolygonCreateRequest(BaseModel):
    """Схема запроса создания полигона доставки.

    Attributes:
        coordinates: Координаты полигона в формате `[[[lat, lon], ...]]` (строка JSON)
    """

    coordinates: str = Field(
        ...,
        description="Координаты полигона в формате `[[[lat, lon], [lat, lon], ...]]` "
                    "(строка с JSON-массивом координат)."
    )


class PolygonCreateResponse(BaseModel):
    """Схема ответа создания полигона доставки.

    Attributes:
        polygon_id: Идентификатор созданного полигона
    """

    polygon_id: int = Field(
        ..., description="Идентификатор созданного полигона."
    )
