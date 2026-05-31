"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyProductsReport"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CreateReportResult


class ReportProductsCreateRequest(BaseModel):
    """Описывает схему запроса на создание отчёта по товарам.

    Attributes:
        sku: Идентификаторы товаров в системе Ozon — SKU
        offer_id: Идентификаторы товаров в системе продавца
        search: Поиск по содержанию записи
        visibility: Видимость товаров
        language: Язык отчёта
    """
    sku: Optional[list[int]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    offer_id: Optional[list[str]] = Field(
        None, description="Идентификаторы товаров в системе продавца."
    )
    search: Optional[str] = Field(
        None, description="Поиск по содержанию записи."
    )
    visibility: Optional[str] = Field(
        None, description="Видимость товаров."
    )
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class ReportProductsCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания отчёта по товарам.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[CreateReportResult] = Field(
        None, description="Результат создания отчёта."
    )
