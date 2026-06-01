"""Схемы метода warehouse_fbs_pickup_courier_cancel (отмена вызова курьера pick-up, v1)."""
from pydantic import BaseModel, Field


class WarehouseFBSPickUpCourierCancelRequest(BaseModel):
    """Параметры запроса отмены вызова курьера на забор отгрузки pick-up.

    Attributes:
        warehouse_id: Идентификатор склада
    """
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSPickUpCourierCancelResponse(BaseModel):
    """Ответ на отмену вызова курьера на забор отгрузки pick-up.

    Notes:
        • Тело ответа отсутствует — успешная отмена подтверждается кодом 200.
    """
