"""https://docs.ozon.ru/api/seller/#operation/pricing_ids"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyIdsByProductIdsRequest(BaseModel):
    """Схема запроса на получение идентификаторов стратегий по идентификаторам товаров.

    Attributes:
        product_id: Список идентификаторов товаров в системе Ozon
    """

    product_id: list[str] = Field(
        ...,
        description="Список идентификаторов товаров в системе Ozon — product_id.",
    )


class StrategyProductStrategyItem(BaseModel):
    """Связь товара со стратегией ценообразования.

    Attributes:
        product_id: Идентификатор товара в системе Ozon
        strategy_id: Идентификатор стратегии, в которую добавлен товар
    """

    product_id: Optional[int] = Field(
        None,
        description="Идентификатор товара в системе Ozon — product_id.",
    )
    strategy_id: Optional[str] = Field(
        None,
        description="Идентификатор стратегии, в которую добавлен товар.",
    )


class StrategyIdsByProductIdsResult(BaseModel):
    """Результат запроса идентификаторов стратегий по товарам.

    Attributes:
        products_info: Список связей товаров со стратегиями
    """

    products_info: Optional[list[StrategyProductStrategyItem]] = Field(
        None,
        description="Список связей товаров со стратегиями ценообразования.",
    )


class StrategyIdsByProductIdsResponse(BaseModel):
    """Схема ответа на запрос идентификаторов стратегий по идентификаторам товаров.

    Attributes:
        result: Результат с информацией о стратегиях товаров
    """

    result: Optional[StrategyIdsByProductIdsResult] = Field(
        None,
        description="Результат с информацией о стратегиях товаров.",
    )
