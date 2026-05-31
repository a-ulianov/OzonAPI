"""https://docs.ozon.ru/api/seller/#operation/Question_AnswerDelete"""
from pydantic import BaseModel, Field


class QuestionAnswerDeleteRequest(BaseModel):
    """Описывает схему запроса на удаление ответа на вопрос.

    Attributes:
        answer_id: Идентификатор ответа
        sku: Идентификатор товара в системе Ozon — SKU
    """
    answer_id: str = Field(
        ..., description="Идентификатор ответа."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )


class QuestionAnswerDeleteResponse(BaseModel):
    """Описывает схему ответа на запрос удаления ответа на вопрос.

    Notes:
        • При успешном удалении API возвращает пустой объект.
    """
    pass
