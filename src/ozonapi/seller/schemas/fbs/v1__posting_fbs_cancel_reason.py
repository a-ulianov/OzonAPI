"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetPostingFbsCancelReasonV1"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import PostingFBSCancelReason


class PostingFBSCancelReasonRequest(BaseModel):
    """Описывает схему запроса на получение информации о причинах отмены отправлений.

    Attributes:
        related_posting_numbers: номера отправлений
    """
    related_posting_numbers: list[str] = Field(
        ..., description="Номера отправлений."
    )


class PostingFBSCancelReasonResultItem(BaseModel):
    """Описывает схему с информацией о причинах отмены отправления.

    Attributes:
        posting_number: Номер отправления
        reasons: Информация о причинах отмены
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    reasons: Optional[list[PostingFBSCancelReason]] = Field(
        default_factory=list, description="Информация о причинах отмены."
    )


class PostingFBSCancelReasonResponse(BaseModel):
    """Описывает схему ответа на запрос на получение информации о причинах отмены отправлений.

    Attributes:
        result: Список отправлений с информацией о причинах их отмены
    """
    result: Optional[list[PostingFBSCancelReasonResultItem]] = Field(
        default_factory=list, description="Список отправлений с информацией о причинах их отмены."
    )