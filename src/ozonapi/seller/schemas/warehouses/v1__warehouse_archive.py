"""Схемы метода warehouse_archive (перенос склада в архив, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseArchiveRequest(BaseModel):
    """Параметры запроса переноса склада в архив.

    Attributes:
        reason: Причина переноса в архив
        return_point_id: Идентификатор пункта возврата
        warehouse_id: Идентификатор склада
    """
    reason: Optional[str] = Field(None, description="Причина переноса в архив.")
    return_point_id: Optional[int] = Field(
        None, description="Идентификатор пункта возврата."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseArchiveResponse(BaseModel):
    """Ответ на перенос склада в архив.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
