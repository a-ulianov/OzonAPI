"""Общая модель запроса смены статуса по номерам отправлений rFBS."""
from typing import Optional

from pydantic import BaseModel, Field


class FbsPostingNumbersRequest(BaseModel):
    """Параметры запроса со списком номеров отправлений.

    Attributes:
        posting_number: Номера отправлений
    """
    posting_number: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )
