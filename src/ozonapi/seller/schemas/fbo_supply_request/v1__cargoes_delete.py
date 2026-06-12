"""Схемы метода cargoes_delete_v1 (удаление грузоместа, v1).

Notes:
    • Устаревшая версия. Ozon выпустил v2 `/v2/cargoes/delete`, поддерживающую
      удаление транспортных грузомест; канонический метод — `cargoes_delete()`.
      Данная v1-версия доступна как `cargoes_delete_v1()`.
"""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesDeleteV1Request(BaseModel):
    """Параметры запроса удаления грузомест.

    Attributes:
        cargo_ids: Идентификаторы грузомест
        supply_id: Идентификатор поставки
    """
    cargo_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы грузомест."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")


class CargoesDeleteV1CargoErrorReason(BaseModel):
    """Ошибки удаления конкретного грузоместа.

    Attributes:
        cargo_id: Идентификатор грузоместа
        error_reasons: Причины ошибки
    """
    cargo_id: Optional[int] = Field(None, description="Идентификатор грузоместа.")
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )


class CargoesDeleteV1Errors(BaseModel):
    """Ошибки удаления грузомест.

    Attributes:
        cargo_error_reasons: Ошибки по отдельным грузоместам
        supply_error_reasons: Ошибки уровня поставки
    """
    cargo_error_reasons: Optional[list[CargoesDeleteV1CargoErrorReason]] = Field(
        None, description="Ошибки по отдельным грузоместам."
    )
    supply_error_reasons: Optional[list[str]] = Field(
        None, description="Ошибки уровня поставки."
    )


class CargoesDeleteV1Response(BaseModel):
    """Ответ на удаление грузомест.

    Attributes:
        errors: Ошибки операции
        operation_id: Идентификатор операции
    """
    errors: Optional[CargoesDeleteV1Errors] = Field(
        None, description="Ошибки операции."
    )
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
