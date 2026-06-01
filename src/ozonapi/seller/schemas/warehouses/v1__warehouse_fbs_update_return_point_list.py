"""Схемы метода warehouse_fbs_update_return_point_list (пункты возврата для обновления, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSPointSearch, WarehouseFBSReturnPoint


class WarehouseFBSUpdateReturnPointListRequest(BaseModel):
    """Параметры запроса пунктов возврата для обновления склада.

    Attributes:
        current_dropoff_point_id: Идентификатор текущего drop-off пункта
        current_return_point_id: Идентификатор текущего пункта возврата
        last_id: Идентификатор последнего значения для пагинации
        limit: Количество значений в ответе
        search: Параметры поиска пункта
        warehouse_id: Идентификатор склада
    """
    current_dropoff_point_id: Optional[int] = Field(
        None, description="Идентификатор текущего drop-off пункта."
    )
    current_return_point_id: Optional[int] = Field(
        None, description="Идентификатор текущего пункта возврата."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    search: Optional[WarehouseFBSPointSearch] = Field(
        None, description="Параметры поиска пункта."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSUpdateReturnPointListResponse(BaseModel):
    """Ответ со списком пунктов возврата для обновления склада.

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
