"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderV3"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .entities import SupplyOrderTimeslot, SupplyOrderTimezoneInfo


class SupplyOrderGetRequest(BaseModel):
    """Описывает схему запроса на получение информации о заявках на поставку.

    Attributes:
        order_ids: Список идентификаторов заявок на поставку
    """
    order_ids: list[int] = Field(
        ..., description="Список идентификаторов заявок на поставку."
    )


class SupplyOrderGetDropOffWarehouse(BaseModel):
    """Пункт отгрузки заявки на поставку.

    Attributes:
        address: Адрес пункта отгрузки
        name: Название пункта отгрузки
        warehouse_id: Идентификатор пункта отгрузки
    """
    address: Optional[str] = Field(
        None, description="Адрес пункта отгрузки."
    )
    name: Optional[str] = Field(
        None, description="Название пункта отгрузки."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор пункта отгрузки."
    )


class SupplyOrderGetOrderTags(BaseModel):
    """Теги заявки на поставку.

    Attributes:
        is_econom: `true`, если заявка относится к товарам «Суперэконом»
        is_pickup: `true`, если доступна отгрузка курьером
        is_quant: `true`, если в поставке есть кванты
        is_super_fbo: `true`, если продавец подключён к Super-поставкам
        is_virtual: `true`, если заявка виртуальная
        original_supply_id: Идентификатор исходной поставки
        product_super_fbo: `true`, если заявка относится к Super-товарам
        seller_warehouse_id: Идентификатор склада продавца
    """
    is_econom: Optional[bool] = Field(
        None, description="`true`, если заявка относится к товарам «Суперэконом»."
    )
    is_pickup: Optional[bool] = Field(
        None, description="`true`, если доступна отгрузка курьером."
    )
    is_quant: Optional[bool] = Field(
        None, description="`true`, если в поставке есть кванты."
    )
    is_super_fbo: Optional[bool] = Field(
        None, description="`true`, если продавец подключён к Super-поставкам."
    )
    is_virtual: Optional[bool] = Field(
        None, description="`true`, если заявка виртуальная."
    )
    original_supply_id: Optional[int] = Field(
        None, description="Идентификатор исходной поставки."
    )
    product_super_fbo: Optional[bool] = Field(
        None, description="`true`, если заявка относится к Super-товарам."
    )
    seller_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада продавца."
    )


class SupplyOrderGetStorageWarehouse(BaseModel):
    """Склад хранения поставки.

    Attributes:
        address: Адрес склада хранения
        arrival_date: Дата прибытия на склад хранения
        name: Название склада хранения
        warehouse_id: Идентификатор склада хранения
    """
    address: Optional[str] = Field(
        None, description="Адрес склада хранения."
    )
    arrival_date: Optional[datetime.datetime] = Field(
        None, description="Дата прибытия на склад хранения."
    )
    name: Optional[str] = Field(
        None, description="Название склада хранения."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада хранения."
    )


class SupplyOrderGetSupplyTags(BaseModel):
    """Теги поставки.

    Attributes:
        freeze_stock_for_marking: `true`, если включена схема поставки с заморозкой стока
        is_ettn_required: `true`, если для поставки нужна электронная ТТН
        is_evsd_required: `true`, если в поставке есть товары с сертификацией «Меркурий»
        is_jewelry: `true`, если в поставке есть ювелирные товары
        is_marking_possible: `true`, если в поставке есть товары, для которых возможна маркировка
        is_marking_required: `true`, если в поставке есть товары, для которых маркировка обязательна
        is_utd: `true`, если для поставки нужно передать УПД
    """
    freeze_stock_for_marking: Optional[bool] = Field(
        None, description="`true`, если включена схема поставки с заморозкой стока."
    )
    is_ettn_required: Optional[bool] = Field(
        None, description="`true`, если для поставки нужна электронная ТТН."
    )
    is_evsd_required: Optional[bool] = Field(
        None, description="`true`, если в поставке есть товары с сертификацией «Меркурий»."
    )
    is_jewelry: Optional[bool] = Field(
        None, description="`true`, если в поставке есть ювелирные товары."
    )
    is_marking_possible: Optional[bool] = Field(
        None, description="`true`, если в поставке есть товары, для которых возможна маркировка."
    )
    is_marking_required: Optional[bool] = Field(
        None, description="`true`, если в поставке есть товары, для которых маркировка обязательна."
    )
    is_utd: Optional[bool] = Field(
        None, description="`true`, если для поставки нужно передать УПД."
    )


