"""Схемы метода conditional_cancellation_reject (отклонение заявки на отмену rFBS, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class ConditionalCancellationRejectRequest(BaseModel):
    """Параметры запроса отклонения заявки на отмену rFBS.

    Attributes:
        cancellation_id: Идентификатор заявки на отмену
        comment: Комментарий
    """
    cancellation_id: int = Field(..., description="Идентификатор заявки на отмену.")
    comment: Optional[str] = Field(None, description="Комментарий.")


class ConditionalCancellationRejectResponse(BaseModel):
    """Ответ на отклонение заявки на отмену rFBS.

    Notes:
        • Тело ответа отсутствует — успешное отклонение возвращает код 200.
    """
