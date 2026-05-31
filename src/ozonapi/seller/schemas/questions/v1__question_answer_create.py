"""https://docs.ozon.ru/api/seller/#operation/Question_AnswerCreate"""
from typing import Optional

from pydantic import BaseModel, Field


class QuestionAnswerCreateRequest(BaseModel):
    """Описывает схему запроса на создание ответа на вопрос.

    Attributes:
        question_id: Идентификатор вопроса
        sku: Идентификатор товара в системе Ozon — SKU
        text: Текст ответа (от 2 до 3000 символов)
    """
    question_id: str = Field(
        ..., description="Идентификатор вопроса."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    text: str = Field(
        ..., description="Текст ответа объёмом от 2 до 3000 символов."
    )


class QuestionAnswerCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания ответа на вопрос.

    Attributes:
        answer_id: Идентификатор ответа на вопрос
    """
    answer_id: Optional[str] = Field(
        None, description="Идентификатор ответа на вопрос."
    )
