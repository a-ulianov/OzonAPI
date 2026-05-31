"""https://docs.ozon.ru/api/seller/#operation/Promos"""
from typing import Optional

from pydantic import BaseModel, Field


class ActionItem(BaseModel):
    """Акция Ozon, доступная продавцу.

    Attributes:
        id: Идентификатор акции
        title: Название акции
        action_type: Тип акции
        description: Описание акции
        date_start: Дата начала акции
        date_end: Дата окончания акции
        freeze_date: Дата заморозки акции
        with_targeting: Признак, что акция с целевой аудиторией
        order_amount: Сумма заказа
        discount_type: Тип скидки
        discount_value: Размер скидки
        potential_products_count: Количество товаров, доступных для акции
        participating_products_count: Количество товаров, участвующих в акции
        is_participating: Признак участия продавца в акции
        banned_products_count: Количество заблокированных товаров
        is_voucher_action: Признак, что для участия в акции нужен промокод
    """

    id: Optional[int] = Field(
        None, description="Идентификатор акции."
    )
    title: Optional[str] = Field(
        None, description="Название акции."
    )
    action_type: Optional[str] = Field(
        None, description="Тип акции."
    )
    description: Optional[str] = Field(
        None, description="Описание акции."
    )
    date_start: Optional[str] = Field(
        None, description="Дата начала акции."
    )
    date_end: Optional[str] = Field(
        None, description="Дата окончания акции."
    )
    freeze_date: Optional[str] = Field(
        None, description="Дата заморозки акции. После этой даты у товаров в акции "
                          "нельзя изменить цены и остатки."
    )
    with_targeting: Optional[bool] = Field(
        None, description="Признак, что акция с целевой аудиторией."
    )
    order_amount: Optional[float] = Field(
        None, description="Сумма заказа."
    )
    discount_type: Optional[str] = Field(
        None, description="Тип скидки."
    )
    discount_value: Optional[float] = Field(
        None, description="Размер скидки."
    )
    potential_products_count: Optional[int] = Field(
        None, description="Количество товаров, доступных для акции."
    )
    participating_products_count: Optional[int] = Field(
        None, description="Количество товаров, участвующих в акции."
    )
    is_participating: Optional[bool] = Field(
        None, description="Признак, что продавец участвует в акции."
    )
    banned_products_count: Optional[int] = Field(
        None, description="Количество заблокированных товаров."
    )
    is_voucher_action: Optional[bool] = Field(
        None, description="Признак, что для участия в акции нужен промокод."
    )


class ActionsResponse(BaseModel):
    """Схема ответа со списком доступных акций.

    Attributes:
        result: Список доступных акций
    """

    result: Optional[list[ActionItem]] = Field(
        None, description="Список доступных акций."
    )
