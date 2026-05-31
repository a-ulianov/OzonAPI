"""https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceCashFlowStatementList"""
from typing import Any, Optional

from pydantic import BaseModel, Field


class FinanceCashFlowPeriod(BaseModel):
    """Период финансового отчёта.

    Attributes:
        from_: Дата начала периода (сериализуется как `from`)
        to: Дата окончания периода
    """
    model_config = {'populate_by_name': True}

    from_: str = Field(
        ..., alias="from", description="Дата, с которой рассчитывается отчёт."
    )
    to: str = Field(
        ..., description="Дата, по которую рассчитывается отчёт."
    )


class FinanceCashFlowStatementListRequest(BaseModel):
    """Описывает схему запроса на получение финансового отчёта.

    Attributes:
        date: Период отчёта
        page: Номер страницы
        page_size: Количество элементов на странице
        with_details: Признак добавления детализации
    """
    date: FinanceCashFlowPeriod = Field(
        ..., description="Период отчёта."
    )
    page: int = Field(
        ..., description="Номер страницы, возвращаемой в запросе."
    )
    page_size: int = Field(
        ..., description="Количество элементов на странице."
    )
    with_details: Optional[bool] = Field(
        None, description="`true`, если нужно добавить детализацию."
    )


class FinanceCashFlowResponsePeriod(BaseModel):
    """Период отчёта в ответе.

    Attributes:
        id: Идентификатор
        begin: Начало периода
        end: Конец периода
    """
    id: Optional[int] = Field(
        None, description="Идентификатор."
    )
    begin: Optional[str] = Field(
        None, description="Начало периода."
    )
    end: Optional[str] = Field(
        None, description="Конец периода."
    )


class FinanceCashFlow(BaseModel):
    """Финансовый отчёт за период.

    Attributes:
        period: Период отчёта
        orders_amount: Сумма цен реализованных товаров
        returns_amount: Сумма цен возвращённых товаров
        commission_amount: Комиссия Ozon за реализацию товаров
        services_amount: Сумма дополнительных услуг
        item_delivery_and_return_amount: Сумма услуг логистики
        currency_code: Код валюты
    """
    period: Optional[FinanceCashFlowResponsePeriod] = Field(
        None, description="Период отчёта."
    )
    orders_amount: Optional[float] = Field(
        None, description="Сумма цен реализованных товаров."
    )
    returns_amount: Optional[float] = Field(
        None, description="Сумма цен возвращённых товаров."
    )
    commission_amount: Optional[float] = Field(
        None, description="Комиссия Ozon за реализацию товаров."
    )
    services_amount: Optional[float] = Field(
        None, description="Сумма дополнительных услуг."
    )
    item_delivery_and_return_amount: Optional[float] = Field(
        None, description="Сумма услуг логистики."
    )
    currency_code: Optional[str] = Field(
        None, description="Код валюты, в которой рассчитываются суммы."
    )


class FinanceCashFlowStatementListResult(BaseModel):
    """Результат запроса финансового отчёта.

    Attributes:
        cash_flows: Список отчётов
        details: Детализация
        page_count: Количество страниц
    """
    cash_flows: Optional[list[FinanceCashFlow]] = Field(
        None, description="Список отчётов."
    )
    details: Optional[list[Any]] = Field(
        None, description="Детализация (если запрошена через `with_details`)."
    )
    page_count: Optional[int] = Field(
        None, description="Количество страниц."
    )


class FinanceCashFlowStatementListResponse(BaseModel):
    """Описывает схему ответа на запрос финансового отчёта.

    Attributes:
        result: Результат запроса
    """
    result: Optional[FinanceCashFlowStatementListResult] = Field(
        None, description="Результат запроса."
    )
