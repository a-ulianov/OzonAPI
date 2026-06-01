"""Схемы метода posting_fbs_timeslot_set (перенос даты доставки, v1)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostingFbsTimeslotSetNewTimeslot(BaseModel):
    """Новый интервал доставки.

    Attributes:
        from_: Начало интервала
        to_: Конец интервала
    """
    model_config = ConfigDict(populate_by_name=True)

    from_: Optional[str] = Field(
        None, alias="from", description="Начало интервала."
    )
    to_: Optional[str] = Field(None, alias="to", description="Конец интервала.")


class PostingFbsTimeslotSetRequest(BaseModel):
    """Параметры запроса переноса даты доставки.

    Attributes:
        new_timeslot: Новый интервал доставки
        posting_number: Номер отправления
    """
    new_timeslot: Optional[PostingFbsTimeslotSetNewTimeslot] = Field(
        None, description="Новый интервал доставки."
    )
    posting_number: str = Field(..., description="Номер отправления.")


class PostingFbsTimeslotSetResponse(BaseModel):
    """Ответ на перенос даты доставки.

    Attributes:
        result: Признак успешного переноса
    """
    result: Optional[bool] = Field(None, description="Признак успешного переноса.")
