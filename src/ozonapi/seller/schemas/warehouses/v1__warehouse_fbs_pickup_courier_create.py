"""Схемы метода warehouse_fbs_pickup_courier_create (вызов курьера на забор pick-up, v1)."""
from pydantic import BaseModel, Field


class WarehouseFBSPickUpCourierCreateRequest(BaseModel):
    """Параметры запроса вызова курьера на забор отгрузки pick-up.

    Attributes:
        warehouse_id: Идентификатор склада
    """
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class WarehouseFBSPickUpCourierCreateResponse(BaseModel):
    """Ответ на вызов курьера на забор отгрузки pick-up.

    Notes:
        • Тело ответа отсутствует — успешный вызов подтверждается кодом 200.
    """
