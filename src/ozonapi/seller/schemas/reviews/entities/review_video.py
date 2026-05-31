"""Общая модель видео отзыва."""
from typing import Optional

from pydantic import BaseModel, Field


class ReviewVideo(BaseModel):
    """Информация о видео отзыва.

    Attributes:
        url: Ссылка на видео
        preview_url: Ссылка на превью видео
        short_video_preview_url: Ссылка на короткое видео
        width: Ширина
        height: Высота
    """
    url: Optional[str] = Field(
        None, description="Ссылка на видео."
    )
    preview_url: Optional[str] = Field(
        None, description="Ссылка на превью видео."
    )
    short_video_preview_url: Optional[str] = Field(
        None, description="Ссылка на короткое видео."
    )
    width: Optional[int] = Field(
        None, description="Ширина."
    )
    height: Optional[int] = Field(
        None, description="Высота."
    )
