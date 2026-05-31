"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageDeliveryList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import DeliveryListError


class CarriageDeliveryListV1Request(BaseModel):
    """Описывает схему запроса на получение списка методов доставки и отгрузок (v1).

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


class CarriageDeliveryListV1Carriage(BaseModel):
    """Информация об отгрузке в составе метода доставки (v1).

    Attributes:
        id: Идентификатор перевозки
        postings_count: Количество отправлений в перевозке
        quantum_count: Количество квантов в перевозке
        status: Статус перевозки для запрашиваемых метода и даты
    """
    id: Optional[str] = Field(
        None, description="Идентификатор перевозки."
    )
    postings_count: Optional[int] = Field(
        None, description="Количество отправлений в перевозке."
    )
    quantum_count: Optional[int] = Field(
        None, description="Количество квантов в перевозке."
    )
    status: Optional[str] = Field(
        None, description="Статус перевозки для запрашиваемых метода и даты."
    )


class CarriageDeliveryListV1Result(BaseModel):
    """Метод доставки со списком перевозок (v1).

    Attributes:
        assembly_list_availability: Признак доступности листа подбора
        can_create_another_carriage: Признак возможности создать ещё одну перевозку
        carriage_postings_count: Количество отправлений в перевозке
        carriage_quantum_count: Количество квантов в перевозке
        carriages: Список перевозок
        cut_in: Время начала сборки и часовой пояс времени склада
        cutoff_at: Дата и время, до которых нужно собрать отправление
        delivery_method_id: Идентификатор метода доставки
        delivery_method_name: Название метода доставки
        delivery_method_status: Статус метода доставки
        departure_date: Дата отгрузки
        dropoff_address: Адрес точки отгрузки
        dropoff_change_availability: Статус возможности смены точки отгрузки
        dropoff_point_id: Идентификатор точки отгрузки
        dropoff_point_type: Способ отгрузки
        errors: Массив ошибок, которые возникли при обработке запроса
        first_mile_changing: Признак изменения точки отгрузки
        first_mile_type: Тип первой мили
        has_entrusted_acceptance: Признак доверительной приёмки
        integration_type: Тип интеграции со службой доставки
        is_presort: Признак отгрузки с предсортировкой
        is_rfbs: Признак работы склада по схеме rFBS
        mandatory_packaged_count: Количество «обязательных» собранных отправлений
        mandatory_packaged_quantum_count: Количество «обязательных» собранных квантов
        mandatory_postings_count: Количество отправлений, которые нужно собрать
        mandatory_quantum_count: Количество квантов, которые нужно собрать
        optional_packaged_count: Количество собранных «необязательных» отправлений
        postings_for_another_carriage_count: Количество отправлений для следующей перевозки
        quantum_for_another_carriage_count: Количество квантов для следующей перевозки
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
    assembly_list_availability: Optional[bool] = Field(
        None, description="`true`, если доступен лист подбора."
    )
    can_create_another_carriage: Optional[bool] = Field(
        None, description="`true`, если можно создать ещё одну перевозку."
    )
    carriage_postings_count: Optional[int] = Field(
        None, description="Количество отправлений в перевозке."
    )
    carriage_quantum_count: Optional[int] = Field(
        None, description="Количество квантов в перевозке."
    )
    carriages: Optional[list[CarriageDeliveryListV1Carriage]] = Field(
        None, description="Список перевозок."
    )
    cut_in: Optional[str] = Field(
        None, description="Время начала сборки и часовой пояс времени склада."
    )
    cutoff_at: Optional[str] = Field(
        None, description="Дата и время, до которых нужно собрать отправление."
    )
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    delivery_method_name: Optional[str] = Field(
        None, description="Название метода доставки."
    )
    delivery_method_status: Optional[str] = Field(
        None, description="Статус метода доставки."
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
        None, description="Массив ошибок, которые возникли при обработке запроса."
    )
    first_mile_changing: Optional[bool] = Field(
        None, description="`true`, если точка отгрузки изменилась."
    )
    first_mile_type: Optional[str] = Field(
        None, description="Тип первой мили."
    )
    has_entrusted_acceptance: Optional[bool] = Field(
        None, description="`true`, если включена доверительная приёмка."
    )
    integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )
    is_presort: Optional[bool] = Field(
        None, description="`true`, если отгрузка с предсортировкой."
    )
    is_rfbs: Optional[bool] = Field(
        None, description="`true`, если склад работает по схеме rFBS."
    )
    mandatory_packaged_count: Optional[int] = Field(
        None, description="Количество «обязательных» собранных отправлений."
    )
    mandatory_packaged_quantum_count: Optional[int] = Field(
        None, description="Количество «обязательных» собранных квантов."
    )
    mandatory_postings_count: Optional[int] = Field(
        None, description="Количество отправлений, которые нужно собрать."
    )
    mandatory_quantum_count: Optional[int] = Field(
        None, description="Количество квантов, которые нужно собрать."
    )
    optional_packaged_count: Optional[int] = Field(
        None, description="Количество собранных «необязательных» отправлений."
    )
    postings_for_another_carriage_count: Optional[int] = Field(
        None, description="Количество отправлений, которые могут попасть в следующую перевозку."
    )
    quantum_for_another_carriage_count: Optional[int] = Field(
        None, description="Количество квантов, которые могут попасть в следующую перевозку."
    )
    recommended_time_local: Optional[str] = Field(
        None, description="Рекомендуемое местное время отгрузки в пункт приёма заказов."
    )
    recommended_time_utc_offset_in_minutes: Optional[float] = Field(
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


class CarriageDeliveryListV1Response(BaseModel):
    """Описывает схему ответа на запрос списка методов доставки и отгрузок (v1).

    Attributes:
        result: Список методов доставки с перевозками
    """
    result: Optional[list[CarriageDeliveryListV1Result]] = Field(
        None, description="Список методов доставки с перевозками."
    )
