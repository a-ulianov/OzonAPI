"""Схемы метода cargoes_delete_status_v1 (статус удаления грузоместа, v1).

Notes:
    • Устаревшая версия. Канонический метод — `cargoes_delete_status()` (v2);
      данная v1-версия доступна как `cargoes_delete_status_v1()`.
"""
from typing import Optional

from pydantic import BaseModel, Field

from .v1__cargoes_delete import CargoesDeleteV1Errors


class CargoesDeleteStatusV1Request(BaseModel):
    """Параметры запроса статуса удаления грузомест.

    Attributes:
        operation_id: Идентификатор операции удаления грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции удаления грузомест."
    )


class CargoesDeleteStatusV1Response(BaseModel):
    """Ответ со статусом удаления грузомест.

    Attributes:
        errors: Ошибки операции
        status: Статус операции
    """
    errors: Optional[CargoesDeleteV1Errors] = Field(
        None, description="Ошибки операции."
    )
    status: Optional[str] = Field(None, description="Статус операции.")
