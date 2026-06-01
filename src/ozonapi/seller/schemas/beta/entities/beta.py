"""Общие сущности бета-методов."""
from typing import Optional

from pydantic import BaseModel, Field


class BetaMoneyAmount(BaseModel):
    """Денежное значение.

    Attributes:
        amount: Сумма
        currency: Код валюты
    """
    amount: Optional[str] = Field(None, description="Сумма.")
    currency: Optional[str] = Field(None, description="Код валюты.")


class StairwayStep(BaseModel):
    """Ступень скидки от количества.

    Attributes:
        discount: Размер скидки в процентах
        quantity: Количество товара для применения скидки
        step: Номер ступени
    """
    discount: Optional[int] = Field(None, description="Размер скидки в процентах.")
    quantity: Optional[int] = Field(
        None, description="Количество товара для применения скидки."
    )
    step: Optional[int] = Field(None, description="Номер ступени.")


class Stairway(BaseModel):
    """Лестница скидок от количества.

    Attributes:
        steps: Ступени скидки
    """
    steps: Optional[list[StairwayStep]] = Field(None, description="Ступени скидки.")


class RemovalReturnsSummaryRow(BaseModel):
    """Строка отчёта по вывозу и утилизации.

    Attributes:
        barcode: Штрихкод товара
        box_barcode: Штрихкод коробки
        box_height: Высота коробки
        box_id: Идентификатор коробки
        box_length: Длина коробки
        box_state: Статус коробки
        box_volume: Объём коробки
        box_weight: Вес коробки
        box_width: Ширина коробки
        clearing_warehouse_name: Название склада оформления
        delivery_date: Дата доставки
        delivery_type: Тип доставки
        destination_warehouse_address: Адрес склада назначения
        destination_warehouse_name: Название склада назначения
        given_out_date: Дата выдачи
        is_auto_return: Признак автоматического возврата
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        preliminary_delivery_price: Предварительная стоимость доставки
        quant_count: Количество в кванте
        quantity_for_return: Количество к возврату
        return_created_at: Дата создания возврата
        return_id: Идентификатор возврата
        return_state: Статус возврата
        sku: Идентификатор товара в системе Ozon — SKU
        stock_type: Тип стока
        utilization_date: Дата утилизации
    """
    barcode: Optional[str] = Field(None, description="Штрихкод товара.")
    box_barcode: Optional[str] = Field(None, description="Штрихкод коробки.")
    box_height: Optional[float] = Field(None, description="Высота коробки.")
    box_id: Optional[int] = Field(None, description="Идентификатор коробки.")
    box_length: Optional[float] = Field(None, description="Длина коробки.")
    box_state: Optional[str] = Field(None, description="Статус коробки.")
    box_volume: Optional[float] = Field(None, description="Объём коробки.")
    box_weight: Optional[float] = Field(None, description="Вес коробки.")
    box_width: Optional[float] = Field(None, description="Ширина коробки.")
    clearing_warehouse_name: Optional[str] = Field(
        None, description="Название склада оформления."
    )
    delivery_date: Optional[str] = Field(None, description="Дата доставки.")
    delivery_type: Optional[str] = Field(None, description="Тип доставки.")
    destination_warehouse_address: Optional[str] = Field(
        None, description="Адрес склада назначения."
    )
    destination_warehouse_name: Optional[str] = Field(
        None, description="Название склада назначения."
    )
    given_out_date: Optional[str] = Field(None, description="Дата выдачи.")
    is_auto_return: Optional[bool] = Field(
        None, description="Признак автоматического возврата."
    )
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    preliminary_delivery_price: Optional[float] = Field(
        None, description="Предварительная стоимость доставки."
    )
    quant_count: Optional[int] = Field(None, description="Количество в кванте.")
    quantity_for_return: Optional[int] = Field(
        None, description="Количество к возврату."
    )
    return_created_at: Optional[str] = Field(None, description="Дата создания возврата.")
    return_id: Optional[int] = Field(None, description="Идентификатор возврата.")
    return_state: Optional[str] = Field(None, description="Статус возврата.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    stock_type: Optional[str] = Field(None, description="Тип стока.")
    utilization_date: Optional[str] = Field(None, description="Дата утилизации.")
