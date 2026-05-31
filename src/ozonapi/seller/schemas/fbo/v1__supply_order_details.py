"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderDetails"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .entities import SupplyOrderTimeslot, SupplyOrderTimezoneInfo
from .v3__supply_order_get import SupplyOrderGetStorageWarehouse


class SupplyOrderDetailsRequest(BaseModel):
    """Описывает схему запроса на получение подробной информации о заявке на поставку.

    Attributes:
        order_id: Идентификатор заявки на поставку
    """
    order_id: int = Field(
        ..., description="Идентификатор заявки на поставку."
    )


class SupplyOrderDetailsOrderTags(BaseModel):
    """Теги заявки на поставку.

    Attributes:
        is_econom: `true`, если в заявке есть товары «Суперэконом»
        is_super_fbo: `true`, если продавец подключён к Super-поставкам
        is_virtual: `true`, если заявка виртуальная
        original_supply_id: Идентификатор исходной поставки
        product_super_fbo: `true`, если в заявке есть Super-товары
    """
    is_econom: Optional[bool] = Field(
        None, description="`true`, если в заявке есть товары «Суперэконом»."
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
        None, description="`true`, если в заявке есть Super-товары."
    )


class SupplyOrderDetailsSupplyTags(BaseModel):
    """Теги поставки.

    Attributes:
        is_ettn_required: `true`, если для поставки нужна электронная ТТН
        is_evsd_required: `true`, если в поставке есть товары с сертификацией «Меркурий»
        is_jewelry: `true`, если в поставке есть ювелирные товары
        is_marking_possible: `true`, если в поставке есть товары, для которых возможна маркировка
        is_marking_required: `true`, если в поставке есть товары, для которых маркировка обязательна
        is_utd: `true`, если для поставки нужно передать УПД
    """
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


class SupplyOrderDetailsCancellationAllowability(BaseModel):
    """Возможность отмены поставки.

    Attributes:
        can_set: `true`, если поставку можно отменить
        can_not_set_reasons: Причины невозможности отмены (строками)
    """
    can_set: Optional[bool] = Field(
        None, description="`true`, если поставку можно отменить."
    )
    can_not_set_reasons: Optional[list[str]] = Field(
        default_factory=list, description="Причины невозможности отмены."
    )


class SupplyOrderDetailsContent(BaseModel):
    """Возможность изменения товарного состава поставки.

    Attributes:
        bundle_id: Идентификатор товарного состава
        can_set: `true`, если можно изменить товарный состав
        can_not_set_reasons: Причины невозможности изменения (строками)
    """
    bundle_id: Optional[str] = Field(
        None, description="Идентификатор товарного состава."
    )
    can_set: Optional[bool] = Field(
        None, description="`true`, если можно изменить товарный состав."
    )
    can_not_set_reasons: Optional[list[str]] = Field(
        default_factory=list, description="Причины невозможности изменения."
    )


class SupplyOrderDetailsETTN(BaseModel):
    """Информация об электронной ТТН поставки.

    Attributes:
        contains_valid: `true`, если электронная ТТН действительная
        is_required: `true`, если для поставки нужна электронная ТТН
        is_uploaded: `true`, если электронная ТТН загружена
    """
    contains_valid: Optional[bool] = Field(
        None, description="`true`, если электронная ТТН действительная."
    )
    is_required: Optional[bool] = Field(
        None, description="`true`, если для поставки нужна электронная ТТН."
    )
    is_uploaded: Optional[bool] = Field(
        None, description="`true`, если электронная ТТН загружена."
    )


class SupplyOrderDetailsSupply(BaseModel):
    """Поставка в составе заявки (подробная информация).

    Attributes:
        supply_id: Идентификатор поставки
        supply_state: Статус поставки (строкой)
        is_crossdock: `true`, если поставка кросс-докинг
        macrolocal_cluster_id: Идентификатор кластера размещения
        overdue_reason: Причина просрочки поставки (строкой)
        storage_warehouse: Склад хранения поставки
        cancellation_allowability: Возможность отмены поставки
        content: Возможность изменения товарного состава
        ettn_info: Информация об электронной ТТН
        supply_tags: Теги поставки
    """
    supply_id: Optional[int] = Field(
        None, description="Идентификатор поставки."
    )
    supply_state: Optional[str] = Field(
        None, description="Статус поставки."
    )
    is_crossdock: Optional[bool] = Field(
        None, description="`true`, если поставка кросс-докинг."
    )
    macrolocal_cluster_id: Optional[int] = Field(
        None, description="Идентификатор кластера размещения."
    )
    overdue_reason: Optional[str] = Field(
        None, description="Причина просрочки поставки."
    )
    storage_warehouse: Optional[SupplyOrderGetStorageWarehouse] = Field(
        None, description="Склад хранения поставки."
    )
    cancellation_allowability: Optional[SupplyOrderDetailsCancellationAllowability] = Field(
        None, description="Возможность отмены поставки."
    )
    content: Optional[SupplyOrderDetailsContent] = Field(
        None, description="Возможность изменения товарного состава."
    )
    ettn_info: Optional[SupplyOrderDetailsETTN] = Field(
        None, description="Информация об электронной ТТН."
    )
    supply_tags: Optional[SupplyOrderDetailsSupplyTags] = Field(
        None, description="Теги поставки."
    )