class SupplyOrderGetSupply(BaseModel):
    """Поставка в составе заявки на поставку.

    Attributes:
        supply_id: Идентификатор поставки
        bundle_id: Идентификатор состава поставки
        state: Статус поставки (строкой)
        is_crossdock: `true`, если поставка кросс-докинг
        macrolocal_cluster_id: Идентификатор кластера размещения
        storage_warehouse: Склад хранения поставки
        supply_tags: Теги поставки
    """
    supply_id: Optional[int] = Field(
        None, description="Идентификатор поставки."
    )
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор состава поставки."
    )
    state: Optional[str] = Field(
        None, description="Статус поставки."
    )
    is_crossdock: Optional[bool] = Field(
        None, description="`true`, если поставка кросс-докинг."
    )
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор кластера размещения."
    )
    storage_warehouse: Optional[SupplyOrderGetStorageWarehouse] = Field(
        None, description="Склад хранения поставки."
    )
    supply_tags: Optional[SupplyOrderGetSupplyTags] = Field(
        None, description="Теги поставки."
    )


class SupplyOrderGetTimeslot(BaseModel):
    """Интервал поставки заявки с информацией о часовом поясе.

    Attributes:
        timeslot: Интервал поставки
        timezone_info: Информация о часовом поясе
    """
    timeslot: Optional[SupplyOrderTimeslot] = Field(
        None, description="Интервал поставки."
    )
    timezone_info: Optional[SupplyOrderTimezoneInfo] = Field(
        None, description="Информация о часовом поясе."
    )


class SupplyOrderGetOrder(BaseModel):
    """Заявка на поставку (подробная информация).

    Attributes:
        order_id: Идентификатор заявки на поставку
        order_number: Номер заявки на поставку
        state: Статус заявки (строкой)
        created_date: Дата создания заявки
        state_updated_date: Дата обновления статуса заявки
        data_filling_deadline_utc: Крайний срок заполнения данных по поставке (UTC)
        dropoff_warehouse: Пункт отгрузки
        order_tags: Теги заявки
        supplies: Список поставок в заявке
        timeslot: Интервал поставки
    """
    order_id: Optional[int] = Field(
        None, description="Идентификатор заявки на поставку."
    )
    order_number: Optional[str] = Field(
        None, description="Номер заявки на поставку."
    )
    state: Optional[str] = Field(
        None, description="Статус заявки."
    )
    created_date: Optional[datetime.datetime] = Field(
        None, description="Дата создания заявки."
    )
    state_updated_date: Optional[datetime.datetime] = Field(
        None, description="Дата обновления статуса заявки."
    )
    data_filling_deadline_utc: Optional[datetime.datetime] = Field(
        None, description="Крайний срок заполнения данных по поставке (UTC)."
    )
    dropoff_warehouse: Optional[SupplyOrderGetDropOffWarehouse] = Field(
        None, description="Пункт отгрузки."
    )
    order_tags: Optional[SupplyOrderGetOrderTags] = Field(
        None, description="Теги заявки."
    )
    supplies: Optional[list[SupplyOrderGetSupply]] = Field(
        default_factory=list, description="Список поставок в заявке."
    )
    timeslot: Optional[SupplyOrderGetTimeslot] = Field(
        None, description="Интервал поставки."
    )


class SupplyOrderGetResponse(BaseModel):
    """Описывает схему ответа на запрос информации о заявках на поставку.

    Attributes:
        orders: Список заявок на поставку
    """
    orders: Optional[list[SupplyOrderGetOrder]] = Field(
        default_factory=list, description="Список заявок на поставку."
    )
