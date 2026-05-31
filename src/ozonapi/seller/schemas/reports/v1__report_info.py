"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_ReportInfo"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import Report


class ReportInfoRequest(BaseModel):
    """Описывает схему запроса на получение информации об отчёте.

    Attributes:
        code: Уникальный идентификатор отчёта
    """
    code: str = Field(
        ..., description="Уникальный идентификатор отчёта."
    )


class ReportInfoResponse(BaseModel):
    """Описывает схему ответа на запрос информации об отчёте.

    Attributes:
        result: Информация об отчёте
    """
    result: Optional[Report] = Field(
        None, description="Информация об отчёте."
    )
