"""Схемы метода warehouse_fbs_create_return_point_list (пункты возврата для создания, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import (
    WarehouseFBSCoordinates,
    WarehouseFBSPointSearch,
    WarehouseFBSReturnPoint,
)


class WarehouseFBSCreateReturnPointListRequest(BaseModel):
    """Параметры запроса пунктов возврата для создания склада.

    Attributes:
        coordinates: Координаты для поиска ближайших пунктов
        country_code: Код страны
        last_id: Идентификатор последнего значения для пагинации
        limit: Количество значений в ответе
        search: Параметры поиска пункта
        selected_dropoff_point_id: Идентификатор выбранного drop-off пункта
    """
    coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты для поиска ближайших пунктов."
    )
    country_code: Optional[str] = Field(None, description="Код страны.")
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    search: Optional[WarehouseFBSPointSearch] = Field(
        None, description="Параметры поиска пункта."
    )
    selected_dropoff_point_id: Optional[int] = Field(
        None, description="Идентификатор выбранного drop-off пункта."
    )


class WarehouseFBSCreateReturnPointListResponse(BaseModel):
    """Ответ со списком пунктов возврата для создания склада.

    Attributes:
        has_next: Признак наличия следующей страницы
        is_selected_point_available: Признак доступности выбранного пункта
        last_id: Идентификатор последнего значения для пагинации
        points: Список пунктов возврата
    """
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    is_selected_point_available: Optional[bool] = Field(
        None, description="Признак доступности выбранного пункта."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    points: Optional[list[WarehouseFBSReturnPoint]] = Field(
        None, description="Список пунктов возврата."
    )
