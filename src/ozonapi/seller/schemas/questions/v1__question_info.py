"""https://docs.ozon.ru/api/seller/#operation/Question_Info"""
from pydantic import BaseModel, Field

from .entities import Question


class QuestionInfoRequest(BaseModel):
    """Описывает схему запроса на получение информации о вопросе.

    Attributes:
        question_id: Идентификатор вопроса
    """
    question_id: str = Field(
        ..., description="Идентификатор вопроса."
    )


class QuestionInfoResponse(Question):
    """Описывает схему ответа на запрос информации о вопросе.

    Notes:
        • Содержит поля вопроса (см. общую модель `Question`).
    """
    pass
