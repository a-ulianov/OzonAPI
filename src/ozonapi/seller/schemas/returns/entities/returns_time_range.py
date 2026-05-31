"""Общая модель периода времени в разделе Возвраты."""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsTimeRange(BaseModel):
    """Период времени.

    Attributes:
        time_from: Начало периода
        time_to: Окончание периода
    """
    time_from: Optional[str] = Field(
        None, description="Начало периода."
    )
    time_to: Optional[str] = Field(
        None, description="Окончание периода."
    )
