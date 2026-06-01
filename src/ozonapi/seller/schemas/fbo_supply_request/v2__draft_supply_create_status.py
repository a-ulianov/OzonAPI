"""Схемы метода draft_supply_create_status (статус создания заявки, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class DraftSupplyCreateStatusRequest(BaseModel):
    """Параметры запроса статуса создания заявки на поставку.

    Attributes:
        draft_id: Идентификатор черновика
    """
    draft_id: int = Field(..., description="Идентификатор черновика.")


class DraftSupplyCreateStatusResponse(BaseModel):
    """Ответ со статусом создания заявки на поставку.

    Attributes:
        error_reasons: Причины ошибки
        order_id: Идентификатор заявки на поставку
        status: Статус создания заявки
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
    order_id: Optional[int] = Field(
        None, description="Идентификатор заявки на поставку."
    )
    status: Optional[str] = Field(
        None, description="Статус создания заявки."
    )
