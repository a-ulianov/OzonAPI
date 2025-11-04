"""https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_GetFbsPostingListV3"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingFBSFilterWith
from .entities.posting__posting import PostingFBSPosting
from ..entities.postings import PostingFilter, PostingRequest
from ..mixins import DateTimeSerializationMixin


class PostingFBSListRequestFilterLastChangedStatusDate(DateTimeSerializationMixin, BaseModel):
    """Период, в который последний раз изменялся статус у отправлений.

    Attributes:
        from_: Дата начала периода
        to_: Дата окончания периода
    """
    model_config = {'populate_by_name': True}

    from_: datetime.datetime = Field(
        ...,
        description="Дата начала периода.",
        alias="from"
    )
    to_: datetime.datetime = Field(
        ...,
        description="Дата окончания периода.",
        alias="to"
    )

    serialize_datetime = DateTimeSerializationMixin.create_datetime_validator([
        'from_', 'to_'
    ])


class PostingFBSListFilter(PostingFilter):
    """Фильтр запроса на получение информации об отправлениях FBS.

    Attributes:
        since: Начало периода, за который нужно получить отправления
        to_: Конец периода, за который нужно получить отправления
        status: Статус отправления
        warehouse_id: Идентификаторы складов
        provider_id: Идентификаторы служб доставки
        delivery_method_id: Идентификаторы способов доставки
        order_id: Идентификатор заказа
        posting_number: Номер отправления
        product_offer_id: Идентификатор товара в системе продавца
        product_sku: Идентификатор товара в системе Ozon
        last_changed_status_date: Период изменения статуса
        is_quantum: Фильтр по квантовым отправлениям
    """
    warehouse_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификаторы складов. Можно получить с помощью метода warehouse_list()."
    )
    provider_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификаторы служб доставки. Можно получить с помощью метода delivery_method_list()."
    )
    delivery_method_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификаторы способов доставки. Можно получить с помощью метода delivery_method_list()."
    )
    order_id: Optional[int] = Field(
        None, description="Идентификатор заказа."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    product_offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    product_sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon."
    )
    last_changed_status_date: Optional[PostingFBSListRequestFilterLastChangedStatusDate] = Field(
        None, description="Период, в который последний раз изменялся статус у отправлений."
    )
    is_quantum: Optional[bool] = Field(
        None, description="true — получить только квантовые отправления, false — все отправления."
    )


class PostingFBSListRequest(PostingRequest):
    """Описывает схему запроса на получение информации об отправлениях FBS.

    Attributes:
        dir: Направление сортировки
        filter: Фильтр выборки
        limit: Количество значений в ответе
        offset: Количество элементов, которое будет пропущено в ответе
        with_: Дополнительные поля, которые нужно добавить в ответ
    """
    filter: PostingFBSListFilter = Field(
        ..., description="Фильтр запроса."
    )
    with_: Optional[PostingFBSFilterWith] = Field(
        None, description="Дополнительные поля, которые нужно добавить в ответ.",
        alias="with",
    )


class PostingFBSListResult(BaseModel):
    """Информация об отправлениях и их количестве.

    Attributes:
        has_next: Признак, что в ответе вернули не весь массив
        postings: Массив отправлений
    """
    has_next: bool = Field(
        ..., description="Признак, что в ответе вернули не весь массив."
    )
    postings: Optional[list[PostingFBSPosting]] = Field(
        default_factory=list, description="Массив отправлений."
    )


class PostingFBSListResponse(BaseModel):
    """Описывает схему ответа на запрос информации об отправлениях FBS.

    Attributes:
        result: Содержимое ответа
    """
    result: PostingFBSListResult = Field(
        ..., description="Содержимое ответа."
    )