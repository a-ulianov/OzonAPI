"""Схемы метода warehouse_rfbs_pause (постановка rFBS-склада на паузу, v1)."""
from pydantic import BaseModel, Field


class WarehouseRfbsPauseRequest(BaseModel):
    """Параметры запроса постановки rFBS-склада на паузу.

    Attributes:
        warehouse_id: Идентификатор склада
    """
    warehouse_id: int = Field(..., description="Идентификатор склада.")
