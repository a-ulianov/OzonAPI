"""Схемы метода order_cancel (отмена заказа, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class OrderCancelRequest(BaseModel):
    """Параметры запроса отмены заказа.

    Attributes:
        order_number: Номер заказа
        reason_id: Идентификатор причины отмены
        reason_message: Комментарий к причине отмены
    """
    order_number: str = Field(..., description="Номер заказа.")
    reason_id: int = Field(..., description="Идентификатор причины отмены.")
    reason_message: Optional[str] = Field(
        None, description="Комментарий к причине отмены."
    )


class OrderCancelResponse(BaseModel):
    """Ответ на отмену заказа.

    Attributes:
        message: Сообщение о результате отмены
    """
    message: Optional[str] = Field(
        None, description="Сообщение о результате отмены."
    )
