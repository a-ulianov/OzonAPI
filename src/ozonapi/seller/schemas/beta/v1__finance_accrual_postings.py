"""Схемы метода finance_accrual_postings (начисления по отправлениям, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import BetaMoneyAmount


class FinanceAccrualPostingsRequest(BaseModel):
    """Параметры запроса начислений по отправлениям.

    Attributes:
        posting_numbers: Номера отправлений
    """
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )


class FinanceAccrual(BaseModel):
    """Начисление по товару.

    Attributes:
        accrual_date: Дата начисления
        accrued: Начисленная сумма
        quantity: Количество товара
        seller_price: Цена продавца
        sku: Идентификатор товара в системе Ozon — SKU
        type_id: Идентификатор типа начисления
    """
    accrual_date: Optional[str] = Field(None, description="Дата начисления.")
    accrued: Optional[BetaMoneyAmount] = Field(None, description="Начисленная сумма.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    seller_price: Optional[BetaMoneyAmount] = Field(None, description="Цена продавца.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    type_id: Optional[int] = Field(None, description="Идентификатор типа начисления.")


class FinanceAccrualPosting(BaseModel):
    """Начисления по отправлению.

    Attributes:
        accruals: Начисления
        posting_number: Номер отправления
    """
    accruals: Optional[list[FinanceAccrual]] = Field(None, description="Начисления.")
    posting_number: Optional[str] = Field(None, description="Номер отправления.")


class FinanceAccrualPostingsResponse(BaseModel):
    """Ответ с начислениями по отправлениям.

    Attributes:
        posting_accruals: Начисления по отправлениям
    """
    posting_accruals: Optional[list[FinanceAccrualPosting]] = Field(
        None, description="Начисления по отправлениям."
    )
