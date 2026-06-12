"""Схемы метода cargoes_transport_activate_status (статус включения транспортных грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesTransportActivateStatusRequest(BaseModel):
    """Параметры запроса статуса включения транспортных грузомест.

    Attributes:
        operation_id: Идентификатор операции включения транспортных грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции включения транспортных грузомест."
    )


class CargoesTransportActivateStatusResponse(BaseModel):
    """Ответ со статусом включения или отключения транспортных грузомест.

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
