"""https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_WarehouseListV2"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import (
    CarriageLabelType,
    FirstMileTypeV2,
    WarehouseWorkingDayV2,
)


class WarehouseListRequest(BaseModel):
    """Описывает схему запроса на получение списка складов FBS и rFBS (API v2).

    Attributes:
        limit: Количество значений в ответе
        cursor: Указатель для выборки следующих данных
        warehouse_ids: Фильтр по идентификаторам складов
    """
    limit: int = Field(
        100, description="Количество значений в ответе.", ge=1
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )


class WarehouseListAddressInfo(BaseModel):
    """Информация об адресе склада.

    Attributes:
        address: Адрес склада
        latitude: Широта
        longitude: Долгота
        utc: Часовой пояс
    """
    address: Optional[str] = Field(None, description="Адрес склада.")
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")
    utc: Optional[str] = Field(None, description="Часовой пояс.")


class WarehouseListFirstMile(BaseModel):
    """Настройки первой мили склада.

    Attributes:
        dropoff_point_id: Идентификатор drop-off пункта
        first_mile_is_changing: Признак, что настройки склада обновляются
        timeslot_from: Время начала таймслота
        timeslot_id: Идентификатор таймслота
        timeslot_to: Время окончания таймслота
        type: Тип первой мили
    """
    dropoff_point_id: Optional[str] = Field(None, description="Идентификатор drop-off пункта.")
    first_mile_is_changing: Optional[bool] = Field(
        None, description="Признак, что настройки склада обновляются."
    )
    timeslot_from: Optional[str] = Field(None, description="Время начала таймслота.")
    timeslot_id: Optional[int] = Field(None, description="Идентификатор таймслота.")
    timeslot_to: Optional[str] = Field(None, description="Время окончания таймслота.")
    type: Optional[FirstMileTypeV2] = Field(None, description="Тип первой мили.")


class WarehouseListWorkingHours(BaseModel):
    """Часы работы склада.

    Attributes:
        time_from: Время начала работы
        time_to: Время окончания работы
    """
    time_from: Optional[datetime.datetime] = Field(None, description="Время начала работы.")
    time_to: Optional[datetime.datetime] = Field(None, description="Время окончания работы.")


class WarehouseListTimetable(BaseModel):
    """Расписание работы склада.

    Attributes:
        timetable_from: Дата начала работы склада
        timetable_to: Дата окончания работы склада
        working_hours: Часы работы склада
    """
    timetable_from: Optional[datetime.datetime] = Field(None, description="Дата начала работы склада.")
    timetable_to: Optional[datetime.datetime] = Field(None, description="Дата окончания работы склада.")
    working_hours: Optional[list[WarehouseListWorkingHours]] = Field(
        None, description="Часы работы склада."
    )


class WarehouseListItem(BaseModel):
    """Информация о складе (API v2).

    Attributes:
        warehouse_id: Идентификатор склада
        name: Название склада
        status: Статус склада
        warehouse_type: Тип склада
        address_info: Информация об адресе склада
        first_mile: Настройки первой мили
        timetable: Расписание работы склада
        working_days: Рабочие дни склада
        carriage_label_type: Размер этикетки отгрузки
        courier_comment: Комментарий для курьера
        courier_phones: Номера телефонов для связи с курьером
        phone: Номер телефона склада
        created_at: Дата и время создания склада
        updated_at: Дата и время последнего обновления склада
        pause_at: Дата постановки склада на паузу
        cut_in_time: Время на отгрузку в минутах
        sla_cut_in: Минимальное время на сборку заказа в минутах
        has_entrusted_acceptance: Признак подключения доверительной приёмки
        has_postings_limit: Признак наличия лимита минимального количества заказов
        min_postings_limit: Минимальное количество заказов в одной поставке
        postings_limit: Лимит заказов (-1, если лимита нет)
        is_auto_assembly: Признак включённой автосборки
        is_comfort: Признак доставки comfort
        is_express: Признак доставки express
        is_kgt: Признак приёма крупногабаритных товаров
        is_rfbs: Признак работы склада по схеме rFBS
        is_waybill_enabled: Признак включённой печати транспортной накладной
        with_item_list: Признак включённой печати листа подбора
    """
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    name: Optional[str] = Field(None, description="Название склада.")
    status: Optional[str] = Field(None, description="Статус склада.")
    warehouse_type: Optional[str] = Field(None, description="Тип склада.")
    address_info: Optional[WarehouseListAddressInfo] = Field(
        None, description="Информация об адресе склада."
    )
    first_mile: Optional[WarehouseListFirstMile] = Field(
        None, description="Настройки первой мили склада."
    )
    timetable: Optional[WarehouseListTimetable] = Field(
        None, description="Расписание работы склада."
    )
    working_days: Optional[list[WarehouseWorkingDayV2]] = Field(
        None, description="Рабочие дни склада."
    )
    carriage_label_type: Optional[CarriageLabelType] = Field(
        None, description="Размер этикетки отгрузки."
    )
    courier_comment: Optional[str] = Field(None, description="Комментарий для курьера.")
    courier_phones: Optional[list[str]] = Field(
        None, description="Номера телефонов для связи с курьером."
    )
    phone: Optional[str] = Field(None, description="Номер телефона склада.")
    created_at: Optional[datetime.datetime] = Field(None, description="Дата и время создания склада.")
    updated_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время последнего обновления данных склада."
    )
    pause_at: Optional[datetime.datetime] = Field(
        None, description="Дата, когда продавец поставил склад на паузу."
    )
    cut_in_time: Optional[int] = Field(None, description="Время на отгрузку в минутах.")
    sla_cut_in: Optional[int] = Field(
        None, description="Минимальное время на сборку заказа в минутах."
    )
    has_entrusted_acceptance: Optional[bool] = Field(
        None, description="Признак подключения доверительной приёмки."
    )
    has_postings_limit: Optional[bool] = Field(
        None, description="Признак наличия лимита минимального количества заказов."
    )
    min_postings_limit: Optional[int] = Field(
        None, description="Минимальное количество заказов, которое можно привезти в одной поставке."
    )
    postings_limit: Optional[int] = Field(None, description="Лимит заказов. -1, если лимита нет.")
    is_auto_assembly: Optional[bool] = Field(None, description="Признак включённой автосборки.")
    is_comfort: Optional[bool] = Field(None, description="Признак доставки comfort.")
    is_express: Optional[bool] = Field(None, description="Признак доставки express.")
    is_kgt: Optional[bool] = Field(
        None, description="Признак, что склад принимает крупногабаритные товары."
    )
    is_rfbs: Optional[bool] = Field(None, description="Признак работы склада по схеме rFBS.")
    is_waybill_enabled: Optional[bool] = Field(
        None, description="Признак включённой печати транспортной накладной."
    )
    with_item_list: Optional[bool] = Field(
        None, description="Признак включённой печати листа подбора."
    )


class WarehouseListResponse(BaseModel):
    """Описывает схему ответа на запрос списка складов FBS и rFBS (API v2).

    Attributes:
        warehouses: Список складов
        cursor: Указатель для выборки следующих данных
        has_next: Признак, что в ответе вернулась только часть складов
    """
    warehouses: list[WarehouseListItem] = Field(
        default_factory=list, description="Список складов."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак, что в ответе вернулась только часть складов."
    )
