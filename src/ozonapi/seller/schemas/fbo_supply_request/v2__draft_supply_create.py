"""Схемы метода draft_supply_create (создать заявку по черновику, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyType


class DraftSupplyCreateTimeslot(BaseModel):
    """Таймслот отгрузки.

    Attributes:
        from_in_timezone: Начало таймслота
        to_in_timezone: Конец таймслота
    """
    from_in_timezone: Optional[str] = Field(
        None, description="Начало таймслота."
    )
    to_in_timezone: Optional[str] = Field(
        None, description="Конец таймслота."
    )


class DraftSupplyCreateSelectedClusterWarehouse(BaseModel):
    """Информация о кластере и складе размещения.

    Attributes:
        macrolocal_cluster_id: Идентификатор макролокального кластера
        storage_warehouse_id: Идентификатор склада размещения
    """
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    storage_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада размещения."
    )


class DraftSupplyCreateRequest(BaseModel):
    """Параметры запроса создания заявки на поставку по черновику.

    Attributes:
        draft_id: Идентификатор черновика
        selected_cluster_warehouses: Информация о кластерах и складах размещения
        timeslot: Таймслот отгрузки
        supply_type: Тип поставки
    """
    draft_id: int = Field(..., description="Идентификатор черновика.")
    selected_cluster_warehouses: list[DraftSupplyCreateSelectedClusterWarehouse] = Field(
        ..., description="Информация о кластерах и складах размещения."
    )
    timeslot: Optional[DraftSupplyCreateTimeslot] = Field(
        None, description="Таймслот отгрузки."
    )
    supply_type: SupplyType = Field(..., description="Тип поставки.")


class DraftSupplyCreateResponse(BaseModel):
    """Ответ на создание заявки на поставку по черновику.

    Attributes:
        draft_id: Идентификатор черновика
        error_reasons: Причины ошибки
    """
    draft_id: Optional[int] = Field(
        None, description="Идентификатор черновика."
    )
    error_reasons: Optional[list[str]] = Field(
        None, description="Причины ошибки."
    )
