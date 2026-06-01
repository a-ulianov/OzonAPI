"""Схемы метода carriage_pass_create (создание пропуска для перевозки, v1)."""
from typing import Optional, Union

from pydantic import BaseModel, Field

from .entities import ArrivalPassDriverVehicle


class CarriagePassCreateArrivalPass(ArrivalPassDriverVehicle):
    """Данные пропуска для перевозки.

    Attributes:
        with_returns: `true`, если будете вывозить возвраты (по умолчанию — `false`)
    """
    with_returns: Optional[bool] = Field(
        None, description="`true`, если будете вывозить возвраты. По умолчанию — `false`."
    )


class CarriagePassCreateRequest(BaseModel):
    """Параметры запроса создания пропуска для перевозки.

    Attributes:
        arrival_passes: Список пропусков
        carriage_id: Идентификатор перевозки
    """
    arrival_passes: list[CarriagePassCreateArrivalPass] = Field(
        ..., description="Список пропусков."
    )
    carriage_id: int = Field(..., description="Идентификатор перевозки.")


class CarriagePassCreateResponse(BaseModel):
    """Ответ на создание пропуска для перевозки.

    Attributes:
        arrival_pass_ids: Идентификаторы созданных пропусков
    """
    arrival_pass_ids: list[Union[int, str]] = Field(
        default_factory=list, description="Идентификаторы созданных пропусков."
    )
