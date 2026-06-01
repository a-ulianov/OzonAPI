"""Схемы метода warehouse_list (список складов FBS и rFBS, v1)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class WarehouseListV1RequestWith(BaseModel):
    """Дополнительные поля в ответе списка складов (v1).

    Attributes:
        able_to_set_price: Добавить признак возможности установки цены
    """
    able_to_set_price: Optional[bool] = Field(
        None, description="Добавить признак возможности установки цены."
    )


class WarehouseListV1Request(BaseModel):
    """Параметры запроса списка складов (v1).

    Attributes:
        limit: Количество значений в ответе
        offset: Смещение выборки
        with_: Дополнительные поля в ответе
    """
    model_config = ConfigDict(populate_by_name=True)

    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    offset: Optional[int] = Field(None, description="Смещение выборки.")
    with_: Optional[WarehouseListV1RequestWith] = Field(
        None, alias="with", description="Дополнительные поля в ответе."
    )


class WarehouseListV1FirstMile(BaseModel):
    """Первая миля склада (v1).

    Attributes:
        dropoff_point_id: Идентификатор точки drop-off
        dropoff_timeslot_id: Идентификатор интервала drop-off
        first_mile_is_changing: Первая миля в процессе изменения
        first_mile_type: Тип первой мили
    """
    dropoff_point_id: Optional[str] = Field(
        None, description="Идентификатор точки drop-off."
    )
    dropoff_timeslot_id: Optional[int] = Field(
        None, description="Идентификатор интервала drop-off."
    )
    first_mile_is_changing: Optional[bool] = Field(
        None, description="Первая миля в процессе изменения."
    )
    first_mile_type: Optional[str] = Field(None, description="Тип первой мили.")


class WarehouseListV1Item(BaseModel):
    """Склад FBS или rFBS (v1).

    Attributes:
        has_entrusted_acceptance: Доверительная приёмка
        is_rfbs: Признак склада rFBS
        name: Название склада
        warehouse_id: Идентификатор склада
        can_print_act_in_advance: Можно ли печатать акт заранее
        first_mile_type: Первая миля склада
        has_postings_limit: Установлен ли лимит отправлений
        is_karantin: Склад на карантине
        is_kgt: Приём крупногабаритных товаров
        is_economy: Эконом-склад
        is_able_to_set_price: Можно ли устанавливать цену
        is_presorted: Склад с предсортировкой
        is_timetable_editable: Можно ли редактировать расписание
        min_postings_limit: Минимальный лимит отправлений
        postings_limit: Лимит отправлений
        min_working_days: Минимальное число рабочих дней
        status: Статус склада
        working_days: Рабочие дни склада
    """
    has_entrusted_acceptance: Optional[bool] = Field(
        None, description="Доверительная приёмка."
    )
    is_rfbs: Optional[bool] = Field(None, description="Признак склада rFBS.")
    name: Optional[str] = Field(None, description="Название склада.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    can_print_act_in_advance: Optional[bool] = Field(
        None, description="Можно ли печатать акт заранее."
    )
    first_mile_type: Optional[WarehouseListV1FirstMile] = Field(
        None, description="Первая миля склада."
    )
    has_postings_limit: Optional[bool] = Field(
        None, description="Установлен ли лимит отправлений."
    )
    is_karantin: Optional[bool] = Field(None, description="Склад на карантине.")
    is_kgt: Optional[bool] = Field(
        None, description="Приём крупногабаритных товаров."
    )
    is_economy: Optional[bool] = Field(None, description="Эконом-склад.")
    is_able_to_set_price: Optional[bool] = Field(
        None, description="Можно ли устанавливать цену."
    )
    is_presorted: Optional[bool] = Field(
        None, description="Склад с предсортировкой."
    )
    is_timetable_editable: Optional[bool] = Field(
        None, description="Можно ли редактировать расписание."
    )
    min_postings_limit: Optional[int] = Field(
        None, description="Минимальный лимит отправлений."
    )
    postings_limit: Optional[int] = Field(None, description="Лимит отправлений.")
    min_working_days: Optional[int] = Field(
        None, description="Минимальное число рабочих дней."
    )
    status: Optional[str] = Field(None, description="Статус склада.")
    working_days: Optional[list[str]] = Field(
        None, description="Рабочие дни склада."
    )


class WarehouseListV1Response(BaseModel):
    """Ответ со списком складов (v1).

    Attributes:
        result: Список складов
    """
    result: Optional[list[WarehouseListV1Item]] = Field(
        None, description="Список складов."
    )
