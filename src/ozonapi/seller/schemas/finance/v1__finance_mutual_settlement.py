"""Схемы метода finance_mutual_settlement (отчёт о взаиморасчётах, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinanceReportCode


class FinanceMutualSettlementRequest(BaseModel):
    """Параметры запроса формирования отчёта о взаиморасчётах.

    Attributes:
        date: Период отчёта в формате `YYYY-MM`
        language: Язык отчёта
    """
    date: str = Field(..., description="Период отчёта в формате `YYYY-MM`.")
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class FinanceMutualSettlementResponse(BaseModel):
    """Ответ с идентификатором сформированного отчёта.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[FinanceReportCode] = Field(
        None, description="Результат создания отчёта."
    )
