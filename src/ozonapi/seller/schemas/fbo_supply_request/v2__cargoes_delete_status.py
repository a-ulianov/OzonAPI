"""Схемы метода cargoes_delete_status (статус удаления грузомест, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from .v2__cargoes_delete import CargoesDeleteErrors


class CargoesDeleteStatusRequest(BaseModel):
    """Параметры запроса статуса удаления грузомест и транспортных грузомест.

    Attributes:
        operation_id: Идентификатор операции удаления грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции удаления грузомест."
    )


class CargoesDeleteStatusResponse(BaseModel):
    """Ответ со статусом удаления грузомест и транспортных грузомест.

    Attributes:
        errors: Ошибки операции
        status: Статус операции (`SUCCESS`, `IN_PROGRESS`, `FAILED`)
    """
    errors: Optional[CargoesDeleteErrors] = Field(
        None, description="Ошибки операции."
    )
    status: Optional[str] = Field(
        None,
        description="Статус операции. Возможные значения: `SUCCESS`, `IN_PROGRESS`, `FAILED`."
    )
