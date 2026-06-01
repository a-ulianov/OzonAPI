"""Схемы метода cargoes_delete_status (статус удаления грузоместа, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .v1__cargoes_delete import CargoesDeleteErrors


class CargoesDeleteStatusRequest(BaseModel):
    """Параметры запроса статуса удаления грузомест.

    Attributes:
        operation_id: Идентификатор операции удаления грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции удаления грузомест."
    )


class CargoesDeleteStatusResponse(BaseModel):
    """Ответ со статусом удаления грузомест.

    Attributes:
        errors: Ошибки операции
        status: Статус операции
    """
    errors: Optional[CargoesDeleteErrors] = Field(
        None, description="Ошибки операции."
    )
    status: Optional[str] = Field(None, description="Статус операции.")
