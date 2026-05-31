"""Схемы метода finance_transaction_totals (суммы транзакций, v3)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FinancePeriod


class FinanceTransactionTotalsRequest(BaseModel):
    """Параметры запроса сумм транзакций.

    Attributes:
        date: Период формирования отчёта
        posting_number: Номер отправления
        transaction_type: Тип операции
    """
    date: Optional[FinancePeriod] = Field(
        None, description="Период формирования отчёта."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    transaction_type: Optional[str] = Field(
        None, description="Тип операции."
    )


class FinanceTransactionTotalsResult(BaseModel):
    """Содержимое ответа с суммами транзакций.

    Attributes:
        accruals_for_sale: Общая стоимость проданных товаров
        compensation_amount: Компенсации
        money_transfer: Начисления за доставку и возврат
        others_amount: Прочие начисления
        processing_and_delivery: Стоимость услуг обработки и доставки
        refunds_and_cancellations: Стоимость обратной магистрали
        sale_commission: Сумма комиссии за продажу
        services_amount: Стоимость дополнительных услуг
    """
    accruals_for_sale: Optional[float] = Field(
        None, description="Общая стоимость проданных товаров."
    )
    compensation_amount: Optional[float] = Field(
        None, description="Компенсации."
    )
    money_transfer: Optional[float] = Field(
        None, description="Начисления за доставку и возврат."
    )
    others_amount: Optional[float] = Field(
        None, description="Прочие начисления."
    )
    processing_and_delivery: Optional[float] = Field(
        None, description="Стоимость услуг обработки и доставки."
    )
    refunds_and_cancellations: Optional[float] = Field(
        None, description="Стоимость обратной магистрали."
    )
    sale_commission: Optional[float] = Field(
        None, description="Сумма комиссии за продажу."
    )
    services_amount: Optional[float] = Field(
        None, description="Стоимость дополнительных услуг."
    )


class FinanceTransactionTotalsResponse(BaseModel):
    """Ответ с суммами транзакций.

    Attributes:
        result: Содержимое ответа
    """
    result: Optional[FinanceTransactionTotalsResult] = Field(
        None, description="Содержимое ответа."
    )
