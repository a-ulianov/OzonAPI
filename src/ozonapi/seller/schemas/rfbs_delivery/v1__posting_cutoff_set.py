"""Схемы метода posting_cutoff_set (уточнение даты отгрузки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingCutoffSetRequest(BaseModel):
    """Параметры запроса уточнения даты отгрузки.

    Attributes:
        new_cutoff_date: Новая дата отгрузки
        posting_number: Номер отправления
    """
    new_cutoff_date: str = Field(..., description="Новая дата отгрузки.")
    posting_number: str = Field(..., description="Номер отправления.")


class PostingCutoffSetResponse(BaseModel):
    """Ответ на уточнение даты отгрузки.

    Attributes:
        result: Признак успешного уточнения
    """
    result: Optional[bool] = Field(None, description="Признак успешного уточнения.")
