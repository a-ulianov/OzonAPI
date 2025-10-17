"""https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_WarehouseList"""
from pydantic import BaseModel, Field

from ...common.enumerations.warehouses import FirstMileType, WarehouseStatus, WarehouseWorkingDays


class WarehouseListFirstMileType(BaseModel):
    """Первая миля FBS.

    Attributes:
        dropoff_point_id: Идентификатор DropOff-точки
        dropoff_timeslot_id: Идентификатор временного слота для DropOff
        first_mile_is_changing: Признак обновления настроек склада
        first_mile_type: Тип первой мили
    """
    dropoff_point_id: str = Field(
        ..., description="Идентификатор DropOff-точки."
    )
    dropoff_timeslot_id: int = Field(
        ..., description="Идентификатор временного слота для DropOff."
    )
    first_mile_is_changing: bool = Field(
        ..., description="Признак, что настройки склада обновляются."
    )
    first_mile_type: FirstMileType = Field(
        ..., description="Тип первой мили."
    )


class WarehouseListItem(BaseModel):
    """Информация о складе.

    Attributes:
        has_entrusted_acceptance: Признак доверительной приёмки
        is_rfbs: Признак работы склада по схеме rFBS
        name: Название склада
        warehouse_id: Идентификатор склада
        can_print_act_in_advance: Возможность печати акта приёма-передачи заранее
        first_mile_type: Первая миля FBS
        has_postings_limit: Признак наличия лимита минимального количества заказов
        is_karantin: Признак карантина склада
        is_kgt: Признак приёма крупногабаритных товаров
        is_economy: Признак работы с эконом-товарами
        is_timetable_editable: Признак возможности изменения расписания
        min_postings_limit: Минимальное значение лимита заказов
        postings_limit: Значение лимита заказов
        min_working_days: Количество рабочих дней склада
        status: Статус склада
        working_days: Рабочие дни склада
    """
    has_entrusted_acceptance: bool = Field(
        ..., description="Признак доверительной приёмки. true, если доверительная приёмка включена на складе."
    )
    is_rfbs: bool = Field(
        ..., description="Признак работы склада по схеме rFBS."
    )
    name: str = Field(
        ..., description="Название склада."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )
    can_print_act_in_advance: bool = Field(
        ..., description="Возможность печати акта приёма-передачи заранее. true, если печатать заранее возможно."
    )
    first_mile_type: WarehouseListFirstMileType = Field(
        ..., description="Первая миля FBS."
    )
    has_postings_limit: bool = Field(
        ..., description="Признак наличия лимита минимального количества заказов. true, если лимит есть."
    )
    is_karantin: bool = Field(
        ..., description="Признак, что склад не работает из-за карантина."
    )
    is_kgt: bool = Field(
        ..., description="Признак, что склад принимает крупногабаритные товары."
    )
    is_economy: bool = Field(
        ..., description="true, если склад работает с эконом-товарами."
    )
    is_timetable_editable: bool = Field(
        ..., description="Признак, что можно менять расписание работы складов."
    )
    min_postings_limit: int = Field(
        ..., description="Минимальное значение лимита — количество заказов, которые можно привезти в одной поставке."
    )
    postings_limit: int = Field(
        ..., description="Значение лимита. -1, если лимита нет."
    )
    min_working_days: int = Field(
        ..., description="Количество рабочих дней склада."
    )
    status: WarehouseStatus = Field(
        ..., description="Статус склада."
    )
    working_days: list[WarehouseWorkingDays] = Field(
        ..., description="Рабочие дни склада."
    )


class WarehouseListResponse(BaseModel):
    """Схема, описывающая ответ сервера на запрос списка складов FBS и rFBS.

    Attributes:
        result: Список складов
    """
    result: list[WarehouseListItem] = Field(
        default_factory=list, description="Список складов."
    )