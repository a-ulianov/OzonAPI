"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageDeliveryListV2"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import DeliveryListError


class CarriageDeliveryListFilter(BaseModel):
    """Фильтр для получения списка методов доставки и отгрузок.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        departure_date: Дата отгрузки (по умолчанию — текущая дата)
    """
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата отгрузки. По умолчанию — текущая дата."
    )


class CarriageDeliveryListRequest(BaseModel):
    """Описывает схему запроса на получение списка методов доставки и отгрузок.

    Attributes:
        limit: Количество значений на странице
        cursor: Указатель для выборки следующих данных
        filter: Фильтр для поиска методов доставки
    """
    limit: int = Field(
        ..., description="Количество значений на странице."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: Optional[CarriageDeliveryListFilter] = Field(
        None, description="Фильтр для поиска методов доставки."
    )


class CarriageDeliveryListPickupFee(BaseModel):
    """Предварительная стоимость отгрузки курьеру Ozon.

    Attributes:
        currency_code: Код валюты
        value: Предварительная стоимость отгрузки курьеру Ozon
    """
    currency_code: Optional[str] = Field(
        None, description="Код валюты."
    )
    value: Optional[float] = Field(
        None, description="Предварительная стоимость отгрузки курьеру Ozon."
    )


class CarriageDeliveryListCarriage(BaseModel):
    """Информация об отгрузке в составе метода доставки.

    Attributes:
        id: Идентификатор отгрузки (если `0` — отгрузку можно создать)
        status: Статус отгрузки для запрашиваемых метода и даты
        all_blr_traceable: Признак наличия товаров, требующих доп. оформления
        available_actions: Доступные действия с отгрузкой
        carriage_volume: Объём отгрузки в литрах
        pickup_fee: Предварительная стоимость отгрузки курьеру Ozon
        postings_count: Количество отправлений в отгрузке
        quantum_count: Количество квантов в отгрузке
    """
    id: Optional[int] = Field(
        None, description="Идентификатор отгрузки. Если `0` — отгрузку можно создать."
    )
    status: Optional[str] = Field(
        None, description="Статус отгрузки для запрашиваемых метода и даты."
    )
    all_blr_traceable: Optional[bool] = Field(
        None, description="`true`, если в отгрузке есть товары, для которых нужно доп. оформление."
    )
    available_actions: Optional[list[str]] = Field(
        None, description="Доступные действия с отгрузкой."
    )
    carriage_volume: Optional[float] = Field(
        None, description="Объём отгрузки в литрах."
    )
    pickup_fee: Optional[CarriageDeliveryListPickupFee] = Field(
        None, description="Предварительная стоимость отгрузки курьеру Ozon."
    )
    postings_count: Optional[int] = Field(
        None, description="Количество отправлений в отгрузке."
    )
    quantum_count: Optional[int] = Field(
        None, description="Количество квантов в отгрузке."
    )


class CarriageDeliveryListMethod(BaseModel):
    """Метод доставки со списком отгрузок.

    Attributes:
        delivery_method_id: Идентификатор метода доставки
        delivery_method_name: Название метода доставки
        delivery_method_status: Статус метода доставки
        carriages: Список отгрузок
        carriage_postings_count: Количество отправлений во всех отгрузках
        cut_in: Время начала сборки и часовой пояс времени склада
        cutoff_at: Дата и время, до которых нужно собрать отправление
        departure_date: Дата отгрузки
        dropoff_address: Адрес точки отгрузки
        dropoff_change_availability: Статус возможности смены точки отгрузки
        dropoff_point_id: Идентификатор точки отгрузки
        dropoff_point_type: Способ отгрузки
        errors: Список ошибок, которые возникли при обработке запроса
        first_mile_changing: Признак изменения точки отгрузки
        first_mile_type: Тип первой мили
        has_entrusted_acceptance: Признак включённой доверительной приёмки
        integration_type: Тип интеграции со службой доставки
        is_optional_carriage: Признак необязательной отгрузки
        is_presort: Признак отгрузки с предсортировкой
        is_rfbs: Признак работы склада по схеме rFBS
        mandatory_packaged_count: Количество собранных обязательных отправлений
        mandatory_postings_count: Количество отправлений, которые нужно собрать
        optional_packaged_count: Количество собранных необязательных отправлений
        recommended_time_local: Рекомендуемое местное время отгрузки
        recommended_time_utc_offset_in_minutes: Смещение часового пояса от UTC-0
        timeslot_from: Начало таймслота в точке отгрузки
        timeslot_to: Окончание таймслота в точке отгрузки
        tpl_provider_icon_url: Ссылка на иконку службы доставки
        tpl_provider_name: Название службы доставки
        warehouse_city: Город склада
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    delivery_method_name: Optional[str] = Field(
        None, description="Название метода доставки."
    )
    delivery_method_status: Optional[str] = Field(
        None, description="Статус метода доставки."
    )
    carriages: Optional[list[CarriageDeliveryListCarriage]] = Field(
        None, description="Список отгрузок."
    )
    carriage_postings_count: Optional[int] = Field(
        None, description="Количество отправлений во всех отгрузках."
    )
    cut_in: Optional[str] = Field(
        None, description="Время начала сборки и часовой пояс времени склада."
    )
    cutoff_at: Optional[str] = Field(
        None, description="Дата и время, до которых нужно собрать отправление."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата отгрузки."
    )
    dropoff_address: Optional[str] = Field(
        None, description="Адрес точки отгрузки."
    )
    dropoff_change_availability: Optional[str] = Field(
        None, description="Статус возможности смены точки отгрузки."
    )
    dropoff_point_id: Optional[int] = Field(
        None, description="Идентификатор точки отгрузки."
    )
    dropoff_point_type: Optional[str] = Field(
        None, description="Способ отгрузки."
    )
    errors: Optional[list[DeliveryListError]] = Field(
        None, description="Список ошибок, которые возникли при обработке запроса."
    )
    first_mile_changing: Optional[bool] = Field(
        None, description="`true`, если точка отгрузки изменилась."
    )
    first_mile_type: Optional[str] = Field(
        None, description="Тип первой мили."
    )
    has_entrusted_acceptance: Optional[bool] = Field(
        None, description="`true`, если на складе включена доверительная приёмка."
    )
    integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )
    is_optional_carriage: Optional[bool] = Field(
        None, description="`true`, если отгрузка не обязательна."
    )
    is_presort: Optional[bool] = Field(
        None, description="`true`, если отгрузка с предсортировкой."
    )
    is_rfbs: Optional[bool] = Field(
        None, description="`true`, если склад работает по схеме rFBS."
    )
    mandatory_packaged_count: Optional[int] = Field(
        None, description="Количество собранных обязательных отправлений."
    )
    mandatory_postings_count: Optional[int] = Field(
        None, description="Количество отправлений, которые нужно собрать."
    )
    optional_packaged_count: Optional[int] = Field(
        None, description="Количество собранных необязательных отправлений."
    )
    recommended_time_local: Optional[str] = Field(
        None, description="Рекомендуемое местное время отгрузки в пункт приёма заказов."
    )
    recommended_time_utc_offset_in_minutes: Optional[int] = Field(
        None, description="Смещение часового пояса рекомендуемого времени отгрузки от UTC-0."
    )
    timeslot_from: Optional[str] = Field(
        None, description="Начало таймслота в точке отгрузки."
    )
    timeslot_to: Optional[str] = Field(
        None, description="Окончание таймслота в точке отгрузки."
    )
    tpl_provider_icon_url: Optional[str] = Field(
        None, description="Ссылка на иконку службы доставки."
    )
    tpl_provider_name: Optional[str] = Field(
        None, description="Название службы доставки."
    )
    warehouse_city: Optional[str] = Field(
        None, description="Город склада."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )
    warehouse_name: Optional[str] = Field(
        None, description="Название склада."
    )


class CarriageDeliveryListResponse(BaseModel):
    """Описывает схему ответа на запрос списка методов доставки и отгрузок.

    Attributes:
        methods: Список методов доставки
        cursor: Указатель для выборки следующих данных
        has_next: Признак наличия следующей страницы
    """
    methods: Optional[list[CarriageDeliveryListMethod]] = Field(
        None, description="Список методов доставки."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="`true`, если в ответе вернулись не все методы доставки."
    )
