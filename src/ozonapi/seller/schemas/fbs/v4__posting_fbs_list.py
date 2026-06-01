"""Схемы метода posting_fbs_list (список отправлений FBS, v4)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .entities.posting__v4_posting import PostingFBSV4Postings


class PostingFBSListLastChangedStatusDate(BaseModel):
    """Период последнего изменения статуса отправлений.

    Attributes:
        from_: Начало периода
        to_: Конец периода
    """
    model_config = ConfigDict(populate_by_name=True)

    from_: Optional[str] = Field(None, alias="from", description="Начало периода.")
    to_: Optional[str] = Field(None, alias="to", description="Конец периода.")


class PostingFBSListFilter(BaseModel):
    """Фильтр списка отправлений FBS.

    Attributes:
        delivery_method_ids: Идентификаторы методов доставки
        is_blr_traceable: Только товары, подлежащие прослеживаемости
        last_changed_status_date: Период последнего изменения статуса
        order_id: Идентификатор заказа
        order_numbers: Номера заказов
        provider_ids: Идентификаторы служб доставки
        since: Начало периода создания отправлений
        statuses: Статусы отправлений
        to: Конец периода создания отправлений
        warehouse_ids: Идентификаторы складов
    """
    delivery_method_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы методов доставки."
    )
    is_blr_traceable: Optional[bool] = Field(
        None, description="Только товары, подлежащие прослеживаемости."
    )
    last_changed_status_date: Optional[PostingFBSListLastChangedStatusDate] = Field(
        None, description="Период последнего изменения статуса."
    )
    order_id: Optional[int] = Field(None, description="Идентификатор заказа.")
    order_numbers: Optional[list[str]] = Field(None, description="Номера заказов.")
    provider_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы служб доставки."
    )
    since: Optional[str] = Field(
        None, description="Начало периода создания отправлений."
    )
    statuses: Optional[list[str]] = Field(None, description="Статусы отправлений.")
    to: Optional[str] = Field(
        None, description="Конец периода создания отправлений."
    )
    warehouse_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы складов."
    )


class PostingFBSListWith(BaseModel):
    """Дополнительные поля в ответе списка отправлений FBS.

    Attributes:
        analytics_data: Добавить данные аналитики
        barcodes: Добавить штрихкоды отправления
        financial_data: Добавить финансовые данные
        legal_info: Добавить юридическую информацию
    """
    analytics_data: Optional[bool] = Field(
        None, description="Добавить данные аналитики."
    )
    barcodes: Optional[bool] = Field(
        None, description="Добавить штрихкоды отправления."
    )
    financial_data: Optional[bool] = Field(
        None, description="Добавить финансовые данные."
    )
    legal_info: Optional[bool] = Field(
        None, description="Добавить юридическую информацию."
    )


class PostingFBSListRequest(BaseModel):
    """Параметры запроса списка отправлений FBS (v4).

    Attributes:
        cursor: Указатель для следующей выборки
        filter: Фильтр списка отправлений
        limit: Количество значений в ответе
        sort_dir: Направление сортировки
        translit: Транслитерировать значения в ответе
        with_: Дополнительные поля в ответе
    """
    model_config = ConfigDict(populate_by_name=True)

    cursor: Optional[str] = Field(
        None, description="Указатель для следующей выборки."
    )
    filter: Optional[PostingFBSListFilter] = Field(
        None, description="Фильтр списка отправлений."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    sort_dir: Optional[str] = Field(None, description="Направление сортировки.")
    translit: Optional[bool] = Field(
        None, description="Транслитерировать значения в ответе."
    )
    with_: Optional[PostingFBSListWith] = Field(
        None, alias="with", description="Дополнительные поля в ответе."
    )


class PostingFBSListResponse(BaseModel):
    """Ответ со списком отправлений FBS (v4).

    Attributes:
        cursor: Указатель для следующей выборки
        has_next: Признак наличия следующей страницы
        postings: Список отправлений
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для следующей выборки."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    postings: Optional[list[PostingFBSV4Postings]] = Field(
        None, description="Список отправлений."
    )
