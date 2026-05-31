"""Схемы метода finance_transaction_list (список транзакций, v3)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinancePeriod


class FinanceTransactionListFilter(BaseModel):
    """Фильтр списка транзакций.

    Attributes:
        date: Период формирования отчёта
        operation_type: Типы операций
        posting_number: Номер отправления
        transaction_type: Тип начисления
    """
    date: Optional[FinancePeriod] = Field(
        None, description="Период формирования отчёта."
    )
    operation_type: Optional[list[str]] = Field(
        None, description="Типы операций."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    transaction_type: Optional[str] = Field(
        None, description="Тип начисления."
    )


class FinanceTransactionListRequest(BaseModel):
    """Параметры запроса списка транзакций.

    Attributes:
        filter: Фильтр транзакций
        page: Номер страницы
        page_size: Количество элементов на странице
    """
    filter: Optional[FinanceTransactionListFilter] = Field(
        None, description="Фильтр транзакций."
    )
    page: int = Field(..., description="Номер страницы.")
    page_size: int = Field(..., description="Количество элементов на странице.")


class FinanceTransactionItem(BaseModel):
    """Информация о товаре в транзакции.

    Attributes:
        name: Название товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    name: Optional[str] = Field(None, description="Название товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class FinanceTransactionPosting(BaseModel):
    """Информация об отправлении в транзакции.

    Attributes:
        delivery_schema: Схема доставки
        order_date: Дата принятия отправления в обработку
        posting_number: Номер отправления
        warehouse_id: Идентификатор склада
    """
    delivery_schema: Optional[str] = Field(
        None, description="Схема доставки."
    )
    order_date: Optional[str] = Field(
        None, description="Дата принятия отправления в обработку."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )


class FinanceTransactionService(BaseModel):
    """Информация об услуге в транзакции.

    Attributes:
        name: Название услуги
        price: Цена
    """
    name: Optional[str] = Field(None, description="Название услуги.")
    price: Optional[float] = Field(None, description="Цена.")


class FinanceTransactionOperation(BaseModel):
    """Информация об операции.

    Attributes:
        accruals_for_sale: Стоимость товаров с учётом скидок продавца
        amount: Итоговая сумма операции
        delivery_charge: Стоимость доставки для начислений
        items: Информация о товарах
        operation_date: Дата операции
        operation_id: Идентификатор операции
        operation_type: Тип операции
        operation_type_name: Название типа операции
        posting: Информация об отправлении
        return_delivery_charge: Плата за возвраты и отмены
        sale_commission: Комиссия за продажу или возврат
        services: Дополнительные услуги
        type: Тип начисления
    """
    accruals_for_sale: Optional[float] = Field(
        None, description="Стоимость товаров с учётом скидок продавца."
    )
    amount: Optional[float] = Field(
        None, description="Итоговая сумма операции."
    )
    delivery_charge: Optional[float] = Field(
        None, description="Стоимость доставки для начислений."
    )
    items: Optional[list[FinanceTransactionItem]] = Field(
        None, description="Информация о товарах."
    )
    operation_date: Optional[str] = Field(
        None, description="Дата операции."
    )
    operation_id: Optional[int] = Field(
        None, description="Идентификатор операции."
    )
    operation_type: Optional[str] = Field(
        None, description="Тип операции."
    )
    operation_type_name: Optional[str] = Field(
        None, description="Название типа операции."
    )
    posting: Optional[FinanceTransactionPosting] = Field(
        None, description="Информация об отправлении."
    )
    return_delivery_charge: Optional[float] = Field(
        None, description="Плата за возвраты и отмены."
    )
    sale_commission: Optional[float] = Field(
        None, description="Комиссия за продажу или возврат."
    )
    services: Optional[list[FinanceTransactionService]] = Field(
        None, description="Дополнительные услуги."
    )
    type: Optional[str] = Field(
        None, description="Тип начисления."
    )


class FinanceTransactionListResult(BaseModel):
    """Содержимое ответа со списком транзакций.

    Attributes:
        operations: Информация об операциях
        page_count: Количество страниц
        row_count: Количество транзакций на всех страницах
    """
    operations: Optional[list[FinanceTransactionOperation]] = Field(
        None, description="Информация об операциях."
    )
    page_count: Optional[int] = Field(
        None, description="Количество страниц."
    )
    row_count: Optional[int] = Field(
        None, description="Количество транзакций на всех страницах."
    )


class FinanceTransactionListResponse(BaseModel):
    """Ответ со списком транзакций.

    Attributes:
        result: Содержимое ответа
    """
    result: Optional[FinanceTransactionListResult] = Field(
        None, description="Содержимое ответа."
    )
