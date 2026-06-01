"""Схемы метода warehouse_fbs_update_drop_off_list (drop-off пункты для изменения склада, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import WarehouseFBSDropOffPoint, WarehouseFBSPointSearch


class WarehouseFBSUpdateDropOffListRequest(BaseModel):
    """Параметры запроса drop-off пунктов для изменения склада.

    Attributes:
        search: Параметры поиска пункта
        warehouse_id: Идентификатор склада
    """
    search: Optional[WarehouseFBSPointSearch] = Field(
        None, description="Параметры поиска пункта."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSUpdateDropOffListResponse(BaseModel):
    """Ответ со списком drop-off пунктов для изменения склада.

    Attributes:
        points: Список drop-off пунктов
    """
    points: Optional[list[WarehouseFBSDropOffPoint]] = Field(
        None, description="Список drop-off пунктов."
    )
