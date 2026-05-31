"""Общая модель склада/места в разделе Возвраты."""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsPlace(BaseModel):
    """Информация о складе (месте).

    Attributes:
        id: Идентификатор склада
        name: Название
        address: Адрес
    """
    id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )
    name: Optional[str] = Field(
        None, description="Название."
    )
    address: Optional[str] = Field(
        None, description="Адрес."
    )
