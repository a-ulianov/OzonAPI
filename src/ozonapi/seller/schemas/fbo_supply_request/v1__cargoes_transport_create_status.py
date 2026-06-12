"""Схемы метода cargoes_transport_create_status (статус создания транспортного грузоместа, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesTransportCreateStatusRequest(BaseModel):
    """Параметры запроса статуса создания транспортных грузомест.

    Attributes:
        operation_id: Идентификатор операции создания транспортных грузомест
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции создания транспортных грузомест."
    )


class CargoesTransportCreateStatusTransportCargo(BaseModel):
    """Созданное транспортное грузоместо.

    Attributes:
        id: Идентификатор транспортного грузоместа
        type: Тип транспортного грузоместа (`PALLET`)
    """
    id: Optional[int] = Field(
        None, description="Идентификатор транспортного грузоместа."
    )
    type: Optional[str] = Field(
        None, description="Тип транспортного грузоместа. Возможное значение: `PALLET`."
    )


class CargoesTransportCreateStatusResult(BaseModel):
    """Результат создания транспортных грузомест.

    Attributes:
        transport_cargoes: Созданные транспортные грузоместа
    """
    transport_cargoes: Optional[
        list[CargoesTransportCreateStatusTransportCargo]
    ] = Field(None, description="Созданные транспортные грузоместа.")


class CargoesTransportCreateStatusResponse(BaseModel):
    """Ответ со статусом создания транспортных грузомест.

    Attributes:
        error_reasons: Причины ошибок
        result: Результат создания
        status: Статус операции (`SUCCESS`, `IN_PROGRESS`, `FAILED`)
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибок."
    )
    result: Optional[CargoesTransportCreateStatusResult] = Field(
        None, description="Результат создания."
    )
    status: Optional[str] = Field(
        None,
        description="Статус операции. Возможные значения: `SUCCESS`, `IN_PROGRESS`, `FAILED`."
    )
