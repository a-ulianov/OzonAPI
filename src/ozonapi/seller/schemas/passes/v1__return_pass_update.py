"""Схемы метода return_pass_update (обновление пропуска для возврата, v1)."""
from pydantic import BaseModel, Field

from .entities import ArrivalPassDriverVehicle


class ReturnPassUpdateArrivalPass(ArrivalPassDriverVehicle):
    """Данные обновляемого пропуска для возврата.

    Attributes:
        arrival_pass_id: Идентификатор пропуска
        arrival_time: Время прибытия в формате UTC — в это время начнёт действовать пропуск
    """
    arrival_pass_id: int = Field(..., description="Идентификатор пропуска.")
    arrival_time: str = Field(
        ...,
        description="Время прибытия в формате UTC. В это время начнёт действовать пропуск."
    )


class ReturnPassUpdateRequest(BaseModel):
    """Параметры запроса обновления пропуска для возврата.

    Attributes:
        arrival_passes: Список пропусков
    """
    arrival_passes: list[ReturnPassUpdateArrivalPass] = Field(
        ..., description="Список пропусков."
    )


class ReturnPassUpdateResponse(BaseModel):
    """Ответ на обновление пропуска для возврата.

    Notes:
        • Тело ответа отсутствует — успешное обновление возвращает код 200.
    """
