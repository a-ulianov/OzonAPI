"""Схемы метода warehouse_operation_status (статус операции склада, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class WarehouseOperationStatusRequest(BaseModel):
    """Параметры запроса статуса операции со складом.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: str = Field(..., description="Идентификатор операции.")


class WarehouseOperationStatusError(BaseModel):
    """Ошибка операции со складом.

    Attributes:
        code: Код ошибки
        message: Сообщение об ошибке
    """
    code: Optional[str] = Field(None, description="Код ошибки.")
    message: Optional[str] = Field(None, description="Сообщение об ошибке.")


class WarehouseOperationStatusResult(BaseModel):
    """Результат операции со складом.

    Attributes:
        entity_id: Идентификатор сущности
    """
    entity_id: Optional[int] = Field(None, description="Идентификатор сущности.")


class WarehouseOperationStatusResponse(BaseModel):
    """Ответ со статусом операции со складом.

    Attributes:
        error: Ошибка операции
        result: Результат операции
        status: Статус операции
        type: Тип операции
    """
    error: Optional[WarehouseOperationStatusError] = Field(
        None, description="Ошибка операции."
    )
    result: Optional[WarehouseOperationStatusResult] = Field(
        None, description="Результат операции."
    )
    status: Optional[str] = Field(None, description="Статус операции.")
    type: Optional[str] = Field(None, description="Тип операции.")
