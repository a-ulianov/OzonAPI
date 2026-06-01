"""Схемы метода posting_cancel (отмена отправления из заказа, v1)."""
from pydantic import BaseModel, Field


class PostingCancelRequest(BaseModel):
    """Параметры запроса отмены отправления.

    Attributes:
        posting_number: Номер отправления
        reason_id: Идентификатор причины отмены отправления
        reason_message: Дополнительная информация по отмене
    """
    posting_number: str = Field(..., description="Номер отправления.")
    reason_id: int = Field(..., description="Идентификатор причины отмены отправления.")
    reason_message: str = Field(..., description="Дополнительная информация по отмене.")


class PostingCancelResponse(BaseModel):
    """Ответ на отмену отправления.

    Attributes:
        message: Результат обработки запроса
    """
    message: str = Field("", description="Результат обработки запроса.")
