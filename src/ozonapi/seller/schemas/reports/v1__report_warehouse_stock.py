"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateWarehouseStockReport"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CreateReportResult


class ReportWarehouseStockRequest(BaseModel):
    """Описывает схему запроса на создание отчёта об остатках на FBS-складе.

    Attributes:
        warehouseId: Идентификаторы складов
        language: Язык отчёта
    """
    warehouseId: list[str] = Field(
        ..., description="Идентификаторы складов."
    )
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class ReportWarehouseStockResponse(BaseModel):
    """Описывает схему ответа на запрос создания отчёта об остатках на FBS-складе.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[CreateReportResult] = Field(
        None, description="Результат создания отчёта."
    )
