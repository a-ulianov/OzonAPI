"""Схемы метода cargoes_delete (удаление грузомест и транспортных грузомест, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesDeleteRequest(BaseModel):
    """Параметры запроса удаления грузомест и транспортных грузомест.

    Attributes:
        cargo_ids: Идентификаторы грузомест
        supply_id: Идентификатор поставки
        transport_cargo_deletion_type: Способ удаления транспортных грузомест
            (`UNBIND_CONTAINED_CARGOES` — отвязать вложенные грузоместа,
            `DELETE_CONTAINED_CARGOES` — удалить вложенные грузоместа)
        transport_cargo_ids: Идентификаторы транспортных грузомест
    """
    cargo_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы грузомест."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")
    transport_cargo_deletion_type: str = Field(
        ...,
        description=(
            "Способ удаления транспортных грузомест. Возможные значения: "
            "`UNBIND_CONTAINED_CARGOES` — отвязать вложенные грузоместа, "
            "`DELETE_CONTAINED_CARGOES` — удалить вложенные грузоместа."
        )
    )
    transport_cargo_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы транспортных грузомест."
    )


class CargoesDeleteCargoErrorReason(BaseModel):
    """Ошибки удаления конкретного грузоместа.

    Attributes:
        cargo_id: Идентификатор грузоместа
        error_reasons: Причины ошибки
    """
    cargo_id: Optional[int] = Field(None, description="Идентификатор грузоместа.")
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )


class CargoesDeleteTransportCargoErrorReason(BaseModel):
    """Ошибки удаления конкретного транспортного грузоместа.

    Attributes:
        error_reasons: Причины ошибки
        transport_cargo_id: Идентификатор транспортного грузоместа
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
    transport_cargo_id: Optional[int] = Field(
        None, description="Идентификатор транспортного грузоместа."
    )


class CargoesDeleteErrors(BaseModel):
    """Ошибки удаления грузомест и транспортных грузомест.

    Attributes:
        cargo_error_reasons: Ошибки по отдельным грузоместам
        supply_error_reasons: Ошибки уровня поставки
        transport_cargo_error_reasons: Ошибки по транспортным грузоместам
    """
    cargo_error_reasons: Optional[list[CargoesDeleteCargoErrorReason]] = Field(
        None, description="Ошибки по отдельным грузоместам."
    )
    supply_error_reasons: Optional[list[str]] = Field(
        None, description="Ошибки уровня поставки."
    )
    transport_cargo_error_reasons: Optional[
        list[CargoesDeleteTransportCargoErrorReason]
    ] = Field(None, description="Ошибки по транспортным грузоместам.")


class CargoesDeleteResponse(BaseModel):
    """Ответ на удаление грузомест и транспортных грузомест.

    Attributes:
        errors: Ошибки операции
        operation_id: Идентификатор операции
    """
    errors: Optional[CargoesDeleteErrors] = Field(
        None, description="Ошибки операции."
    )
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