class SupplyOrderDetailsTimeslotValue(BaseModel):
    """Значение интервала поставки с часовым поясом.

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


class SupplyOrderDetailsTimeslot(BaseModel):
    """Интервал поставки заявки с возможностью изменения.

    Attributes:
        can_set: `true`, если можно изменить интервал поставки
        can_not_set_reasons: Причины невозможности изменения (строками)
        value: Текущее значение интервала поставки
    """
    can_set: Optional[bool] = Field(
        None, description="`true`, если можно изменить интервал поставки."
    )
    can_not_set_reasons: Optional[list[str]] = Field(
        default_factory=list, description="Причины невозможности изменения."
    )
    value: Optional[SupplyOrderDetailsTimeslotValue] = Field(
        None, description="Текущее значение интервала поставки."
    )


class SupplyOrderDetailsVehicleValue(BaseModel):
    """Данные о водителе и автомобиле.

    Attributes:
        driver_name: Имя водителя
        driver_phone: Телефон водителя
        driver_is_deleted: `true`, если информация о водителе удалена
        vehicle_model: Модель автомобиля
        vehicle_number: Номер автомобиля
        vehicle_is_deleted: `true`, если информация об автомобиле удалена
    """
    driver_name: Optional[str] = Field(
        None, description="Имя водителя."
    )
    driver_phone: Optional[str] = Field(
        None, description="Телефон водителя."
    )
    driver_is_deleted: Optional[bool] = Field(
        None, description="`true`, если информация о водителе удалена."
    )
    vehicle_model: Optional[str] = Field(
        None, description="Модель автомобиля."
    )
    vehicle_number: Optional[str] = Field(
        None, description="Номер автомобиля."
    )
    vehicle_is_deleted: Optional[bool] = Field(
        None, description="`true`, если информация об автомобиле удалена."
    )


class SupplyOrderDetailsVehicle(BaseModel):
    """Данные о водителе и автомобиле с возможностью изменения.

    Attributes:
        can_set: `true`, если можно изменить данные о водителе или автомобиле
        can_not_set_reasons: Причины невозможности изменения (строками)
        value: Текущие данные о водителе и автомобиле
    """
    can_set: Optional[bool] = Field(
        None, description="`true`, если можно изменить данные о водителе или автомобиле."
    )
    can_not_set_reasons: Optional[list[str]] = Field(
        default_factory=list, description="Причины невозможности изменения."
    )
    value: Optional[SupplyOrderDetailsVehicleValue] = Field(
        None, description="Текущие данные о водителе и автомобиле."
    )


class SupplyOrderDetailsResponse(BaseModel):
    """Описывает схему ответа на запрос подробной информации о заявке на поставку.

    Attributes:
        order_id: Идентификатор заявки на поставку
        order_number: Номер заявки на поставку
        state: Статус заявки (строкой)
        created_date: Дата создания заявки
        state_updated_date: Дата обновления статуса заявки
        data_filling_deadline_utc: Крайний срок заполнения данных по поставке (UTC)
        dropoff_warehouse_id: Идентификатор пункта отгрузки
        order_tags: Теги заявки
        supplies: Список поставок в заявке
        timeslot: Интервал поставки
        vehicle: Данные о водителе и автомобиле
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
    dropoff_warehouse_id: Optional[int] = Field(
        None, description="Идентификатор пункта отгрузки."
    )
    order_tags: Optional[SupplyOrderDetailsOrderTags] = Field(
        None, description="Теги заявки."
    )
    supplies: Optional[list[SupplyOrderDetailsSupply]] = Field(
        default_factory=list, description="Список поставок в заявке."
    )
    timeslot: Optional[SupplyOrderDetailsTimeslot] = Field(
        None, description="Интервал поставки."
    )
    vehicle: Optional[SupplyOrderDetailsVehicle] = Field(
        None, description="Данные о водителе и автомобиле."
    )
