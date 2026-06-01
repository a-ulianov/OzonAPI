"""Схемы метода carriage_pass_update (обновление пропуска для перевозки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ArrivalPassDriverVehicle


class CarriagePassUpdateArrivalPass(ArrivalPassDriverVehicle):
    """Данные обновляемого пропуска для перевозки.

    Attributes:
        id: Идентификатор пропуска
        with_returns: `true`, если будете вывозить возвраты (по умолчанию — `false`)
    """
    id: int = Field(..., description="Идентификатор пропуска.")
    with_returns: Optional[bool] = Field(
        None, description="`true`, если будете вывозить возвраты. По умолчанию — `false`."
    )


class CarriagePassUpdateRequest(BaseModel):
    """Параметры запроса обновления пропуска для перевозки.

    Attributes:
        arrival_passes: Список пропусков
        carriage_id: Идентификатор перевозки
    """
    arrival_passes: list[CarriagePassUpdateArrivalPass] = Field(
        ..., description="Список пропусков."
    )
    carriage_id: int = Field(..., description="Идентификатор перевозки.")


class CarriagePassUpdateResponse(BaseModel):
    """Ответ на обновление пропуска для перевозки.

    Notes:
        • Тело ответа отсутствует — успешное обновление возвращает код 200.
    """
