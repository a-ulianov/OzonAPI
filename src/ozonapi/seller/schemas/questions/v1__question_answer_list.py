"""https://docs.ozon.ru/api/seller/#operation/Question_AnswerList"""
from typing import Optional

from pydantic import BaseModel, Field


class QuestionAnswerListRequest(BaseModel):
    """Описывает схему запроса на получение списка ответов на вопрос.

    Attributes:
        question_id: Идентификатор вопроса
        sku: Идентификатор товара в системе Ozon — SKU
        last_id: Идентификатор последнего значения на странице
    """
    question_id: str = Field(
        ..., description="Идентификатор вопроса."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )


class QuestionAnswerListAnswer(BaseModel):
    """Ответ на вопрос.

    Attributes:
        id: Идентификатор ответа
        question_id: Идентификатор вопроса
        sku: Идентификатор товара в системе Ozon — SKU
        text: Текст ответа
        author_name: Автор ответа
        published_at: Дата публикации ответа
        status_publication: Статус публикации ответа
    """
    id: Optional[str] = Field(
        None, description="Идентификатор ответа."
    )
    question_id: Optional[str] = Field(
        None, description="Идентификатор вопроса."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    text: Optional[str] = Field(
        None, description="Текст ответа."
    )
    author_name: Optional[str] = Field(
        None, description="Автор ответа."
    )
    published_at: Optional[str] = Field(
        None, description="Дата публикации ответа."
    )
    status_publication: Optional[str] = Field(
        None, description="Статус публикации ответа."
    )


class QuestionAnswerListResponse(BaseModel):
    """Описывает схему ответа на запрос списка ответов на вопрос.

    Attributes:
        answers: Ответы
        last_id: Идентификатор последнего значения на странице
    """
    answers: Optional[list[QuestionAnswerListAnswer]] = Field(
        None, description="Ответы."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения на странице."
    )
