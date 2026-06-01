"""Схемы метода finance_accrual_by_day (начисления за день, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import BetaMoneyAmount


class FinanceAccrualByDayRequest(BaseModel):
    """Параметры запроса начислений за день.

    Attributes:
        date: Дата начислений
        last_id: Идентификатор последнего значения для пагинации
    """
    date: Optional[str] = Field(None, description="Дата начислений.")
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )


class FinanceAccrualByDayFee(BaseModel):
    """Начисление по типу.

    Attributes:
        accrued: Начисленная сумма
        type_id: Идентификатор типа начисления
    """
    accrued: Optional[BetaMoneyAmount] = Field(None, description="Начисленная сумма.")
    type_id: Optional[int] = Field(None, description="Идентификатор типа начисления.")


class FinanceAccrualByDayItemFee(BaseModel):
    """Начисления по товару.

    Attributes:
        fees: Начисления
        sku: Идентификатор товара в системе Ozon — SKU
    """
    fees: Optional[list[FinanceAccrualByDayFee]] = Field(None, description="Начисления.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class FinanceAccrualByDayItemFees(BaseModel):
    """Начисления по товарам.

    Attributes:
        fees: Начисления по товарам
    """
    fees: Optional[list[FinanceAccrualByDayItemFee]] = Field(
        None, description="Начисления по товарам."
    )


class FinanceAccrualByDayProductCommission(BaseModel):
    """Комиссия по товару.

    Attributes:
        bonus: Бонусы
        coinvestment: Софинансирование
        commission: Комиссия
        commission_ratio: Ставка комиссии
        sale_amount: Сумма продажи
        sale_commission: Комиссия за продажу
        sale_price: Цена продажи
        seller_price: Цена продавца
    """
    bonus: Optional[BetaMoneyAmount] = Field(None, description="Бонусы.")
    coinvestment: Optional[BetaMoneyAmount] = Field(None, description="Софинансирование.")
    commission: Optional[BetaMoneyAmount] = Field(None, description="Комиссия.")
    commission_ratio: Optional[str] = Field(None, description="Ставка комиссии.")
    sale_amount: Optional[BetaMoneyAmount] = Field(None, description="Сумма продажи.")
    sale_commission: Optional[BetaMoneyAmount] = Field(
        None, description="Комиссия за продажу."
    )
    sale_price: Optional[BetaMoneyAmount] = Field(None, description="Цена продажи.")
    seller_price: Optional[BetaMoneyAmount] = Field(None, description="Цена продавца.")


class FinanceAccrualByDayProductDelivery(BaseModel):
    """Начисления за доставку товара.

    Attributes:
        services: Услуги доставки
        total_accrued: Итоговое начисление
    """
    services: Optional[list[FinanceAccrualByDayFee]] = Field(
        None, description="Услуги доставки."
    )
    total_accrued: Optional[BetaMoneyAmount] = Field(
        None, description="Итоговое начисление."
    )


class FinanceAccrualByDayProduct(BaseModel):
    """Товар в начислении.

    Attributes:
        commission: Комиссия по товару
        delivery: Начисления за доставку
        sku: Идентификатор товара в системе Ozon — SKU
    """
    commission: Optional[FinanceAccrualByDayProductCommission] = Field(
        None, description="Комиссия по товару."
    )
    delivery: Optional[FinanceAccrualByDayProductDelivery] = Field(
        None, description="Начисления за доставку."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class FinanceAccrualByDayPosting(BaseModel):
    """Отправление в начислении.

    Attributes:
        delivery_schema: Схема доставки
        delivery_speed: Скорость доставки
        products: Товары в отправлении
    """
    delivery_schema: Optional[str] = Field(None, description="Схема доставки.")
    delivery_speed: Optional[int] = Field(None, description="Скорость доставки.")
    products: Optional[list[FinanceAccrualByDayProduct]] = Field(
        None, description="Товары в отправлении."
    )


class FinanceAccrualByDayItem(BaseModel):
    """Начисление за день.

    Attributes:
        accrued_category: Категория начисления
        date: Дата начисления
        item_fees: Начисления по товарам
        non_item_fee: Начисление, не связанное с товаром
        posting: Отправление
        total_amount: Итоговая сумма
        type_id: Идентификатор типа начисления
        unit_number: Номер документа
    """
    accrued_category: Optional[str] = Field(None, description="Категория начисления.")
    date: Optional[str] = Field(None, description="Дата начисления.")
    item_fees: Optional[FinanceAccrualByDayItemFees] = Field(
        None, description="Начисления по товарам."
    )
    non_item_fee: Optional[FinanceAccrualByDayFee] = Field(
        None, description="Начисление, не связанное с товаром."
    )
    posting: Optional[FinanceAccrualByDayPosting] = Field(
        None, description="Отправление."
    )
    total_amount: Optional[BetaMoneyAmount] = Field(None, description="Итоговая сумма.")
    type_id: Optional[int] = Field(None, description="Идентификатор типа начисления.")
    unit_number: Optional[str] = Field(None, description="Номер документа.")


class FinanceAccrualByDayResponse(BaseModel):
    """Ответ с начислениями за день.

    Attributes:
        accruals: Начисления
        last_id: Идентификатор последнего значения для пагинации
    """
    accruals: Optional[list[FinanceAccrualByDayItem]] = Field(
        None, description="Начисления."
    )
    last_id: Optional[str] = Field(
        None, description="Идентификатор последнего значения для пагинации."
    )
