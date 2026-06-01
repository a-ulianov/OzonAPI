"""https://docs.ozon.ru/api/seller/#operation/FinanceAPI_GetRealizationByDayReportV1"""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceRealizationByDayRequest(BaseModel):
    """Схема запроса отчёта о реализации товаров за день (Premium).

    Attributes:
        day: День месяца
        month: Месяц
        year: Год
    """

    day: int = Field(
        ..., description="День месяца, за который формируется отчёт."
    )
    month: int = Field(
        ..., description="Месяц, за который формируется отчёт."
    )
    year: int = Field(
        ..., description="Год, за который формируется отчёт."
    )


class FinanceRealizationByDayItem(BaseModel):
    """Товар в строке отчёта о реализации за день.

    Attributes:
        sku: SKU товара
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        barcode: Штрихкод товара
    """

    sku: Optional[int] = Field(
        None, description="SKU товара."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    barcode: Optional[str] = Field(
        None, description="Штрихкод товара."
    )


class FinanceRealizationByDayCommission(BaseModel):
    """Комиссии и начисления по товару в отчёте о реализации за день.

    Attributes:
        amount: Сумма начисления
        bonus: Баллы за скидки
        commission: Комиссия
        compensation: Компенсация
        price_per_instance: Цена за единицу товара
        quantity: Количество товаров
        standard_fee: Стандартная комиссия
        bank_coinvestment: Софинансирование банка
        stars: Софинансирование «Звёзды»
        pick_up_point_coinvestment: Софинансирование пункта выдачи
        total: Итоговая сумма
    """

    amount: Optional[float] = Field(
        None, description="Сумма начисления."
    )
    bonus: Optional[float] = Field(
        None, description="Баллы за скидки."
    )
    commission: Optional[float] = Field(
        None, description="Комиссия."
    )
    compensation: Optional[float] = Field(
        None, description="Компенсация."
    )
    price_per_instance: Optional[float] = Field(
        None, description="Цена за единицу товара."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товаров."
    )
    standard_fee: Optional[float] = Field(
        None, description="Стандартная комиссия."
    )
    bank_coinvestment: Optional[float] = Field(
        None, description="Софинансирование банка."
    )
    stars: Optional[float] = Field(
        None, description="Софинансирование «Звёзды»."
    )
    pick_up_point_coinvestment: Optional[float] = Field(
        None, description="Софинансирование пункта выдачи."
    )
    total: Optional[float] = Field(
        None, description="Итоговая сумма."
    )


class FinanceRealizationByDayRow(BaseModel):
    """Строка отчёта о реализации товаров за день.

    Attributes:
        row_number: Номер строки
        item: Товар
        delivery_commission: Начисления по доставленным товарам
        return_commission: Начисления по возвращённым товарам
        commission_ratio: Доля комиссии
        seller_price_per_instance: Цена продавца за единицу товара
    """

    row_number: Optional[int] = Field(
        None, alias="rowNumber", description="Номер строки."
    )
    item: Optional[FinanceRealizationByDayItem] = Field(
        None, description="Товар."
    )
    delivery_commission: Optional[FinanceRealizationByDayCommission] = Field(
        None, description="Начисления по доставленным товарам."
    )
    return_commission: Optional[FinanceRealizationByDayCommission] = Field(
        None, description="Начисления по возвращённым товарам."
    )
    commission_ratio: Optional[float] = Field(
        None, description="Доля комиссии."
    )
    seller_price_per_instance: Optional[float] = Field(
        None, description="Цена продавца за единицу товара."
    )


class FinanceRealizationByDayResponse(BaseModel):
    """Схема ответа отчёта о реализации товаров за день.

    Attributes:
        rows: Строки отчёта о реализации
    """

    rows: list[FinanceRealizationByDayRow] = Field(
        default_factory=list, description="Строки отчёта о реализации."
    )
