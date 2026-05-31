"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerRemovePostings"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingError


class CarriageContainerRemovePostingsRequest(BaseModel):
    """Описывает схему запроса на удаление отправлений из грузоместа.

    Attributes:
        container_id: Идентификатор грузоместа
        posting_numbers: Номера отправлений
    """
    container_id: int = Field(
        ..., description="Идентификатор грузоместа."
    )
    posting_numbers: list[str] = Field(
        ..., description="Номера отправлений."
    )


class CarriageContainerRemovePostingsResponse(BaseModel):
    """Описывает схему ответа на запрос удаления отправлений из грузоместа.

    Attributes:
        task_id: Идентификатор задания
        error_postings: Ошибки по отправлениям
    """
    task_id: Optional[int] = Field(
        None, description="Идентификатор задания."
    )
    error_postings: Optional[list[PostingError]] = Field(
        None, description="Ошибки по отправлениям."
    )
