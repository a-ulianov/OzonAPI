"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateReturnsReportV2"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CreateReportResult


class ReportReturnsCreateFilter(BaseModel):
    """Фильтр для отчёта о возвратах.

    Attributes:
        delivery_schema: Схема работы (`FBS`, `FBO`)
        date_from: Дата начала периода
        date_to: Дата окончания периода
        status: Статус возврата
    """
    delivery_schema: Optional[str] = Field(
        None, description="Схема работы: `FBS`, `FBO`."
    )
    date_from: Optional[str] = Field(
        None, description="Дата, с которой данные отображаются в отчёте."
    )
    date_to: Optional[str] = Field(
        None, description="Дата, по которую данные отображаются в отчёте."
    )
    status: Optional[str] = Field(
        None, description="Фильтр по статусу возврата."
    )


class ReportReturnsCreateRequest(BaseModel):
    """Описывает схему запроса на создание отчёта о возвратах.

    Attributes:
        filter: Фильтр
        language: Язык отчёта
    """
    filter: ReportReturnsCreateFilter = Field(
        ..., description="Фильтр."
    )
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class ReportReturnsCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания отчёта о возвратах.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[CreateReportResult] = Field(
        None, description="Результат создания отчёта."
    )
