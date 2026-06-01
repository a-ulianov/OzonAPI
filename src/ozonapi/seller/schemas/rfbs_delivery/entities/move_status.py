"""Общая модель ответа на смену статуса отправления rFBS."""
from typing import Optional

from pydantic import BaseModel, Field


class FbsPostingMoveStatus(BaseModel):
    """Результат смены статуса для одного отправления.

    Attributes:
        error: Текст ошибки, если статус не изменён
        posting_number: Номер отправления
        result: Признак успешной смены статуса
    """
    error: Optional[str] = Field(
        None, description="Текст ошибки, если статус не изменён."
    )
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    result: Optional[bool] = Field(
        None, description="Признак успешной смены статуса."
    )


class FbsPostingMoveStatusResponse(BaseModel):
    """Ответ на смену статуса отправлений rFBS.

    Attributes:
        result: Результаты смены статуса по каждому отправлению
    """
    result: Optional[list[FbsPostingMoveStatus]] = Field(
        None, description="Результаты смены статуса по каждому отправлению."
    )
