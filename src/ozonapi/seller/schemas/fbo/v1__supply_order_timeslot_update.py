"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_UpdateSupplyOrderTimeslot"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import SupplyOrderTimeslot


class SupplyOrderTimeslotUpdateRequest(BaseModel):
    """Описывает схему запроса на обновление интервала поставки.

    Attributes:
        supply_order_id: Идентификатор заявки на поставку
        timeslot: Новый интервал поставки
    """
    supply_order_id: int = Field(
        ..., description="Идентификатор заявки на поставку."
    )
    timeslot: SupplyOrderTimeslot = Field(
        ..., description="Новый интервал поставки."
    )


class SupplyOrderTimeslotUpdateResponse(BaseModel):
    """Описывает схему ответа на запрос обновления интервала поставки.

    Attributes:
        operation_id: Идентификатор операции (для проверки статуса)
        errors: Список ошибок обновления (строками)
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции (для проверки статуса)."
    )
    errors: Optional[list[str]] = Field(
        default_factory=list, description="Список ошибок обновления."
    )
