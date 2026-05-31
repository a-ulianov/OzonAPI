"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderListV3"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.fbo import (
    SupplyOrderSortDirection,
    SupplyOrderSortField,
    SupplyOrderState,
    TimeslotFilterType,
)


class SupplyOrderListTimeslotFromRange(BaseModel):
    """Фильтр по диапазону начала интервала поставки.

    Attributes:
        from_: Дата начала диапазона (сериализуется как `from`)
        to: Дата окончания диапазона
        timeslot_filter_type: Тип фильтрации по времени
    """
    model_config = {'populate_by_name': True}

    from_: Optional[datetime.datetime] = Field(
        None, alias="from", description="Дата начала диапазона."
    )
    to: Optional[datetime.datetime] = Field(
        None, description="Дата окончания диапазона."
    )
    timeslot_filter_type: Optional[TimeslotFilterType] = Field(
        None, description="Тип фильтрации по времени."
    )


class SupplyOrderListFilter(BaseModel):
    """Фильтр для поиска заявок на поставку.

    Attributes:
        states: Список статусов заявок
        dropoff_warehouse_ids: Список идентификаторов пунктов отгрузки
        order_number_search: Номер заявки на поставку для поиска
        timeslot_from_range: Фильтр по диапазону начала интервала поставки
    """
    states: list[SupplyOrderState] = Field(
        ..., description="Список статусов заявок."
    )
    dropoff_warehouse_ids: Optional[list[int]] = Field(
        None, description="Список идентификаторов пунктов отгрузки."
    )
    order_number_search: Optional[str] = Field(
        None, description="Номер заявки на поставку для поиска."
    )
    timeslot_from_range: Optional[SupplyOrderListTimeslotFromRange] = Field(
        None, description="Фильтр по диапазону начала интервала поставки."
    )


class SupplyOrderListRequest(BaseModel):
    """Описывает схему запроса на получение списка заявок на поставку.

    Attributes:
        filter: Фильтр для поиска заявок
        limit: Количество значений на странице
        sort_by: Поле сортировки
        sort_dir: Направление сортировки
        last_id: Идентификатор последнего значения на странице
    """
    filter: SupplyOrderListFilter = Field(
        ..., description="Фильтр для поиска заявок."
    )
    limit: int = Field(
        ..., description="Количество значений на странице."
    )
    sort_by: SupplyOrderSortField = Field(
        ..., description="Поле сортировки."
    )
    sort_dir: Optional[SupplyOrderSortDirection] = Field(
        None, description="Направление сортировки."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )


class SupplyOrderListResponse(BaseModel):
    """Описывает схему ответа на запрос списка заявок на поставку.

    Notes:
        • Метод возвращает только идентификаторы заявок; подробности получайте
          методом `supply_order_get`.

    Attributes:
        order_ids: Список идентификаторов заявок на поставку
        last_id: Идентификатор последнего значения на странице
    """
    order_ids: Optional[list[int]] = Field(
        default_factory=list, description="Список идентификаторов заявок на поставку."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )
