"""Общая модель комиссии в строке отчёта о реализации."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceCommission(BaseModel):
    """Комиссия (за доставку или возврат) в строке отчёта о реализации.

    Attributes:
        amount: Итоговая сумма
        bonus: Скидка за счёт Ozon
        commission: Комиссия за продажу
        compensation: Компенсация
        price_per_instance: Цена за экземпляр
        quantity: Количество
        standard_fee: Базовое вознаграждение Ozon
        bank_coinvestment: Доплата за счёт банковского софинансирования
        stars: Доплата за счёт Ozon.Звёзды
        pick_up_point_coinvestment: Доплата за счёт пунктов выдачи
        total: Итого к начислению
    """
    amount: Optional[float] = Field(
        None, description="Итоговая сумма."
    )
    bonus: Optional[float] = Field(
        None, description="Скидка за счёт Ozon."
    )
    commission: Optional[float] = Field(
        None, description="Комиссия за продажу."
    )
    compensation: Optional[float] = Field(
        None, description="Компенсация."
    )
    price_per_instance: Optional[float] = Field(
        None, description="Цена за экземпляр."
    )
    quantity: Optional[int] = Field(
        None, description="Количество."
    )
    standard_fee: Optional[float] = Field(
        None, description="Базовое вознаграждение Ozon."
    )
    bank_coinvestment: Optional[float] = Field(
        None, description="Доплата за счёт банковского софинансирования."
    )
    stars: Optional[float] = Field(
        None, description="Доплата за счёт Ozon.Звёзды."
    )
    pick_up_point_coinvestment: Optional[float] = Field(
        None, description="Доплата за счёт пунктов выдачи."
    )
    total: Optional[float] = Field(
        None, description="Итого к начислению."
    )
