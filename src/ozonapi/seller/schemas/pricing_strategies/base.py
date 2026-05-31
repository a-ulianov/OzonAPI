"""Базовые модели для методов раздела Стратегии ценообразования."""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyCompetitor(BaseModel):
    """Конкурент в стратегии ценообразования.

    Attributes:
        coefficient: Коэффициент умножения минимальной цены конкурента
        competitor_id: Идентификатор конкурента
    """

    coefficient: float = Field(
        ...,
        description="Коэффициент, на который умножается минимальная цена среди конкурентов. "
                    "Допустимый диапазон — от 0.5 до 1.2.",
        ge=0.5,
        le=1.2,
    )
    competitor_id: int = Field(
        ...,
        description="Идентификатор конкурента.",
    )


class StrategyProductError(BaseModel):
    """Ошибка при добавлении товара в стратегию ценообразования.

    Attributes:
        code: Код ошибки
        error: Текст ошибки
        product_id: Идентификатор товара в системе Ozon
    """

    code: Optional[str] = Field(
        None,
        description="Код ошибки.",
    )
    error: Optional[str] = Field(
        None,
        description="Текст ошибки.",
    )
    product_id: Optional[int] = Field(
        None,
        description="Идентификатор товара в системе Ozon — product_id.",
    )
