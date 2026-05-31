"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateMarkedProductsSalesReport"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CreateReportResult


class ReportMarkedProductsSalesCreateDate(BaseModel):
    """Период отчёта по продажам маркированных товаров.

    Attributes:
        from_: Дата начала отчётного периода (сериализуется как `from`)
        to: Дата окончания отчётного периода
    """
    model_config = {'populate_by_name': True}

    from_: Optional[str] = Field(
        None, alias="from", description="Дата начала отчётного периода."
    )
    to: Optional[str] = Field(
        None, description="Дата окончания отчётного периода."
    )


class ReportMarkedProductsSalesCreateRequest(BaseModel):
    """Описывает схему запроса на создание отчёта по продажам товаров с маркировкой.

    Attributes:
        date: Период отчёта
    """
    date: Optional[ReportMarkedProductsSalesCreateDate] = Field(
        None, description="Период отчёта."
    )


class ReportMarkedProductsSalesCreateResponse(BaseModel):
    """Описывает схему ответа на запрос отчёта по продажам товаров с маркировкой.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[CreateReportResult] = Field(
        None, description="Результат создания отчёта."
    )
