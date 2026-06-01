"""Схемы метода delivery_point_info (информация о точке самовывоза, v1)."""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .entities import DeliveryLatLong


class DeliveryPointInfoRequest(BaseModel):
    """Параметры запроса информации о точках самовывоза.

    Attributes:
        map_point_ids: Идентификаторы точек на карте
    """
    map_point_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы точек на карте."
    )


class DeliveryPointAddressDetails(BaseModel):
    """Детали адреса точки самовывоза.

    Attributes:
        city: Город
        house: Дом
        region: Регион
        street: Улица
    """
    city: Optional[str] = Field(None, description="Город.")
    house: Optional[str] = Field(None, description="Дом.")
    region: Optional[str] = Field(None, description="Регион.")
    street: Optional[str] = Field(None, description="Улица.")


class DeliveryPointDeliveryType(BaseModel):
    """Тип доставки точки самовывоза.

    Attributes:
        id: Идентификатор типа доставки
        name: Название типа доставки
    """
    id: Optional[int] = Field(None, description="Идентификатор типа доставки.")
    name: Optional[str] = Field(None, description="Название типа доставки.")


class DeliveryPointHolidays(BaseModel):
    """Период нерабочих дней точки самовывоза.

    Attributes:
        begin: Начало периода
        end: Конец периода
    """
    begin: Optional[datetime.datetime] = Field(None, description="Начало периода.")
    end: Optional[datetime.datetime] = Field(None, description="Конец периода.")


class DeliveryPointProperty(BaseModel):
    """Свойство точки самовывоза.

    Attributes:
        enabled: Признак включённости свойства
        name: Название свойства
    """
    enabled: Optional[bool] = Field(None, description="Признак включённости свойства.")
    name: Optional[str] = Field(None, description="Название свойства.")


class DeliveryPointWorkingHoursPeriodTime(BaseModel):
    """Время в часах и минутах.

    Attributes:
        hours: Часы
        minutes: Минуты
    """
    hours: Optional[int] = Field(None, description="Часы.")
    minutes: Optional[int] = Field(None, description="Минуты.")


class DeliveryPointWorkingHoursPeriod(BaseModel):
    """Интервал рабочего времени.

    Attributes:
        max: Время окончания интервала
        min: Время начала интервала
    """
    max: Optional[DeliveryPointWorkingHoursPeriodTime] = Field(
        None, description="Время окончания интервала."
    )
    min: Optional[DeliveryPointWorkingHoursPeriodTime] = Field(
        None, description="Время начала интервала."
    )


class DeliveryPointWorkingHours(BaseModel):
    """Рабочие часы точки самовывоза на дату.

    Attributes:
        date: Дата
        periods: Интервалы рабочего времени
    """
    date: Optional[datetime.datetime] = Field(None, description="Дата.")
    periods: Optional[list[DeliveryPointWorkingHoursPeriod]] = Field(
        None, description="Интервалы рабочего времени."
    )


class DeliveryPointInfoDeliveryMethod(BaseModel):
    """Информация о точке самовывоза.

    Attributes:
        address: Адрес точки
        address_details: Детали адреса
        coordinates: Координаты точки
        delivery_type: Тип доставки
        description: Описание точки
        fitting_rooms_count: Количество примерочных
        holidays: Нерабочие дни
        holidays_filled: Признак, что нерабочие дни заполнены
        images: Изображения точки
        location_id: Идентификатор местоположения
        map_point_id: Идентификатор точки на карте
        name: Название точки
        properties: Свойства точки
        pvz_rating: Рейтинг пункта выдачи
        storage_period: Срок хранения в днях
        working_hours: Рабочие часы
    """
    address: Optional[str] = Field(None, description="Адрес точки.")
    address_details: Optional[DeliveryPointAddressDetails] = Field(
        None, description="Детали адреса."
    )
    coordinates: Optional[DeliveryLatLong] = Field(None, description="Координаты точки.")
    delivery_type: Optional[DeliveryPointDeliveryType] = Field(
        None, description="Тип доставки."
    )
    description: Optional[str] = Field(None, description="Описание точки.")
    fitting_rooms_count: Optional[int] = Field(
        None, description="Количество примерочных."
    )
    holidays: Optional[list[DeliveryPointHolidays]] = Field(
        None, description="Нерабочие дни."
    )
    holidays_filled: Optional[bool] = Field(
        None, description="Признак, что нерабочие дни заполнены."
    )
    images: Optional[list[str]] = Field(None, description="Изображения точки.")
    location_id: Optional[str] = Field(
        None, description="Идентификатор местоположения."
    )
    map_point_id: Optional[int] = Field(
        None, description="Идентификатор точки на карте."
    )
    name: Optional[str] = Field(None, description="Название точки.")
    properties: Optional[list[DeliveryPointProperty]] = Field(
        None, description="Свойства точки."
    )
    pvz_rating: Optional[int] = Field(None, description="Рейтинг пункта выдачи.")
    storage_period: Optional[int] = Field(None, description="Срок хранения в днях.")
    working_hours: Optional[list[DeliveryPointWorkingHours]] = Field(
        None, description="Рабочие часы."
    )


class DeliveryPointInfoItem(BaseModel):
    """Точка самовывоза с информацией о методе доставки.

    Attributes:
        delivery_method: Информация о точке самовывоза
        enabled: Признак доступности точки
    """
    delivery_method: Optional[DeliveryPointInfoDeliveryMethod] = Field(
        None, description="Информация о точке самовывоза."
    )
    enabled: Optional[bool] = Field(None, description="Признак доступности точки.")


class DeliveryPointInfoResponse(BaseModel):
    """Ответ с информацией о точках самовывоза.

    Attributes:
        points: Список точек самовывоза
    """
    points: Optional[list[DeliveryPointInfoItem]] = Field(
        None, description="Список точек самовывоза."
    )
