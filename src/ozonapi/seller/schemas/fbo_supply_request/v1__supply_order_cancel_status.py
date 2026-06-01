"""Схемы метода supply_order_cancel_status (статус отмены заявки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderCancelStatusRequest(BaseModel):
    """Параметры запроса статуса отмены заявки на поставку.

    Attributes:
        operation_id: Идентификатор операции отмены
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции отмены."
    )


class SupplyOrderCancelStatusSupply(BaseModel):
    """Результат отмены отдельной поставки.

    Attributes:
        error_reasons: Причины ошибки отмены поставки
        is_supply_cancelled: Поставка отменена
        supply_id: Идентификатор поставки
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки отмены поставки."
    )
    is_supply_cancelled: Optional[bool] = Field(
        None, description="Поставка отменена."
    )
    supply_id: Optional[int] = Field(None, description="Идентификатор поставки.")


class SupplyOrderCancelStatusResult(BaseModel):
    """Результат отмены заявки на поставку.

    Attributes:
        is_order_cancelled: Заявка отменена
        supplies: Результаты отмены поставок
    """
    is_order_cancelled: Optional[bool] = Field(
        None, description="Заявка отменена."
    )
    supplies: Optional[list[SupplyOrderCancelStatusSupply]] = Field(
        None, description="Результаты отмены поставок."
    )


class SupplyOrderCancelStatusResponse(BaseModel):
    """Ответ со статусом отмены заявки на поставку.

    Attributes:
        error_reasons: Причины ошибки отмены заявки
        result: Результат отмены заявки
        status: Статус операции отмены
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки отмены заявки."
    )
    result: Optional[SupplyOrderCancelStatusResult] = Field(
        None, description="Результат отмены заявки."
    )
    status: Optional[str] = Field(None, description="Статус операции отмены.")
