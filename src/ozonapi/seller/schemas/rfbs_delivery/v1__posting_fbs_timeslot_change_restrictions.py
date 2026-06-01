"""Схемы метода posting_fbs_timeslot_change_restrictions (v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFbsTimeslotChangeRestrictionsRequest(BaseModel):
    """Параметры запроса доступных дат переноса доставки.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(..., description="Номер отправления.")


class PostingFbsTimeslotChangeRestrictionsInterval(BaseModel):
    """Доступный интервал переноса доставки.

    Attributes:
        begin: Начало интервала
        end: Конец интервала
    """
    begin: Optional[str] = Field(None, description="Начало интервала.")
    end: Optional[str] = Field(None, description="Конец интервала.")


class PostingFbsTimeslotChangeRestrictionsResponse(BaseModel):
    """Ответ с доступными датами переноса доставки.

    Attributes:
        delivery_interval: Доступный интервал доставки
        remaining_changes_count: Оставшееся число переносов
    """
    delivery_interval: Optional[PostingFbsTimeslotChangeRestrictionsInterval] = Field(
        None, description="Доступный интервал доставки."
    )
    remaining_changes_count: Optional[int] = Field(
        None, description="Оставшееся число переносов."
    )
