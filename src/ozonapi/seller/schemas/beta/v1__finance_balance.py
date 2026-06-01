"""Схемы метода finance_balance (отчёт о балансе, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceBalanceMoney(BaseModel):
    """Денежное значение отчёта о балансе.

    Attributes:
        currency_code: Код валюты
        value: Значение
    """
    currency_code: Optional[str] = Field(None, description="Код валюты.")
    value: Optional[float] = Field(None, description="Значение.")


class FinanceBalanceRequest(BaseModel):
    """Параметры запроса отчёта о балансе.

    Attributes:
        date_from: Начало периода в формате YYYY-MM-DD
        date_to: Конец периода в формате YYYY-MM-DD
    """
    date_from: Optional[str] = Field(
        None, description="Начало периода в формате YYYY-MM-DD."
    )
    date_to: Optional[str] = Field(
        None, description="Конец периода в формате YYYY-MM-DD."
    )


class FinanceBalanceCashflowDetails(BaseModel):
    """Детализация денежного потока.

    Attributes:
        partner_programs: Партнёрские программы
        points_for_discounts: Баллы за скидки
        revenue: Выручка
    """
    partner_programs: Optional[FinanceBalanceMoney] = Field(
        None, description="Партнёрские программы."
    )
    points_for_discounts: Optional[str] = Field(None, description="Баллы за скидки.")
    revenue: Optional[FinanceBalanceMoney] = Field(None, description="Выручка.")


class FinanceBalanceCashflow(BaseModel):
    """Денежный поток (продажи или возвраты).

    Attributes:
        amount: Сумма
        amount_details: Детализация суммы
        fee: Комиссия
    """
    amount: Optional[FinanceBalanceMoney] = Field(None, description="Сумма.")
    amount_details: Optional[FinanceBalanceCashflowDetails] = Field(
        None, description="Детализация суммы."
    )
    fee: Optional[FinanceBalanceMoney] = Field(None, description="Комиссия.")


class FinanceBalanceService(BaseModel):
    """Услуга в денежном потоке.

    Attributes:
        amount: Сумма
        name: Название услуги
    """
    amount: Optional[FinanceBalanceMoney] = Field(None, description="Сумма.")
    name: Optional[str] = Field(None, description="Название услуги.")


class FinanceBalanceCashflows(BaseModel):
    """Денежные потоки отчёта о балансе.

    Attributes:
        returns: Возвраты
        sales: Продажи
        services: Услуги
    """
    returns: Optional[FinanceBalanceCashflow] = Field(None, description="Возвраты.")
    sales: Optional[FinanceBalanceCashflow] = Field(None, description="Продажи.")
    services: Optional[list[FinanceBalanceService]] = Field(
        None, description="Услуги."
    )


class FinanceBalanceTotal(BaseModel):
    """Итоговые значения отчёта о балансе.

    Attributes:
        accrued: Начислено
        closing_balance: Баланс на конец периода
        opening_balance: Баланс на начало периода
        payments: Выплаты
    """
    accrued: Optional[FinanceBalanceMoney] = Field(None, description="Начислено.")
    closing_balance: Optional[FinanceBalanceMoney] = Field(
        None, description="Баланс на конец периода."
    )
    opening_balance: Optional[FinanceBalanceMoney] = Field(
        None, description="Баланс на начало периода."
    )
    payments: Optional[list[FinanceBalanceMoney]] = Field(
        None, description="Выплаты."
    )


class FinanceBalanceResponse(BaseModel):
    """Ответ с отчётом о балансе.

    Attributes:
        cashflows: Денежные потоки
        total: Итоговые значения
    """
    cashflows: Optional[FinanceBalanceCashflows] = Field(
        None, description="Денежные потоки."
    )
    total: Optional[FinanceBalanceTotal] = Field(
        None, description="Итоговые значения."
    )
