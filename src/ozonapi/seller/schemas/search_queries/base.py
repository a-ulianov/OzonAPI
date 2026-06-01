"""Базовые (переиспользуемые) модели раздела «Поисковые запросы» (Premium)."""
from typing import Optional

from pydantic import BaseModel, Field


class SearchQuery(BaseModel):
    """Метрики поискового запроса.

    Attributes:
        query: Текст поискового запроса
        client_count: Количество уникальных пользователей, сделавших запрос
        avg_price: Средняя цена товаров в выдаче по запросу
        add_to_cart: Количество добавлений товаров в корзину по запросу
        conversion_to_cart: Конверсия в добавление в корзину
        items_views: Количество показов товаров по запросу
        sellers_count: Количество продавцов в выдаче по запросу
    """

    query: Optional[str] = Field(
        None, description="Текст поискового запроса."
    )
    client_count: Optional[float] = Field(
        None, description="Количество уникальных пользователей, сделавших запрос."
    )
    avg_price: Optional[float] = Field(
        None, description="Средняя цена товаров в выдаче по запросу."
    )
    add_to_cart: Optional[float] = Field(
        None, description="Количество добавлений товаров в корзину по запросу."
    )
    conversion_to_cart: Optional[float] = Field(
        None, description="Конверсия в добавление в корзину."
    )
    items_views: Optional[float] = Field(
        None, description="Количество показов товаров по запросу."
    )
    sellers_count: Optional[float] = Field(
        None, description="Количество продавцов в выдаче по запросу."
    )
