"""Схемы метода delivery_point_list (список точек самовывоза, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import DeliveryLatLong


class DeliveryPointListRequest(BaseModel):
    """Параметры запроса списка всех точек самовывоза.

    Notes:
        • Запрос без параметров.
    """


class DeliveryPointListItem(BaseModel):
    """Точка самовывоза.

    Attributes:
        coordinate: Координаты точки
        map_point_id: Идентификатор точки на карте
    """
    coordinate: Optional[DeliveryLatLong] = Field(None, description="Координаты точки.")
    map_point_id: Optional[int] = Field(
        None, description="Идентификатор точки на карте."
    )


class DeliveryPointListResponse(BaseModel):
    """Ответ со списком всех точек самовывоза.

    Attributes:
        points: Список точек самовывоза
    """
    points: Optional[list[DeliveryPointListItem]] = Field(
        None, description="Список точек самовывоза."
    )
