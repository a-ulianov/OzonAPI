"""https://docs.ozon.ru/api/seller/#operation/pricing_items-add"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import StrategyProductError


class StrategyProductsAddRequest(BaseModel):
    """Схема запроса на добавление товаров в стратегию ценообразования.

    Attributes:
        product_id: Список идентификаторов товаров в системе Ozon
        strategy_id: Идентификатор стратегии
    """

    product_id: list[str] = Field(
        ...,
        description="Список идентификаторов товаров в системе Ozon — product_id.",
    )
    strategy_id: str = Field(
        ...,
        description="Идентификатор стратегии.",
    )


class StrategyProductsAddResult(BaseModel):
    """Результат добавления товаров в стратегию ценообразования.

    Attributes:
        errors: Список ошибок по товарам
        failed_product_count: Количество товаров с ошибками
    """

    errors: Optional[list[StrategyProductError]] = Field(
        None,
        description="Список ошибок по товарам, которые не удалось добавить.",
    )
    failed_product_count: Optional[int] = Field(
        None,
        description="Количество товаров с ошибками.",
    )


class StrategyProductsAddResponse(BaseModel):
    """Схема ответа на запрос добавления товаров в стратегию ценообразования.

    Attributes:
        result: Результат добавления товаров
    """

    result: Optional[StrategyProductsAddResult] = Field(
        None,
        description="Результат добавления товаров в стратегию.",
    )
