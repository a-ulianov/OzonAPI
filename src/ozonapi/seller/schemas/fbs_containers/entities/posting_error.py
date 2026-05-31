"""Общая модель ошибки по отправлению в грузоместе."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingError(BaseModel):
    """Ошибка обработки отправления.

    Attributes:
        posting_number: Номер отправления
        error_message: Текст ошибки
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    error_message: Optional[str] = Field(
        None, description="Текст ошибки."
    )
