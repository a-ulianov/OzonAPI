"""Схемы метода warehouse_unarchive (перенос склада из архива, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseUnarchiveRequest(BaseModel):
    """Параметры запроса переноса склада из архива.

    Attributes:
        return_point_id: Идентификатор пункта возврата
        warehouse_id: Идентификатор склада
    """
    return_point_id: Optional[int] = Field(
        None, description="Идентификатор пункта возврата."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseUnarchiveResponse(BaseModel):
    """Ответ на перенос склада из архива.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
