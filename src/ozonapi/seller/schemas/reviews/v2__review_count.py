"""https://docs.ozon.ru/api/seller/#operation/Review_CountV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCountResponse(BaseModel):
    """Описывает схему ответа на запрос количества отзывов по статусам.

    Attributes:
        total: Количество всех отзывов
        new: Количество новых отзывов
        viewed: Количество просмотренных отзывов
        processed: Количество обработанных отзывов
    """
    total: Optional[int] = Field(
        None, description="Количество всех отзывов."
    )
    new: Optional[int] = Field(
        None, description="Количество новых отзывов."
    )
    viewed: Optional[int] = Field(
        None, description="Количество просмотренных отзывов."
    )
    processed: Optional[int] = Field(
        None, description="Количество обработанных отзывов."
    )
