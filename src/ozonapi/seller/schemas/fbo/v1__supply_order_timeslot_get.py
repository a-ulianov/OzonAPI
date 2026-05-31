"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderTimeslots"""
from typing import Any, Optional

from pydantic import BaseModel, Field

from .entities import SupplyOrderTimeslot


class SupplyOrderTimeslotGetRequest(BaseModel):
    """Описывает схему запроса на получение доступных интервалов поставки.

    Attributes:
        supply_order_id: Идентификатор заявки на поставку
    """
    supply_order_id: int = Field(
        ..., description="Идентификатор заявки на поставку."
    )


class SupplyOrderTimeslotGetResponse(BaseModel):
    """Описывает схему ответа на запрос доступных интервалов поставки.

    Attributes:
        timeslots: Список доступных интервалов поставки
        timezone: Часовой пояс интервалов
    """
    timeslots: Optional[list[SupplyOrderTimeslot]] = Field(
        default_factory=list, description="Список доступных интервалов поставки."
    )
    timezone: Optional[Any] = Field(
        None, description="Часовой пояс интервалов."
    )
