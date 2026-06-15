"""Схемы метода cargoes_transport_activate (включение транспортных грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesTransportActivateRequest(BaseModel):
    """Параметры запроса включения или отключения транспортных грузомест.

    Attributes:
        is_transport: Признак включения транспортных грузомест в поставке
        supply_id: Идентификатор поставки
    """
    is_transport: bool = Field(
        ..., description="Признак включения транспортных грузомест в поставке."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")


class CargoesTransportActivateResponse(BaseModel):
    """Ответ на включение или отключение транспортных грузомест.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
