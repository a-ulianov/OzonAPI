"""Общая модель периода в разделе Финансовые отчёты."""
from typing import Optional

from pydantic import BaseModel, Field


class FinancePeriod(BaseModel):
    """Период отчёта.

    Attributes:
        from_: Начало периода (сериализуется как `from`)
        to: Конец периода
    """
    model_config = {'populate_by_name': True}

    from_: Optional[str] = Field(
        None, alias="from", description="Начало периода."
    )
    to: Optional[str] = Field(
        None, description="Конец периода."
    )
