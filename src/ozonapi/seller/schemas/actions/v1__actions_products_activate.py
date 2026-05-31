"""https://docs.ozon.ru/api/seller/#operation/ActionsProductsActivate"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import ActionsProductsChangeResult


class ActionsProductsActivateProduct(BaseModel):
    """Товар для добавления в акцию.

    Attributes:
        product_id: Идентификатор товара
        action_price: Цена товара по акции
        stock: Количество товара для акции типа «Скидка на сток»
    """

    product_id: int = Field(
        ..., description="Идентификатор товара."
    )
    action_price: float = Field(
        ..., description="Цена товара по акции."
    )
    stock: Optional[int] = Field(
        None, description="Количество товара для акции типа «Скидка на сток»."
    )


class ActionsProductsActivateRequest(BaseModel):
    """Схема запроса на добавление товаров в акцию.

    Attributes:
        action_id: Идентификатор акции
        products: Список товаров для добавления в акцию
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )
    products: list[ActionsProductsActivateProduct] = Field(
        ..., description="Список товаров для добавления в акцию.",
        min_length=1
    )


class ActionsProductsActivateResponse(BaseModel):
    """Схема ответа на добавление товаров в акцию.

    Attributes:
        result: Результат добавления товаров в акцию
    """

    result: Optional[ActionsProductsChangeResult] = Field(
        None, description="Результат добавления товаров в акцию."
    )
