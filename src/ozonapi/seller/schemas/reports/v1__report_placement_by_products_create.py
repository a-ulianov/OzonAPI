"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreatePlacementByProductsReport"""
from typing import Optional

from pydantic import BaseModel, Field


class ReportPlacementByProductsCreateRequest(BaseModel):
    """Описывает схему запроса на создание отчёта о стоимости размещения по товарам.

    Attributes:
        date_from: Дата начала отчётного периода
        date_to: Дата окончания отчётного периода
    """
    date_from: str = Field(
        ..., description="Дата начала отчётного периода."
    )
    date_to: str = Field(
        ..., description="Дата окончания отчётного периода."
    )


class ReportPlacementByProductsCreateResponse(BaseModel):
    """Описывает схему ответа на запрос отчёта о стоимости размещения по товарам.

    Attributes:
        code: Уникальный идентификатор отчёта
    """
    code: Optional[str] = Field(
        None, description="Уникальный идентификатор отчёта."
    )
