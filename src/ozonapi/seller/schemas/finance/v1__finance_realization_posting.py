"""Схемы метода finance_realization_posting (отчёт о реализации по отправлениям, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinanceCommission, FinanceRealizationHeader, FinanceRowItem


class FinanceRealizationPostingRequest(BaseModel):
    """Параметры запроса отчёта о реализации товаров по отправлениям.

    Attributes:
        month: Номер месяца отчёта
        year: Год отчёта
    """
    month: int = Field(..., description="Номер месяца отчёта.")
    year: int = Field(..., description="Год отчёта.")


class FinanceRealizationPostingOrder(BaseModel):
    """Информация об отправлении в строке отчёта.

    Attributes:
        posting_number: Номер отправления
        created_date: Дата создания отправления
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    created_date: Optional[str] = Field(
        None, description="Дата создания отправления."
    )


class FinanceRealizationPostingDocument(BaseModel):
    """Информация о документе юридического лица в строке отчёта.

    Attributes:
        number: Номер документа
        sale_date: Дата продажи
    """
    number: Optional[str] = Field(
        None, description="Номер документа."
    )
    sale_date: Optional[str] = Field(
        None, description="Дата продажи."
    )


class FinanceRealizationPostingRow(BaseModel):
    """Строка отчёта о реализации товаров по отправлениям.

    Attributes:
        row_number: Номер строки в отчёте
        item: Информация о товаре
        delivery_commission: Информация о комиссии за доставку
        return_commission: Информация о комиссии за возврат
        commission_ratio: Процент комиссии
        seller_price_per_instance: Цена продавца за экземпляр
        order: Информация об отправлении
        legal_entity_document: Документ юридического лица
    """
    row_number: Optional[int] = Field(
        None, description="Номер строки в отчёте."
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
    order: Optional[FinanceRealizationPostingOrder] = Field(
        None, description="Информация об отправлении."
    )
    legal_entity_document: Optional[FinanceRealizationPostingDocument] = Field(
        None, description="Документ юридического лица."
    )


class FinanceRealizationPostingResponse(BaseModel):
    """Ответ с отчётом о реализации товаров по отправлениям.

    Attributes:
        header: Заголовок отчёта
        rows: Строки отчёта по товарам
    """
    header: Optional[FinanceRealizationHeader] = Field(
        None, description="Заголовок отчёта."
    )
    rows: Optional[list[FinanceRealizationPostingRow]] = Field(
        None, description="Строки отчёта по товарам."
    )
