"""Схемы метода finance_document_b2b_sales (отчёт по продажам юр. лицам, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinanceReportCode


class FinanceDocumentB2BSalesRequest(BaseModel):
    """Параметры запроса формирования отчёта по продажам юридическим лицам.

    Attributes:
        date: Период отчёта в формате `YYYY-MM`
        language: Язык отчёта
    """
    date: str = Field(..., description="Период отчёта в формате `YYYY-MM`.")
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class FinanceDocumentB2BSalesResponse(BaseModel):
    """Ответ с идентификатором сформированного отчёта.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[FinanceReportCode] = Field(
        None, description="Результат создания отчёта."
    )
