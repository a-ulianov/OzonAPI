"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Report


class ReportListRequest(BaseModel):
    """Описывает схему запроса на получение списка отчётов.

    Attributes:
        page: Номер страницы
        page_size: Количество значений на странице
        report_type: Тип отчёта
    """
    page: int = Field(
        ..., description="Номер страницы."
    )
    page_size: int = Field(
        ..., description="Количество значений на странице."
    )
    report_type: Optional[str] = Field(
        None, description="Тип отчёта."
    )


class ReportListResult(BaseModel):
    """Результат запроса списка отчётов.

    Attributes:
        reports: Массив со всеми сгенерированными отчётами
        total: Суммарное количество отчётов
    """
    reports: Optional[list[Report]] = Field(
        None, description="Массив со всеми сгенерированными отчётами."
    )
    total: Optional[int] = Field(
        None, description="Суммарное количество отчётов."
    )


class ReportListResponse(BaseModel):
    """Описывает схему ответа на запрос списка отчётов.

    Attributes:
        result: Результат запроса
    """
    result: Optional[ReportListResult] = Field(
        None, description="Результат запроса."
    )
