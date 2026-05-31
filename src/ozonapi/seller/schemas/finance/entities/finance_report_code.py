"""Общая модель результата создания финансового отчёта."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceReportCode(BaseModel):
    """Результат создания финансового отчёта.

    Attributes:
        code: Уникальный идентификатор отчёта
    """
    code: Optional[str] = Field(
        None, description="Уникальный идентификатор отчёта."
    )
