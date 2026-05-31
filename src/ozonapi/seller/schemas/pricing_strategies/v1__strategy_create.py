"""https://docs.ozon.ru/api/seller/#operation/pricing_create"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import StrategyCompetitor


class StrategyCreateRequest(BaseModel):
    """Схема запроса на создание стратегии ценообразования.

    Attributes:
        competitors: Список конкурентов и коэффициентов
        strategy_name: Название стратегии
    """

    competitors: list[StrategyCompetitor] = Field(
        ...,
        description="Список конкурентов с коэффициентами для стратегии ценообразования.",
    )
    strategy_name: str = Field(
        ...,
        description="Название стратегии.",
    )


class StrategyCreateResult(BaseModel):
    """Внутренний объект результата создания стратегии.

    Attributes:
        strategy_id: Идентификатор созданной стратегии
    """

    strategy_id: Optional[str] = Field(
        None,
        description="Идентификатор созданной стратегии.",
    )


class StrategyCreateResponse(BaseModel):
    """Схема ответа на запрос создания стратегии ценообразования.

    Attributes:
        result: Результат с идентификатором созданной стратегии
    """

    result: Optional[StrategyCreateResult] = Field(
        None,
        description="Результат с идентификатором созданной стратегии.",
    )
