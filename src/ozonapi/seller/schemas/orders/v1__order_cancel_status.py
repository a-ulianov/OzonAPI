"""Схемы метода order_cancel_status (статус отмены заказа, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class OrderCancelStatusRequest(BaseModel):
    """Параметры запроса статуса отмены заказа.

    Attributes:
        order_number: Номер заказа
    """
    order_number: str = Field(..., description="Номер заказа.")


class OrderCancelStatusResponse(BaseModel):
    """Ответ со статусом отмены заказа.

    Attributes:
        order_number: Номер заказа
        posting_number: Номера отправлений заказа
        state: Статус отмены заказа
    """
    order_number: Optional[str] = Field(None, description="Номер заказа.")
    posting_number: Optional[list[str]] = Field(
        None, description="Номера отправлений заказа."
    )
    state: Optional[str] = Field(None, description="Статус отмены заказа.")
