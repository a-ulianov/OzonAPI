"""Схемы метода return_pass_create (создание пропуска для возврата, v1)."""
from typing import Union

from pydantic import BaseModel, Field

from .entities import ArrivalPassDriverVehicle


class ReturnPassCreateArrivalPass(ArrivalPassDriverVehicle):
    """Данные пропуска для возврата.

    Attributes:
        arrival_time: Время прибытия в формате UTC — в это время пропуск начнёт действовать
        dropoff_point_id: Идентификатор склада, на который оформляется пропуск
        warehouse_id: Идентификатор склада продавца
    """
    arrival_time: str = Field(
        ...,
        description="Время прибытия в формате UTC. В это время пропуск начнёт действовать."
    )
    dropoff_point_id: int = Field(
        ..., description="Идентификатор склада, на который оформляется пропуск."
    )
    warehouse_id: int = Field(..., description="Идентификатор склада продавца.")


class ReturnPassCreateRequest(BaseModel):
    """Параметры запроса создания пропуска для возврата.

    Attributes:
        arrival_passes: Список пропусков
    """
    arrival_passes: list[ReturnPassCreateArrivalPass] = Field(
        ..., description="Список пропусков."
    )


class ReturnPassCreateResponse(BaseModel):
    """Ответ на создание пропуска для возврата.

    Attributes:
        arrival_pass_ids: Идентификаторы созданных пропусков
    """
    arrival_pass_ids: list[Union[int, str]] = Field(
        default_factory=list, description="Идентификаторы созданных пропусков."
    )
