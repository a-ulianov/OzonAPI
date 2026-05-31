"""Схемы метода finance_compensation (отчёт о компенсациях, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinanceReportCode


class FinanceCompensationRequest(BaseModel):
    """Параметры запроса формирования отчёта о компенсациях.

    Attributes:
        date: Период отчёта в формате `YYYY-MM`
        language: Язык отчёта
    """
    date: str = Field(..., description="Период отчёта в формате `YYYY-MM`.")
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class FinanceCompensationResponse(BaseModel):
    """Ответ с идентификатором сформированного отчёта.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[FinanceReportCode] = Field(
        None, description="Результат создания отчёта."
    )
