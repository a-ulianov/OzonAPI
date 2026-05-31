"""Схемы метода finance_realization (отчёт о реализации товаров, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinanceCommission, FinanceRealizationHeader, FinanceRowItem


class FinanceRealizationRequest(BaseModel):
    """Параметры запроса отчёта о реализации товаров.

    Attributes:
        month: Номер месяца отчёта
        year: Год отчёта
    """
    month: int = Field(..., description="Номер месяца отчёта.")
    year: int = Field(..., description="Год отчёта.")


class FinanceRealizationRow(BaseModel):
    """Строка отчёта о реализации товаров.

    Attributes:
        row_number: Номер строки в отчёте
        item: Информация о товаре
        delivery_commission: Информация о комиссии за доставку
        return_commission: Информация о комиссии за возврат
        commission_ratio: Процент комиссии
        seller_price_per_instance: Цена продавца за экземпляр
    """
    model_config = {'populate_by_name': True}

    row_number: Optional[int] = Field(
        None, alias="rowNumber", description="Номер строки в отчёте."
    )
    item: Optional[FinanceRowItem] = Field(
        None, description="Информация о товаре."
    )
    delivery_commission: Optional[FinanceCommission] = Field(
        None, description="Информация о комиссии за доставку."
    )
    return_commission: Optional[FinanceCommission] = Field(
        None, description="Информация о комиссии за возврат."
    )
    commission_ratio: Optional[float] = Field(
        None, description="Процент комиссии."
    )
    seller_price_per_instance: Optional[float] = Field(
        None, description="Цена продавца за экземпляр."
    )


class FinanceRealizationResult(BaseModel):
    """Содержимое отчёта о реализации товаров.

    Attributes:
        header: Заголовок отчёта
        rows: Строки отчёта по товарам
    """
    header: Optional[FinanceRealizationHeader] = Field(
        None, description="Заголовок отчёта."
    )
    rows: Optional[list[FinanceRealizationRow]] = Field(
        None, description="Строки отчёта по товарам."
    )


class FinanceRealizationResponse(BaseModel):
    """Ответ с отчётом о реализации товаров.

    Attributes:
        result: Содержимое отчёта
    """
    result: Optional[FinanceRealizationResult] = Field(
        None, description="Содержимое отчёта."
    )
