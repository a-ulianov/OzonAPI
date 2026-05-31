"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActList"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSActListFilter(BaseModel):
    """Фильтр для получения списка актов по отгрузкам.

    Attributes:
        date_from: Начальная дата создания отгрузок
        date_to: Конечная дата создания отгрузок
        integration_type: Тип интеграции со службой доставки
        status: Статусы перевозок
    """
    date_from: Optional[str] = Field(
        None, description="Начальная дата создания отгрузок."
    )
    date_to: Optional[str] = Field(
        None, description="Конечная дата создания отгрузок."
    )
    integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )
    status: Optional[list[str]] = Field(
        None, description="Статусы перевозок."
    )


class PostingFBSActListRequest(BaseModel):
    """Описывает схему запроса на получение списка актов по отгрузкам.

    Attributes:
        limit: Максимальное количество актов в ответе
        filter: Фильтр для поиска актов
    """
    limit: int = Field(
        ..., description="Максимальное количество актов в ответе."
    )
    filter: Optional[PostingFBSActListFilter] = Field(
        None, description="Фильтр для поиска актов."
    )


class PostingFBSActListRelatedDoc(BaseModel):
    """Информация об одном документе перевозки.

    Attributes:
        created_at: Дата создания акта
        document_status: Статус акта
    """
    created_at: Optional[str] = Field(
        None, description="Дата создания акта."
    )
    document_status: Optional[str] = Field(
        None, description="Статус акта (`FORMING`, `FORMED`, `CONFIRMED`, `ERROR` и т.д.)."
    )


class PostingFBSActListRelatedDocs(BaseModel):
    """Информация про акты перевозки.

    Attributes:
        act_of_acceptance: Информация про акт приёма-передачи
        act_of_mismatch: Информация про акт о расхождениях
        act_of_excess: Информация про акт об излишках
    """
    act_of_acceptance: Optional[PostingFBSActListRelatedDoc] = Field(
        None, description="Информация про акт приёма-передачи."
    )
    act_of_mismatch: Optional[PostingFBSActListRelatedDoc] = Field(
        None, description="Информация про акт о расхождениях."
    )
    act_of_excess: Optional[PostingFBSActListRelatedDoc] = Field(
        None, description="Информация про акт об излишках."
    )


class PostingFBSActListResult(BaseModel):
    """Информация об отгрузке в списке актов.

    Attributes:
        id: Идентификатор отгрузки
        delivery_method_id: Идентификатор метода доставки
        delivery_method_name: Название метода доставки
        integration_type: Тип интеграции со службой доставки
        containers_count: Число грузовых мест
        status: Статус отгрузки
        departure_date: Дата отгрузки
        created_at: Дата создания записи об отгрузке
        updated_at: Дата обновления записи об отгрузке
        act_type: Тип акта приёма-передачи для FBS продавцов
        is_partial: Признак частичной перевозки
        has_postings_for_next_carriage: Признак наличия отправлений для следующей перевозки
        partial_num: Порядковый номер частичной перевозки
        related_docs: Информация про акты перевозки
    """
    id: Optional[int] = Field(
        None, description="Идентификатор отгрузки."
    )
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор метода доставки."
    )
    delivery_method_name: Optional[str] = Field(
        None, description="Название метода доставки."
    )
    integration_type: Optional[str] = Field(
        None, description="Тип интеграции со службой доставки."
    )
    containers_count: Optional[int] = Field(
        None, description="Число грузовых мест."
    )
    status: Optional[str] = Field(
        None, description="Статус отгрузки."
    )
    departure_date: Optional[str] = Field(
        None, description="Дата отгрузки."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания записи об отгрузке."
    )
    updated_at: Optional[str] = Field(
        None, description="Дата обновления записи об отгрузке."
    )
    act_type: Optional[str] = Field(
        None, description="Тип акта приёма-передачи для FBS продавцов."
    )
    is_partial: Optional[bool] = Field(
        None, description="Признак частичной перевозки. `true`, если перевозка частичная."
    )
    has_postings_for_next_carriage: Optional[bool] = Field(
        None, description="Признак наличия отправлений, подлежащих отгрузке в следующей перевозке."
    )
    partial_num: Optional[int] = Field(
        None, description="Порядковый номер частичной перевозки."
    )
    related_docs: Optional[PostingFBSActListRelatedDocs] = Field(
        None, description="Информация про акты перевозки."
    )


class PostingFBSActListResponse(BaseModel):
    """Описывает схему ответа на запрос списка актов по отгрузкам.

    Attributes:
        result: Список отгрузок с информацией об актах
    """
    result: Optional[list[PostingFBSActListResult]] = Field(
        None, description="Результат запроса."
    )
