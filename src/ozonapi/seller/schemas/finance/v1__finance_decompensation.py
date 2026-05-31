"""Схемы метода finance_decompensation (отчёт о декомпенсациях, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinanceReportCode


class FinanceDecompensationRequest(BaseModel):
    """Параметры запроса формирования отчёта о декомпенсациях.

    Attributes:
        date: Период отчёта в формате `YYYY-MM`
        language: Язык отчёта
    """
    date: str = Field(..., description="Период отчёта в формате `YYYY-MM`.")
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class FinanceDecompensationResponse(BaseModel):
    """Ответ с идентификатором сформированного отчёта.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[FinanceReportCode] = Field(
        None, description="Результат создания отчёта."
    )
