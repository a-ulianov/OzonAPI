"""Схемы метода finance_products_buyout (отчёт о выкупленных товарах, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceProductsBuyoutRequest(BaseModel):
    """Параметры запроса отчёта о выкупленных товарах.

    Attributes:
        date_from: Дата начала периода
        date_to: Дата конца периода
    """
    date_from: str = Field(..., description="Дата начала периода.")
    date_to: str = Field(..., description="Дата конца периода.")


class FinanceProductsBuyoutProduct(BaseModel):
    """Информация о выкупленном товаре.

    Attributes:
        amount: Сумма к начислению
        buyout_price: Цена выкупа товара с НДС
        deduction_by_category_percent: Скидка по категории в процентах
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        posting_number: Номер отправления
        quantity: Количество товара
        seller_price_per_instance: Цена продавца с учётом скидок
        sku: Идентификатор товара в системе Ozon — SKU
        vat_percent: Ставка НДС для товара
    """
    amount: Optional[float] = Field(
        None, description="Сумма к начислению."
    )
    buyout_price: Optional[float] = Field(
        None, description="Цена выкупа товара с НДС."
    )
    deduction_by_category_percent: Optional[float] = Field(
        None, description="Скидка по категории в процентах."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара."
    )
    seller_price_per_instance: Optional[float] = Field(
        None, description="Цена продавца с учётом скидок."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    vat_percent: Optional[int] = Field(
        None, description="Ставка НДС для товара."
    )


class FinanceProductsBuyoutResponse(BaseModel):
    """Ответ с отчётом о выкупленных товарах.

    Attributes:
        products: Список выкупленных товаров
    """
    products: Optional[list[FinanceProductsBuyoutProduct]] = Field(
        None, description="Список выкупленных товаров."
    )
