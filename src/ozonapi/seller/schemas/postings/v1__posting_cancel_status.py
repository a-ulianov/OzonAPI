"""Схемы метода posting_cancel_status (статус отмены отправления, v1)."""
from pydantic import BaseModel, Field


class PostingCancelStatusRequest(BaseModel):
    """Параметры запроса статуса отмены отправления.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(..., description="Номер отправления.")


class PostingCancelStatusResponse(BaseModel):
    """Ответ со статусом отмены отправления.

    Attributes:
        order_number: Номер заказа
        posting_number: Номера отправлений
        state: Статус отмены отправления
    """
    order_number: str = Field("", description="Номер заказа.")
    posting_number: list[str] = Field(
        default_factory=list, description="Номера отправлений."
    )
    state: str = Field("", description="Статус отмены отправления.")
