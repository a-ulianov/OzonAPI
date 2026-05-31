"""https://docs.ozon.ru/api/seller/#operation/pricing_items-info"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyProductInfoRequest(BaseModel):
    """Схема запроса на получение цены товара у конкурента.

    Attributes:
        product_id: Идентификатор товара в системе Ozon
    """

    product_id: int = Field(
        ...,
        description="Идентификатор товара в системе Ozon — product_id.",
    )


class StrategyProductInfoResult(BaseModel):
    """Информация о цене товара по стратегии ценообразования.

    Attributes:
        strategy_id: Идентификатор стратегии
        is_enabled: Участвует ли товар в стратегии ценообразования
        strategy_product_price: Цена по стратегии
        price_downloaded_at: Дата установки цены по стратегии
        strategy_competitor_id: Идентификатор конкурента (устарело)
        strategy_competitor_product_url: Ссылка на товар конкурента
    """

    strategy_id: Optional[str] = Field(
        None,
        description="Идентификатор стратегии.",
    )
    is_enabled: Optional[bool] = Field(
        None,
        description="true, если товар участвует в стратегии ценообразования.",
    )
    strategy_product_price: Optional[int] = Field(
        None,
        description="Цена по стратегии.",
    )
    price_downloaded_at: Optional[str] = Field(
        None,
        description="Дата установки цены по стратегии.",
    )
    strategy_competitor_id: Optional[int] = Field(
        None,
        description="Идентификатор конкурента. Устаревшее поле.",
    )
    strategy_competitor_product_url: Optional[str] = Field(
        None,
        description="Ссылка на товар конкурента.",
    )


class StrategyProductInfoResponse(BaseModel):
    """Схема ответа на запрос цены товара у конкурента.

    Attributes:
        result: Информация о цене товара по стратегии
    """

    result: Optional[StrategyProductInfoResult] = Field(
        None,
        description="Информация о цене товара по стратегии.",
    )
