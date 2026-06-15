"""Схемы метода cargoes_label_transport_create (этикетки транспортных грузомест по грузоместу, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesLabelTransportCreateRequest(BaseModel):
    """Параметры запроса генерации этикеток транспортных грузомест.

    Attributes:
        supply_id: Идентификатор поставки
        transport_cargo_ids: Идентификаторы транспортных грузомест
    """
    supply_id: int = Field(..., description="Идентификатор поставки.")
    transport_cargo_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы транспортных грузомест."
    )


class CargoesLabelTransportCreateResponse(BaseModel):
    """Ответ на генерацию этикеток транспортных грузомест.

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
