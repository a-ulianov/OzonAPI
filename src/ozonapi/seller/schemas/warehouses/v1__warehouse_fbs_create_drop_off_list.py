"""Схемы метода warehouse_fbs_create_drop_off_list (drop-off пункты для создания склада, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    WarehouseFBSCoordinates,
    WarehouseFBSDropOffPoint,
    WarehouseFBSPointSearch,
)


class WarehouseFBSCreateDropOffListRequest(BaseModel):
    """Параметры запроса drop-off пунктов для создания склада.

    Attributes:
        coordinates: Координаты для поиска ближайших пунктов
        country_code: Код страны
        is_kgt: Признак приёма крупногабаритных товаров
        search: Параметры поиска пункта
    """
    coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты для поиска ближайших пунктов."
    )
    country_code: Optional[str] = Field(None, description="Код страны.")
    is_kgt: bool = Field(
        ..., description="Признак приёма крупногабаритных товаров."
    )
    search: Optional[WarehouseFBSPointSearch] = Field(
        None, description="Параметры поиска пункта."
    )


class WarehouseFBSCreateDropOffListResponse(BaseModel):
    """Ответ со списком drop-off пунктов для создания склада.

    Attributes:
        points: Список drop-off пунктов
    """
    points: Optional[list[WarehouseFBSDropOffPoint]] = Field(
        None, description="Список drop-off пунктов."
    )
