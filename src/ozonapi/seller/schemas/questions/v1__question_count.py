"""https://docs.ozon.ru/api/seller/#operation/Question_Count"""
from typing import Optional

from pydantic import BaseModel, Field


class QuestionCountResponse(BaseModel):
    """Описывает схему ответа на запрос количества вопросов по статусам.

    Attributes:
        all: Всего вопросов
        new: Новые вопросы
        viewed: Просмотренные вопросы
        processed: Обработанные вопросы
        unprocessed: Необработанные вопросы
    """
    all: Optional[int] = Field(
        None, description="Всего вопросов."
    )
    new: Optional[int] = Field(
        None, description="Новые вопросы."
    )
    viewed: Optional[int] = Field(
        None, description="Просмотренные вопросы."
    )
    processed: Optional[int] = Field(
        None, description="Обработанные вопросы."
    )
    unprocessed: Optional[int] = Field(
        None, description="Необработанные вопросы."
    )
