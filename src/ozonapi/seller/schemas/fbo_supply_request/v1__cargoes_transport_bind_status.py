"""Схемы метода cargoes_transport_bind_status (статус связывания грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesTransportBindStatusRequest(BaseModel):
    """Параметры запроса статуса связывания грузомест и транспортных грузомест.

    Attributes:
        operation_id: Идентификатор операции связывания грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции связывания грузомест."
    )


class CargoesTransportBindStatusResponse(BaseModel):
    """Ответ со статусом связывания или отвязывания грузомест.

    Attributes:
        error_reasons: Причины ошибок
        status: Статус операции (`SUCCESS`, `IN_PROGRESS`, `FAILED`)
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибок."
    )
    status: Optional[str] = Field(
        None,
        description="Статус операции. Возможные значения: `SUCCESS`, `IN_PROGRESS`, `FAILED`."
    )
