"""Схемы метода supply_order_cancel (отмена заявки на поставку, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderCancelRequest(BaseModel):
    """Параметры запроса отмены заявки на поставку.

    Attributes:
        order_id: Идентификатор заявки на поставку
    """
    order_id: int = Field(..., description="Идентификатор заявки на поставку.")


class SupplyOrderCancelResponse(BaseModel):
    """Ответ на отмену заявки на поставку.

    Attributes:
        operation_id: Идентификатор операции отмены
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции отмены."
    )
