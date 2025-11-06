from typing import Optional

from pydantic import Field, BaseModel

from .entities.posting__posting import PostingFBOPosting
from ..entities.postings import PostingRequest


class PostingFBOListRequest(PostingRequest):
    """Описывает схему запроса на получение информации об отправлениях FBO.

    Attributes:
        dir: Направление сортировки
        filter: Фильтр выборки
        limit: Количество значений в ответе
        offset: Количество элементов, которое будет пропущено в ответе
        with_: Дополнительные поля, которые нужно добавить в ответ
        translit: Если включена транслитерация адреса из кириллицы в латиницу — true
    """
    translit: Optional[bool] = Field(
        False
    )


class PostingFBOListResponse(BaseModel):
    """Описывает схему ответа на запрос на получение информации об отправлениях FBO.

    Attributes:
        result: Массив отправлений
    """
    result: Optional[list[PostingFBOPosting]] = Field(
        default_factory=list, description="Массив отправлений."
    )