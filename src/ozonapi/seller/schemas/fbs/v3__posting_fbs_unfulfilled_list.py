"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingUnfulfilledList"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field, model_validator

from .entities import PostingFBSFilterWith
from .entities.posting__posting import PostingFBSPosting
from ..mixins import DateTimeSerializationMixin
from ...common.enumerations.postings import PostingStatus
from ...common.enumerations.requests import SortingDirection
from ..base import BaseRequestOffset


class PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate(BaseModel):
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


class PostingFBSUnfulfilledListFilter(DateTimeSerializationMixin, BaseModel):
    """Фильтр запроса на получение информации о необработанных отправлениях FBS и rFBS
    за указанный период времени (максимум 1 год).

    Используйте фильтр либо по времени сборки — cutoff, либо по дате передачи отправления в доставку — delivering_date.
    Если использовать их вместе, в ответе вернётся ошибка.

    Чтобы использовать фильтр по времени сборки, заполните поля cutoff_from и cutoff_to.

    Чтобы использовать фильтр по дате передачи отправления в доставку,
    заполните поля delivering_date_from и delivering_date_to.

    Attributes:
        cutoff_from: Начало периода до которого продавцу нужно собрать заказ (опционально)
        cutoff_to: Конец периода до которого продавцу нужно собрать заказ (опционально)
        delivering_date_from: Минимальная дата передачи отправления в доставку (опционально)
        delivering_date_to: Максимальная дата передачи отправления в доставку (опционально)
        delivery_method_id: Список идентификаторов способов доставки (опционально, можно получить с помощью метода delivery_method_list())
        is_quantum: true, чтобы получить только отправления квантов, false - все отправления (опционально)
        provider_id: Идентификатор службы доставки (опционально, можно получить с помощью метода delivery_method_list())
        status: Статус отправления (опционально)
        warehouse_id: Идентификатор склада (опционально, можно получить с помощью метода warehouse_list())
        last_changed_status_date: Период, в который последний раз изменялся статус у отправлений (опционально)
    """
    cutoff_from: Optional[datetime.datetime | str] = Field(
        None, description="Фильтр по времени, до которого продавцу нужно собрать заказ. Начало периода."
    )
    cutoff_to: Optional[datetime.datetime | str] = Field(
        None, description="Фильтр по времени, до которого продавцу нужно собрать заказ. Конец периода."
    )
    delivering_date_from: Optional[datetime.datetime | str] = Field(
        None, description="Минимальная дата передачи отправления в доставку."
    )
    delivering_date_to: Optional[datetime.datetime | str] = Field(
        None, description="Максимальная дата передачи отправления в доставку."
    )
    delivery_method_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификаторы способов доставки. Можно получить с помощью метода delivery_method_list()."
    )
    is_quantum: Optional[bool] = Field(
        False, description="true, чтобы получить только отправления квантов. false - все отправления."
    )
    provider_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификатор службы доставки. Можно получить с помощью метода delivery_method_list()."
    )
    status: Optional[PostingStatus] = Field(
        None, description="Статус отправления."
    )
    warehouse_id: Optional[list[int]] = Field(
        default_factory=list, description="Идентификатор склада. Можно получить с помощью метода warehouse_list()."
    )
    last_changed_status_date: Optional[PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate] = Field(
        None, description="Период, в который последний раз изменялся статус у отправлений."
    )

    serialize_datetime = DateTimeSerializationMixin.create_datetime_validator([
        'cutoff_from', 'cutoff_to', 'delivering_date_from', 'delivering_date_to',
    ])

    @model_validator(mode='after')
    def validate_exclusive_filters(self) -> 'PostingFBSUnfulfilledListFilter':
        cutoff_filled = self.cutoff_from is not None or self.cutoff_to is not None

        delivering_date_filled = self.delivering_date_from is not None or self.delivering_date_to is not None

        if cutoff_filled and delivering_date_filled:
            raise ValueError(
                "Нельзя использовать одновременно фильтры cutoff и delivering_date. "
            )

        if not cutoff_filled and not delivering_date_filled:
            raise ValueError(
                "Должен быть использован один из фильтров: либо cutoff, либо delivering_date."
            )

        return self


class PostingFBSUnfulfilledListRequest(BaseRequestOffset):
    """Описывает схему запроса на получение информации о необработанных отправлениях FBS и rFBS
    за указанный период времени (максимум 1 год).

    Attributes:
        dir: Направление сортировки (опционально)
        filter: Фильтр выборки (опционально)
        limit: Количество значений в ответе (опционально, максимум 1000)
        offset (int): Количество элементов, которое будет пропущено в ответе (опционально)
        with_: Дополнительные поля, которые нужно добавить в ответ (опционально)
    """
    model_config = {'populate_by_name': True}

    dir: Optional[SortingDirection] = Field(
        SortingDirection.ASC, description="Направление сортировки."
    )
    filter: PostingFBSUnfulfilledListFilter = Field(
        ..., description="Фильтр запроса. Используйте фильтр либо cutoff, либо delivering_date. Иначе будет ошибка."
    )
    limit: Optional[int] = Field(
        1000, description="Количество значений в ответе.",
        ge=1, le=1000,
    )
    with_: Optional[PostingFBSFilterWith] = Field(
        None, description="Дополнительные поля, которые нужно добавить в ответ.",
        alias="with",
    )


class PostingFBSUnfulfilledListResult(BaseModel):
    """Информация о необработанных отправлениях и их количестве.

    Attributes:
        count: Счётчик элементов в ответе
        postings: Массив отправлений
    """
    count: int = Field(
        ..., description="Счётчик элементов в ответе.",
    )
    postings: Optional[list[PostingFBSPosting]] = Field(
        default_factory=list, description="Массив отправлений."
    )


class PostingFBSUnfulfilledListResponse(BaseModel):
    """Описывает схему ответа на запрос информации о необработанных отправлениях FBS и rFBS.

    Attributes:
        result: Содержимое ответа
    """
    result: PostingFBSUnfulfilledListResult = Field(
        ..., description="Содержимое ответа."
    )