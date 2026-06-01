"""Схемы метода draft_supply_create_status_v1 (статус создания заявки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class DraftSupplyCreateStatusV1Request(BaseModel):
    """Параметры запроса статуса создания заявки на поставку (версия 1).

    Attributes:
        operation_id: Идентификатор операции создания заявки
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции создания заявки."
    )


class DraftSupplyCreateStatusV1Result(BaseModel):
    """Результат создания заявок на поставку.

    Attributes:
        order_ids: Идентификаторы заявок на поставку
    """
    order_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы заявок на поставку."
    )


class DraftSupplyCreateStatusV1Response(BaseModel):
    """Ответ со статусом создания заявки на поставку (версия 1).

    Attributes:
        error_messages: Ошибки создания заявок
        result: Результат создания заявок
        status: Статус создания заявки
    """
    error_messages: Optional[list[str]] = Field(
        None, description="Ошибки создания заявок."
    )
    result: Optional[DraftSupplyCreateStatusV1Result] = Field(
        None, description="Результат создания заявок."
    )
    status: Optional[str] = Field(
        None, description="Статус создания заявки."
    )
