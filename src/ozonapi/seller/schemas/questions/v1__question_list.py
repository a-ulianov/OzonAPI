"""https://docs.ozon.ru/api/seller/#operation/Question_List"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Question


class QuestionListFilter(BaseModel):
    """Фильтр для получения списка вопросов.

    Attributes:
        status: Статус вопроса
        date_from: Начало периода
        date_to: Конец периода
    """
    status: Optional[str] = Field(
        None, description="Статусы вопроса: `NEW`, `VIEWED`, `PROCESSED`."
    )
    date_from: Optional[str] = Field(
        None, description="Начало периода."
    )
    date_to: Optional[str] = Field(
        None, description="Конец периода."
    )


class QuestionListRequest(BaseModel):
    """Описывает схему запроса на получение списка вопросов.

    Attributes:
        limit: Количество значений в ответе
        last_id: Идентификатор последнего значения на странице
        sort_dir: Направление сортировки (`ASC` / `DESC`)
        filter: Фильтр для поиска вопросов
    """
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки: `ASC` — по возрастанию, `DESC` — по убыванию."
    )
    filter: Optional[QuestionListFilter] = Field(
        None, description="Фильтр для поиска вопросов."
    )


class QuestionListResponse(BaseModel):
    """Описывает схему ответа на запрос списка вопросов.

    Attributes:
        questions: Вопросы
        last_id: Идентификатор последнего значения на странице
        has_next: Признак наличия следующей страницы
    """
    questions: Optional[list[Question]] = Field(
        None, description="Вопросы."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )
    has_next: Optional[bool] = Field(
        None, description="`true`, если в ответе вернулись не все вопросы."
    )
