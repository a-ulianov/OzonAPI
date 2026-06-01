"""Схемы метода warehouse_rfbs_unpause (снятие rFBS-склада с паузы, v1)."""
from pydantic import BaseModel, Field


class WarehouseRfbsUnpauseRequest(BaseModel):
    """Параметры запроса снятия rFBS-склада с паузы.

    Attributes:
        warehouse_id: Идентификатор склада
    """
    warehouse_id: int = Field(..., description="Идентификатор склада.")
