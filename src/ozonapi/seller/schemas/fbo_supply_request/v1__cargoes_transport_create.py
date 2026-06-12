"""Схемы метода cargoes_transport_create (создание транспортного грузоместа, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesTransportCreateItem(BaseModel):
    """Транспортное грузоместо для создания.

    Attributes:
        count: Количество транспортных грузомест
        type: Тип транспортного грузоместа (`PALLET`)
    """
    count: int = Field(..., description="Количество транспортных грузомест.")
    type: str = Field(
        ..., description="Тип транспортного грузоместа. Возможное значение: `PALLET`."
    )


class CargoesTransportCreateRequest(BaseModel):
    """Параметры запроса создания транспортных грузомест.

    Attributes:
        supply_id: Идентификатор поставки
        transport_cargoes: Транспортные грузоместа для создания
    """
    supply_id: int = Field(..., description="Идентификатор поставки.")
    transport_cargoes: list[CargoesTransportCreateItem] = Field(
        ..., description="Транспортные грузоместа для создания."
    )


class CargoesTransportCreateResponse(BaseModel):
    """Ответ на создание транспортных грузомест.

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
