"""Схемы метода draft_timeslot_info (доступные таймслоты, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo_supply_request import SupplyType


class DraftTimeslotInfoSelectedClusterWarehouse(BaseModel):
    """Информация о кластере и складе хранения.

    Attributes:
        macrolocal_cluster_id: Идентификатор макролокального кластера
        storage_warehouse_id: Идентификатор склада хранения
    """
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор макролокального кластера."
    )
    storage_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада хранения."
    )


class DraftTimeslotInfoRequest(BaseModel):
    """Параметры запроса доступных таймслотов.

    Attributes:
        date_from: Дата начала периода
        date_to: Дата окончания периода
        draft_id: Идентификатор черновика
        supply_type: Тип поставки
        selected_cluster_warehouses: Информация о кластерах и складах хранения
    """
    date_from: str = Field(..., description="Дата начала периода.")
    date_to: str = Field(..., description="Дата окончания периода.")
    draft_id: int = Field(..., description="Идентификатор черновика.")
    supply_type: SupplyType = Field(..., description="Тип поставки.")
    selected_cluster_warehouses: list[DraftTimeslotInfoSelectedClusterWarehouse] = Field(
        ..., description="Информация о кластерах и складах хранения."
    )


class DraftTimeslotSlot(BaseModel):
    """Таймслот.

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


class DraftTimeslotDay(BaseModel):
    """Таймслоты по дате.

    Attributes:
        date_in_timezone: Дата таймслотов
        timeslots: Таймслоты
    """
    date_in_timezone: Optional[str] = Field(
        None, description="Дата таймслотов."
    )
    timeslots: Optional[list[DraftTimeslotSlot]] = Field(
        None, description="Таймслоты."
    )


class DraftTimeslotWarehouseTimeslots(BaseModel):
    """Таймслоты склада.

    Attributes:
        current_time_in_timezone: Текущее время в часовом поясе склада
        days: Таймслоты по датам
        warehouse_timezone: Часовой пояс склада
    """
    current_time_in_timezone: Optional[str] = Field(
        None, description="Текущее время в часовом поясе склада."
    )
    days: Optional[list[DraftTimeslotDay]] = Field(
        None, description="Таймслоты по датам."
    )
    warehouse_timezone: Optional[str] = Field(
        None, description="Часовой пояс склада."
    )


class DraftTimeslotInfoResult(BaseModel):
    """Результат запроса таймслотов.

    Attributes:
        drop_off_warehouse_timeslots: Таймслоты склада
        requested_date_from: Дата начала периода
        requested_date_to: Дата окончания периода
    """
    drop_off_warehouse_timeslots: Optional[DraftTimeslotWarehouseTimeslots] = Field(
        None, description="Таймслоты склада."
    )
    requested_date_from: Optional[str] = Field(
        None, description="Дата начала периода."
    )
    requested_date_to: Optional[str] = Field(
        None, description="Дата окончания периода."
    )


class DraftTimeslotInfoResponse(BaseModel):
    """Ответ с доступными таймслотами.

    Attributes:
        error_reason: Причина ошибки
        result: Результат запроса таймслотов
    """
    error_reason: Optional[str] = Field(
        None, description="Причина ошибки."
    )
    result: Optional[DraftTimeslotInfoResult] = Field(
        None, description="Результат запроса таймслотов."
    )
