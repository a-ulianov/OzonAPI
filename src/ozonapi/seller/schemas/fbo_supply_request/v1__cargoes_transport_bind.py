"""Схемы метода cargoes_transport_bind (связывание грузомест и транспортных грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesTransportBindItem(BaseModel):
    """Связывание грузомест с транспортным грузоместом.

    Attributes:
        cargo_ids: Идентификаторы грузомест
        transport_cargo_id: Идентификатор транспортного грузоместа
    """
    cargo_ids: list[str] = Field(..., description="Идентификаторы грузомест.")
    transport_cargo_id: int = Field(
        ..., description="Идентификатор транспортного грузоместа."
    )


class CargoesTransportBindRequest(BaseModel):
    """Параметры запроса связывания или отвязывания грузомест и транспортных грузомест.

    Attributes:
        cargoes_unbind_transport_cargoes: Идентификаторы грузомест для отвязывания
        supply_id: Идентификатор поставки
        transport_cargo_bind: Связывания грузомест с транспортными грузоместами
    """
    cargoes_unbind_transport_cargoes: Optional[list[str]] = Field(
        None, description="Идентификаторы грузомест для отвязывания."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")
    transport_cargo_bind: Optional[list[CargoesTransportBindItem]] = Field(
        None, description="Связывания грузомест с транспортными грузоместами."
    )


class CargoesTransportBindResponse(BaseModel):
    """Ответ на связывание или отвязывание грузомест и транспортных грузомест.

    Attributes:
        error_reasons: Причины ошибок
        operation_id: Идентификатор операции
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибок."
    )
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
