"""Базовые (переиспользуемые) модели для методов раздела «Акции продавца»."""
from typing import Optional, Union

from pydantic import BaseModel, Field


class SellerActionDiscountLevel(BaseModel):
    """Уровень скидки для акции «Многоуровневая скидка от суммы».

    Attributes:
        discount_value: Размер скидки на уровне
        order_amount: Сумма заказа, с которой начинает действовать уровень
    """

    discount_value: float = Field(
        ..., description="Размер скидки на уровне."
    )
    order_amount: float = Field(
        ..., description="Сумма заказа, с которой начинает действовать уровень скидки."
    )


class SellerActionProduct(BaseModel):
    """Товар, доступный для акции продавца или участвующий в ней.

    Attributes:
        action_price: Цена товара по акции
        base_price: Базовая цена товара
        currency: Валюта цен
        discount_percent: Процент скидки в акции
        is_active: Участвует ли товар в акции
        min_seller_price: Минимальная цена продавца
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        price: Текущая цена товара
        product_id: Идентификатор товара в системе Ozon — product_id
        quant_size: Размер кванта
        quant_type: Тип кванта
        sku: Список SKU товара
    """

    action_price: Optional[float] = Field(
        None, description="Цена товара по акции."
    )
    base_price: Optional[float] = Field(
        None, description="Базовая цена товара."
    )
    currency: Optional[str] = Field(
        None, description="Валюта цен."
    )
    discount_percent: Optional[float] = Field(
        None, description="Процент скидки в акции."
    )
    is_active: Optional[bool] = Field(
        None, description="Участвует ли товар в акции."
    )
    min_seller_price: Optional[float] = Field(
        None, description="Минимальная цена продавца."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[float] = Field(
        None, description="Текущая цена товара."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    quant_size: Optional[int] = Field(
        None, description="Размер кванта."
    )
    quant_type: Optional[str] = Field(
        None, description="Тип кванта: `UNSPECIFIED`, `BOX`, `PALLET` или `GENERAL`."
    )
    sku: Optional[list[Union[int, str]]] = Field(
        None, description="Список SKU товара. По данным живого API возвращаются числа "
                          "(swagger ошибочно объявляет строки)."
    )
