"""Схемы метода fbs_posting_tracking_number_set (добавление трек-номеров, v2)."""
from typing import Optional

from pydantic import BaseModel, Field


class FbsPostingTrackingNumber(BaseModel):
    """Трек-номер отправления.

    Attributes:
        posting_number: Номер отправления
        tracking_number: Трек-номер
    """
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    tracking_number: Optional[str] = Field(None, description="Трек-номер.")


class FbsPostingTrackingNumberSetRequest(BaseModel):
    """Параметры запроса добавления трек-номеров.

    Attributes:
        tracking_numbers: Список трек-номеров отправлений
    """
    tracking_numbers: Optional[list[FbsPostingTrackingNumber]] = Field(
        None, description="Список трек-номеров отправлений."
    )
