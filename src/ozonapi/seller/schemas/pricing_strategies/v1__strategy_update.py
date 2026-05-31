"""https://docs.ozon.ru/api/seller/#operation/pricing_update"""
from pydantic import BaseModel, Field

from .base import StrategyCompetitor


class StrategyUpdateRequest(BaseModel):
    """Схема запроса на обновление стратегии ценообразования.

    Attributes:
        competitors: Список конкурентов и коэффициентов
        strategy_id: Идентификатор стратегии
        strategy_name: Новое название стратегии
    """

    competitors: list[StrategyCompetitor] = Field(
        ...,
        description="Список конкурентов с коэффициентами для стратегии ценообразования.",
    )
    strategy_id: str = Field(
        ...,
        description="Идентификатор стратегии.",
    )
    strategy_name: str = Field(
        ...,
        description="Название стратегии.",
    )


class StrategyUpdateResponse(BaseModel):
    """Схема ответа на запрос обновления стратегии ценообразования.

    Attributes:
        None — сервер возвращает пустой объект при успехе
    """

    pass
