"""Схемы метода draft_supply_create_v1 (создать заявку по черновику, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .v2__draft_supply_create import DraftSupplyCreateTimeslot


class DraftSupplyCreateV1Request(BaseModel):
    """Параметры запроса создания заявки на поставку по черновику (версия 1).

    Attributes:
        draft_id: Идентификатор черновика
        timeslot: Таймслот отгрузки
        warehouse_id: Идентификатор склада размещения
    """
    draft_id: int = Field(..., description="Идентификатор черновика.")
    timeslot: Optional[DraftSupplyCreateTimeslot] = Field(
        None, description="Таймслот отгрузки."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада размещения."
    )


class DraftSupplyCreateV1Response(BaseModel):
    """Ответ на создание заявки на поставку по черновику (версия 1).

    Attributes:
        operation_id: Идентификатор операции создания заявки
    """
    operation_id: Optional[str] = Field(
        None, description="Идентификатор операции создания заявки."
    )
