"""Общая модель результата создания отчёта."""
from typing import Optional

from pydantic import BaseModel, Field


class CreateReportResult(BaseModel):
    """Результат создания отчёта.

    Attributes:
        code: Уникальный идентификатор отчёта
    """
    code: Optional[str] = Field(
        None, description="Уникальный идентификатор отчёта."
    )
