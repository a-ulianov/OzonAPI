"""https://docs.ozon.ru/api/seller/#operation/Question_ChangeStatus"""
from pydantic import BaseModel, Field


class QuestionChangeStatusRequest(BaseModel):
    """Описывает схему запроса на изменение статуса вопросов.

    Attributes:
        question_ids: Идентификаторы вопросов
        status: Статус вопросов (`NEW`, `VIEWED`, `PROCESSED`)
    """
    question_ids: list[str] = Field(
        ..., description="Идентификаторы вопросов."
    )
    status: str = Field(
        ..., description="Статусы вопросов: `NEW` — новые, `VIEWED` — просмотренные, `PROCESSED` — обработанные."
    )


class QuestionChangeStatusResponse(BaseModel):
    """Описывает схему ответа на запрос изменения статуса вопросов.

    Notes:
        • При успешном выполнении API возвращает пустой объект.
    """
    pass
