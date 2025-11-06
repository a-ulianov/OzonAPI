from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingFBOPosting
from ..entities.postings import PostingFilterWith


class PostingFBOGetRequest(BaseModel):
    """Описывает схему запроса на получение информации об определенном отправлении FBO.

    Attributes:
        posting_number: Номер отправления
        translit: Если включена транслитерация адреса из кириллицы в латиницу — true (опционально)
        with_: Дополнительные поля, которые нужно добавить в ответ (опционально)
    """
    model_config = {'populate_by_name': True}

    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    translit: Optional[bool] = Field(
        None, description="Если включена транслитерация адреса из кириллицы в латиницу — true."
    )
    with_: Optional[PostingFilterWith] = Field(
        None, description="Дополнительные поля, которые нужно добавить в ответ."
    )


class PostingFBOGetResponse(BaseModel):
    """Описывает схему ответа на запрос о получении информации об определенном отправлении FBO.

    Attributes:
        result: Результат запроса
    """
    result: Optional[PostingFBOPosting] = Field(
        None, description="Результат запроса."
    )