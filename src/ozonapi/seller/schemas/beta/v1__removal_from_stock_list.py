"""Схемы метода removal_from_stock_list (отчёт по вывозу и утилизации со стока FBO, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import RemovalReturnsSummaryRow


class RemovalFromStockListRequest(BaseModel):
    """Параметры запроса отчёта по вывозу и утилизации со стока FBO.

    Attributes:
        date_from: Начало периода
        date_to: Конец периода
        last_id: Идентификатор последнего значения для пагинации
        limit: Количество значений в ответе
    """
    date_from: Optional[str] = Field(None, description="Начало периода.")
    date_to: Optional[str] = Field(None, description="Конец периода.")
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")


class RemovalFromStockListResponse(BaseModel):
    """Ответ с отчётом по вывозу и утилизации со стока FBO.

    Attributes:
        last_id: Идентификатор последнего значения для пагинации
        returns_summary_report_rows: Строки отчёта
    """
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
    returns_summary_report_rows: Optional[list[RemovalReturnsSummaryRow]] = Field(
        None, description="Строки отчёта."
    )
