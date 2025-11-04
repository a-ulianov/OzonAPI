import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...mixins import DateTimeSerializationMixin
from ....common.enumerations.postings import PostingStatus


class PostingFilter(DateTimeSerializationMixin, BaseModel):
    """Фильтр запроса на получение информации об отправлениях.

    Attributes:
        since: Начало периода, за который нужно получить отправления
        to_: Конец периода, за который нужно получить отправления
        status: Статус отправления
    """
    model_config = {'populate_by_name': True}

    since: datetime.datetime = Field(
        ..., description="Начало периода, за который нужно получить отправления. Период не более 1 года."
    )
    to_: datetime.datetime = Field(
        ..., description="Конец периода, за который нужно получить отправления. Период не более 1 года.",
        alias="to"
    )
    status: Optional[PostingStatus] = Field(
        None, description="Статус отправления."
    )

    serialize_datetime = DateTimeSerializationMixin.create_datetime_validator([
        'since', 'to_'
    ])