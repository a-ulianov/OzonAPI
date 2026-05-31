"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageGet"""
from typing import Optional, Union

from pydantic import BaseModel, Field


class CarriageGetCancelAvailability(BaseModel):
    """Информация о возможности отмены перевозки.

    Attributes:
        is_cancel_available: Признак возможности отмены перевозки
        reason: Причина, почему перевозку нельзя отменить
    """
    is_cancel_available: Optional[bool] = Field(
        None, description="`true`, если перевозку можно отменить."
    )
    reason: Optional[str] = Field(
        None, description="Причина, почему перевозку нельзя отменить."
    )


class CarriageGetRequest(BaseModel):
    """Описывает схему запроса на получение информации о перевозке.

    Attributes:
        carriage_id: Идентификатор перевозки
    """
    carriage_id: int = Field(
        ..., description="Идентификатор перевозки."
    )


class CarriageGetResponse(BaseModel):
    """Описывает схему ответа на запрос информации о перевозке.

    Attributes:
        carriage_id: Идентификатор перевозки
        act_type: Тип акта приёма-передачи (актуально для продавцов FBS)
        available_actions: Доступные действия с перевозкой
        arrival_pass_ids: Список идентификаторов пропусков, оформленных на перевозку
        cancel_availability: Информация о возможности отмены перевозки
        company_id: Идентификатор продавца
        containers_count: Количество грузовых мест
        created_at: Дата создания перевозки
        delivery_method_id: Идентификатор метода доставки
        departure_date: Дата выполнения перевозки
        first_mile_type: Тип первой мили
        has_postings_for_next_carriage: Признак наличия отправлений для следующей перевозки
        integration_type: Тип перевозки
        is_container_label_printed: Признак печати этикеток на грузовые места
        is_econom: Признак отгрузки товаров «Суперэконом»
        is_partial: Признак частичной перевозки
        is_waybill_enabled: Признак доступности печати транспортной накладной
        all_blr_traceable: Признак отгрузки с прослеживаемыми товарами
        partial_num: Порядковый номер частичной перевозки
        retry_count: Количество повторных попыток создания перевозки
        status: Статус перевозки
        tpl_provider_id: Идентификатор провайдера доставки
        updated_at: Дата последнего обновления информации о перевозке
        warehouse_id: Идентификатор склада
    """
    carriage_id: Optional[int] = Field(
        None, description="Идентификатор перевозки."
    )
    act_type: Optional[str] = Field(
        None, description="Тип акта приёма-передачи. Актуально для продавцов FBS."
    )
    available_actions: Optional[list[str]] = Field(
        None, description="Доступные действия с перевозкой."
    )
    arrival_pass_ids: Optional[list[Union[int, str]]] = Field(
        None, description="Список идентификаторов пропусков, оформленных на перевозку."
    )
    cancel_availability: Optional[CarriageGetCancelAvailability] = Field(
        None, description="Информация о возможности отмены перевозки."
    )
    company_id: Optional[int] = Field(
        None, description="Идентификатор продавца."
    )
    containers_count: Optional[int] = Field(
        None, description="Количество грузовых мест."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания перевозки."
    )
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата выполнения перевозки."
    )
    first_mile_type: Optional[str] = Field(
        None, description="Тип первой мили."
    )
    has_postings_for_next_carriage: Optional[bool] = Field(
        None, description="`true`, если есть отправления, которые не попали в перевозку."
    )
    integration_type: Optional[str] = Field(
        None, description="Тип перевозки."
    )
    is_container_label_printed: Optional[bool] = Field(
        None, description="`true`, если вы уже напечатали этикетки на грузовые места."
    )
    is_econom: Optional[bool] = Field(
        None, description="`true`, если отгрузка относится к товарам «Суперэконом»."
    )
    is_partial: Optional[bool] = Field(
        None, description="`true`, если перевозка частичная."
    )
    is_waybill_enabled: Optional[bool] = Field(
        None, description="`true`, если доступна печать транспортной накладной."
    )
    all_blr_traceable: Optional[bool] = Field(
        None, description="`true`, если отгрузка с прослеживаемыми товарами."
    )
    partial_num: Optional[int] = Field(
        None, description="Порядковый номер частичной перевозки."
    )
    retry_count: Optional[int] = Field(
        None, description="Количество повторных попыток создания перевозки."
    )
    status: Optional[str] = Field(
        None, description="Статус перевозки."
    )
    tpl_provider_id: Optional[int] = Field(
        None, description="Идентификатор провайдера доставки."
    )
    updated_at: Optional[str] = Field(
        None, description="Дата последнего обновления информации о перевозке."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )
