"""Схемы метода conditional_cancellation_approve (подтверждение заявки на отмену rFBS, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class ConditionalCancellationApproveRequest(BaseModel):
    """Параметры запроса подтверждения заявки на отмену rFBS.

    Attributes:
        cancellation_id: Идентификатор заявки на отмену
        comment: Комментарий
    """
    cancellation_id: int = Field(..., description="Идентификатор заявки на отмену.")
    comment: Optional[str] = Field(None, description="Комментарий.")


class ConditionalCancellationApproveResponse(BaseModel):
    """Ответ на подтверждение заявки на отмену rFBS.

    Notes:
        • Тело ответа отсутствует — успешное подтверждение возвращает код 200.
    """
