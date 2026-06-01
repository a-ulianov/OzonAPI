"""Общие сущности методов создания и управления FBS-складами (/v1/warehouse/fbs/*)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ....common.enumerations.warehouses import WarehouseFBSPointType


class WarehouseFBSCoordinates(BaseModel):
    """Географические координаты точки.

    Attributes:
        latitude: Широта
        longitude: Долгота
    """
    latitude: Optional[float] = Field(None, description="Широта.")
    longitude: Optional[float] = Field(None, description="Долгота.")


class WarehouseFBSTimeOfDay(BaseModel):
    """Время суток без привязки к дате.

    Attributes:
        hours: Часы
        minutes: Минуты
        nanos: Наносекунды
        seconds: Секунды
    """
    hours: Optional[int] = Field(None, description="Часы.")
    minutes: Optional[int] = Field(None, description="Минуты.")
    nanos: Optional[int] = Field(None, description="Наносекунды.")
    seconds: Optional[int] = Field(None, description="Секунды.")


class WarehouseFBSPointSearch(BaseModel):
    """Параметры поиска drop-off пункта или пункта возврата.

    Attributes:
        address: Адрес для поиска
        types: Типы пунктов для фильтрации
    """
    address: Optional[str] = Field(None, description="Адрес для поиска.")
    types: Optional[list[WarehouseFBSPointType]] = Field(
        None, description="Типы пунктов для фильтрации."
    )


class WarehouseFBSDropOffPoint(BaseModel):
    """Drop-off пункт для создания или изменения склада.

    Attributes:
        address: Адрес пункта
        coordinates: Координаты пункта
        discount_percent: Процент скидки за отгрузку через пункт
        id: Идентификатор пункта
        last_transit_time_local: Время последней отгрузки по местному времени
        type: Тип пункта
    """
    address: Optional[str] = Field(None, description="Адрес пункта.")
    coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты пункта."
    )
    discount_percent: Optional[float] = Field(
        None, description="Процент скидки за отгрузку через пункт."
    )
    id: Optional[str] = Field(None, description="Идентификатор пункта.")
    last_transit_time_local: Optional[WarehouseFBSTimeOfDay] = Field(
        None, description="Время последней отгрузки по местному времени."
    )
    type: Optional[str] = Field(None, description="Тип пункта.")


class WarehouseFBSDropOffTimeslot(BaseModel):
    """Таймслот отгрузки drop-off.

    Attributes:
        acceptance_end_time_local: Окончание приёмки по местному времени
        acceptance_start_time_local: Начало приёмки по местному времени
        from_: Начало таймслота
        id: Идентификатор таймслота
        to_: Окончание таймслота
    """
    model_config = ConfigDict(populate_by_name=True)

    acceptance_end_time_local: Optional[str] = Field(
        None, description="Окончание приёмки по местному времени."
    )
    acceptance_start_time_local: Optional[str] = Field(
        None, description="Начало приёмки по местному времени."
    )
    from_: Optional[str] = Field(None, alias="from", description="Начало таймслота.")
    id: Optional[int] = Field(None, description="Идентификатор таймслота.")
    to_: Optional[str] = Field(None, alias="to", description="Окончание таймслота.")


class WarehouseFBSPickUpTimeslot(BaseModel):
    """Таймслот отгрузки pick-up.

    Attributes:
        from_: Начало таймслота
        id: Идентификатор таймслота
        to_: Окончание таймслота
    """
    model_config = ConfigDict(populate_by_name=True)

    from_: Optional[str] = Field(None, alias="from", description="Начало таймслота.")
    id: Optional[int] = Field(None, description="Идентификатор таймслота.")
    to_: Optional[str] = Field(None, alias="to", description="Окончание таймслота.")


class WarehouseFBSReturnPointWorkingDay(BaseModel):
    """Рабочий день пункта возврата.

    Attributes:
        day: День недели
        from_: Начало рабочего дня
        to_: Окончание рабочего дня
    """
    model_config = ConfigDict(populate_by_name=True)

    day: Optional[str] = Field(None, description="День недели.")
    from_: Optional[str] = Field(None, alias="from", description="Начало рабочего дня.")
    to_: Optional[str] = Field(None, alias="to", description="Окончание рабочего дня.")


class WarehouseFBSReturnPoint(BaseModel):
    """Пункт возврата FBS.

    Attributes:
        address: Адрес пункта возврата
        coordinates: Координаты пункта возврата
        id: Идентификатор пункта возврата
        name: Название пункта возврата
        type: Тип пункта возврата
        utc_offset: Смещение относительно UTC в минутах
        working_days: Рабочие дни пункта возврата
    """
    address: Optional[str] = Field(None, description="Адрес пункта возврата.")
    coordinates: Optional[WarehouseFBSCoordinates] = Field(
        None, description="Координаты пункта возврата."
    )
    id: Optional[int] = Field(None, description="Идентификатор пункта возврата.")
    name: Optional[str] = Field(None, description="Название пункта возврата.")
    type: Optional[str] = Field(None, description="Тип пункта возврата.")
    utc_offset: Optional[int] = Field(
        None, description="Смещение относительно UTC в минутах."
    )
    working_days: Optional[list[WarehouseFBSReturnPointWorkingDay]] = Field(
        None, description="Рабочие дни пункта возврата."
    )


class WarehouseFBSOptions(BaseModel):
    """Дополнительные настройки склада FBS.

    Attributes:
        comment: Комментарий для курьера
        courier_phones: Телефоны для связи с курьером
        is_auto_assembly: Признак включённой автосборки
        is_waybill_enabled: Признак включённой печати транспортной накладной
    """
    comment: Optional[str] = Field(None, description="Комментарий для курьера.")
    courier_phones: Optional[list[str]] = Field(
        None, description="Телефоны для связи с курьером."
    )
    is_auto_assembly: Optional[bool] = Field(
        None, description="Признак включённой автосборки."
    )
    is_waybill_enabled: Optional[bool] = Field(
        None, description="Признак включённой печати транспортной накладной."
    )
