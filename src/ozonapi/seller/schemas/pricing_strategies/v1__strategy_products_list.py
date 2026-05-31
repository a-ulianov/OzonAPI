"""https://docs.ozon.ru/api/seller/#operation/pricing_items-list"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyProductsListRequest(BaseModel):
    """Схема запроса на получение списка товаров в стратегии ценообразования.

    Attributes:
        strategy_id: Идентификатор стратегии
    """

    strategy_id: str = Field(
        ...,
        description="Идентификатор стратегии.",
    )


class StrategyProductsListResult(BaseModel):
    """Результат запроса списка товаров в стратегии.

    Attributes:
        product_id: Список идентификаторов товаров в системе Ozon
    """

    product_id: Optional[list[str]] = Field(
        None,
        description="Список идентификаторов товаров в системе Ozon — product_id.",
    )


class StrategyProductsListResponse(BaseModel):
    """Схема ответа на запрос списка товаров в стратегии ценообразования.

    Attributes:
        result: Результат с идентификаторами товаров
    """

    result: Optional[StrategyProductsListResult] = Field(
        None,
        description="Результат с идентификаторами товаров в стратегии.",
    )
