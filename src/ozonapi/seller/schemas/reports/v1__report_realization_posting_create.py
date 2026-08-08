"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyFinanceRealizationPostingReport"""
from typing import Optional

from pydantic import BaseModel, Field


class ReportRealizationPostingCreateRequest(BaseModel):
    """Описывает схему запроса на создание позаказного отчёта о реализации товаров.

    Attributes:
        month: Номер месяца отчётного периода (от 1 до 12)
        year: Год отчётного периода
    """
    month: int = Field(
        ..., description="Номер месяца отчётного периода — от 1 до 12."
    )
    year: int = Field(
        ..., description="Год отчётного периода."
    )


class ReportRealizationPostingCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания позаказного отчёта о реализации.

    Attributes:
        code: Уникальный идентификатор отчёта
    """
    code: Optional[str] = Field(
        None, description="Уникальный идентификатор отчёта."
    )
