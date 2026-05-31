"""https://docs.ozon.ru/api/seller/#operation/Review_Count"""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCountV1Response(BaseModel):
    """Описывает схему ответа на запрос количества отзывов по статусам (v1).

    Attributes:
        total: Количество всех отзывов
        processed: Количество обработанных отзывов
        unprocessed: Количество необработанных отзывов
    """
    total: Optional[int] = Field(
        None, description="Количество всех отзывов."
    )
    processed: Optional[int] = Field(
        None, description="Количество обработанных отзывов."
    )
    unprocessed: Optional[int] = Field(
        None, description="Количество необработанных отзывов."
    )
