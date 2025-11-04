from typing import Optional

from pydantic import Field

from .filter import PostingFilter
from .filter_with import PostingFilterWith
from ...base import BaseRequestOffset
from ....common.enumerations.requests import SortingDirection


class PostingRequest(BaseRequestOffset):
    """Описывает схему запроса на получение информации об отправлениях.

    Attributes:
        dir: Направление сортировки
        filter: Фильтр выборки
        limit: Количество значений в ответе
        offset: Количество элементов, которое будет пропущено в ответе
        with_: Дополнительные поля, которые нужно добавить в ответ
    """
    model_config = {'populate_by_name': True}

    dir: Optional[SortingDirection] = Field(
        SortingDirection.ASC, description="Направление сортировки."
    )
    filter: PostingFilter = Field(
        ..., description="Фильтр запроса."
    )
    limit: Optional[int] = Field(
        1000, description="Количество значений в ответе.",
        ge=1, le=1000,
    )
    with_: Optional[PostingFilterWith] = Field(
        None, description="Дополнительные поля, которые нужно добавить в ответ.",
        alias="with",
    )