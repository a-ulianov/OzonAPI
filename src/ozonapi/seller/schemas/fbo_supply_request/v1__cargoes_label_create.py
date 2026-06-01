"""Схемы метода cargoes_label_create (генерация этикеток грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesLabelErrors(BaseModel):
    """Ошибки операции с этикетками грузомест.

    Attributes:
        error_reasons: Причины ошибки
    """
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )


class CargoesLabelCreateCargo(BaseModel):
    """Грузоместо для генерации этикетки.

    Attributes:
        cargo_id: Идентификатор грузоместа
    """
    cargo_id: Optional[int] = Field(
        None, description="Идентификатор грузоместа."
    )


class CargoesLabelCreateRequest(BaseModel):
    """Параметры запроса генерации этикеток грузомест.

    Attributes:
        cargoes: Информация о грузоместах
        supply_id: Идентификатор поставки
    """
    cargoes: Optional[list[CargoesLabelCreateCargo]] = Field(
        None, description="Информация о грузоместах."
    )
    supply_id: int = Field(..., description="Идентификатор поставки.")


class CargoesLabelCreateResponse(BaseModel):
    """Ответ на генерацию этикеток грузомест.

    Attributes:
        operation_id: Идентификатор операции
        errors: Ошибки операции
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции."
    )
    errors: Optional[CargoesLabelErrors] = Field(
        None, description="Ошибки операции."
    )
