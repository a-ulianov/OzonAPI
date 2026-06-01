"""Схемы метода posting_fbs_unfulfilled_list (необработанные отправления, v4)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .entities.posting__v4_posting import PostingFBSV4Postings
from .v4__posting_fbs_list import (
    PostingFBSListLastChangedStatusDate,
    PostingFBSListWith,
)


class PostingFBSUnfulfilledListFilter(BaseModel):
    """Фильтр списка необработанных отправлений FBS.

    Attributes:
        cutoff_from: Начало периода сборки
        cutoff_to: Конец периода сборки
        delivering_date_from: Начало периода доставки
        delivering_date_to: Конец периода доставки
        delivery_method_ids: Идентификаторы методов доставки
        last_changed_status_date: Период последнего изменения статуса
        provider_ids: Идентификаторы служб доставки
        statuses: Статусы отправлений
        warehouse_ids: Идентификаторы складов
    """
    cutoff_from: Optional[str] = Field(None, description="Начало периода сборки.")
    cutoff_to: Optional[str] = Field(None, description="Конец периода сборки.")
    delivering_date_from: Optional[str] = Field(
        None, description="Начало периода доставки."
    )
    delivering_date_to: Optional[str] = Field(
        None, description="Конец периода доставки."
    )
    delivery_method_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы методов доставки."
    )
    last_changed_status_date: Optional[PostingFBSListLastChangedStatusDate] = Field(
        None, description="Период последнего изменения статуса."
    )
    provider_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы служб доставки."
    )
    statuses: Optional[list[str]] = Field(None, description="Статусы отправлений.")
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )


class PostingFBSUnfulfilledListRequest(BaseModel):
    """Параметры запроса списка необработанных отправлений FBS (v4).

    Attributes:
        cursor: Указатель для следующей выборки
        filter: Фильтр списка необработанных отправлений
        limit: Количество значений в ответе
        sort_dir: Направление сортировки
        translit: Транслитерировать значения в ответе
        with_: Дополнительные поля в ответе
    """
    model_config = ConfigDict(populate_by_name=True)

    cursor: Optional[str] = Field(
        None, description="Указатель для следующей выборки."
    )
    filter: Optional[PostingFBSUnfulfilledListFilter] = Field(
        None, description="Фильтр списка необработанных отправлений."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    sort_dir: Optional[str] = Field(None, description="Направление сортировки.")
    translit: Optional[bool] = Field(
        None, description="Транслитерировать значения в ответе."
    )
    with_: Optional[PostingFBSListWith] = Field(
        None, alias="with", description="Дополнительные поля в ответе."
    )


class PostingFBSUnfulfilledListResponse(BaseModel):
    """Ответ со списком необработанных отправлений FBS (v4).

    Attributes:
        count: Количество необработанных отправлений
        cursor: Указатель для следующей выборки
        has_next: Признак наличия следующей страницы
        postings: Список отправлений
    """
    count: Optional[int] = Field(
        None, description="Количество необработанных отправлений."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для следующей выборки."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    postings: Optional[list[PostingFBSV4Postings]] = Field(
        None, description="Список отправлений."
    )
