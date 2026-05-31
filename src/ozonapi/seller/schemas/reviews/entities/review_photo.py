"""Общая модель изображения отзыва."""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewPhoto(BaseModel):
    """Информация об изображении отзыва.

    Attributes:
        url: Ссылка на изображение
        width: Ширина
        height: Высота
    """
    url: Optional[str] = Field(
        None, description="Ссылка на изображение."
    )
    width: Optional[int] = Field(
        None, description="Ширина."
    )
    height: Optional[int] = Field(
        None, description="Высота."
    )
