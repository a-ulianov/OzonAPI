"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetCarriageAvailableList"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingCarriageAvailableListRequest(BaseModel):
    """Описывает схему запроса на получение списка доступных перевозок.

    Attributes:
        delivery_method_id: Фильтр по методу доставки
        departure_date: Дата отгрузки (по умолчанию — текущая дата)
    """
    delivery_method_id: int = Field(
        ..., description="Фильтр по методу доставки."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата отгрузки. По умолчанию — текущая дата."
    )


class PostingCarriageAvailableListError(BaseModel):
    """Ошибка в составе доступной перевозки.

    Attributes:
        code: Код ошибки
        status: Тип ошибки (`warning` — предупреждение, `critical` — критическая)
    """
    code: Optional[str] = Field(
        None, description="Код ошибки."
    )
    status: Optional[str] = Field(
        None, description="Тип ошибки: `warning` — предупреждение, `critical` — критическая."
    )


class PostingCarriageAvailableListResult(BaseModel):
    """Доступная перевозка.

    Attributes:
        carriage_id: Идентификатор перевозки (также номер задания на формирование)
        carriage_postings_count: Количество отправлений в перевозке
        carriage_status: Статус перевозки для метода доставки и даты отгрузки
        cutoff_at: Дата и время, до которых нужно собрать отправление
        delivery_method_id: Идентификатор метода доставки
        delivery_method_name: Название метода доставки
        errors: Список ошибок
        first_mile_type: Тип первой мили
        has_entrusted_acceptance: Признак доверительной приёмки
        mandatory_postings_count: Количество отправлений, которые нужно собрать
        mandatory_packaged_count: Количество собранных отправлений
        recommended_time_local: Рекомендуемое местное время отгрузки
        recommended_time_utc_offset_in_minutes: Смещение часового пояса от UTC-0
        tpl_provider_icon_url: Ссылка на иконку службы доставки
        tpl_provider_name: Название службы доставки
        warehouse_city: Город склада
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
        warehouse_timezone: Часовой пояс, в котором находится склад
    """
    carriage_id: Optional[int] = Field(
        None, description="Идентификатор перевозки (также номер задания на формирование)."
    )
    carriage_postings_count: Optional[int] = Field(
        None, description="Количество отправлений в перевозке."
    )
    carriage_status: Optional[str] = Field(
        None, description="Статус перевозки для запрашиваемого метода доставки и даты отгрузки."
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
    errors: Optional[list[PostingCarriageAvailableListError]] = Field(
        None, description="Список ошибок."
    )
    first_mile_type: Optional[str] = Field(
        None, description="Тип первой мили."
    )
    has_entrusted_acceptance: Optional[bool] = Field(
        None, description="Признак доверительной приёмки. `true`, если доверительная приёмка включена."
    )
    mandatory_postings_count: Optional[int] = Field(
        None, description="Количество отправлений, которые нужно собрать."
    )
    mandatory_packaged_count: Optional[int] = Field(
        None, description="Количество собранных отправлений."
    )
    recommended_time_local: Optional[str] = Field(
        None, description="Рекомендуемое местное время отгрузки на пункт приёма заказов."
    )
    recommended_time_utc_offset_in_minutes: Optional[float] = Field(
        None, description="Смещение часового пояса рекомендуемого времени отгрузки от UTC-0."
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
    warehouse_timezone: Optional[str] = Field(
        None, description="Часовой пояс, в котором находится склад."
    )


class PostingCarriageAvailableListResponse(BaseModel):
    """Описывает схему ответа на запрос списка доступных перевозок.

    Attributes:
        result: Список доступных перевозок
    """
    result: Optional[list[PostingCarriageAvailableListResult]] = Field(
        None, description="Список доступных перевозок."
    )
