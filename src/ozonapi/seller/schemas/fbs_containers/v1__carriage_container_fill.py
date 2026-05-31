"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerFill"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingError


class CarriageContainerFillRequest(BaseModel):
    """Описывает схему запроса на наполнение грузоместа отправлениями.

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


class CarriageContainerFillResponse(BaseModel):
    """Описывает схему ответа на запрос наполнения грузоместа.

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
