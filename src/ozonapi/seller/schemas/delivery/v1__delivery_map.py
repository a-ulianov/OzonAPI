"""Схемы метода delivery_map (точки самовывоза на карте, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import DeliveryLatLong, DeliveryViewport


class DeliveryMapRequest(BaseModel):
    """Параметры запроса точек самовывоза на карте.

    Attributes:
        viewport: Видимая область карты
        zoom: Масштаб карты
    """
    viewport: Optional[DeliveryViewport] = Field(
        None, description="Видимая область карты."
    )
    zoom: Optional[int] = Field(None, description="Масштаб карты.")


class DeliveryMapCluster(BaseModel):
    """Кластер точек самовывоза на карте.

    Attributes:
        coordinate: Координаты центра кластера
        is_same_building: Признак, что точки находятся в одном здании
        map_point_ids: Идентификаторы точек кластера
        points_count: Количество точек в кластере
        viewport: Область кластера на карте
    """
    coordinate: Optional[DeliveryLatLong] = Field(
        None, description="Координаты центра кластера."
    )
    is_same_building: Optional[bool] = Field(
        None, description="Признак, что точки находятся в одном здании."
    )
    map_point_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы точек кластера."
    )
    points_count: Optional[int] = Field(
        None, description="Количество точек в кластере."
    )
    viewport: Optional[DeliveryViewport] = Field(
        None, description="Область кластера на карте."
    )


class DeliveryMapResponse(BaseModel):
    """Ответ со списком кластеров точек самовывоза на карте.

    Attributes:
        clusters: Кластеры точек самовывоза
    """
    clusters: Optional[list[DeliveryMapCluster]] = Field(
        None, description="Кластеры точек самовывоза."
    )
