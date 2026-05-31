"""https://docs.ozon.ru/api/seller/#operation/pricing_info"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import StrategyCompetitor


class StrategyInfoRequest(BaseModel):
    """Схема запроса на получение информации о стратегии ценообразования.

    Attributes:
        strategy_id: Идентификатор стратегии
    """

    strategy_id: str = Field(
        ...,
        description="Идентификатор стратегии.",
    )


class StrategyInfoResult(BaseModel):
    """Детальная информация о стратегии ценообразования.

    Attributes:
        competitors: Список конкурентов с коэффициентами
        enabled: Статус стратегии (включена или отключена)
        name: Название стратегии
        type: Тип стратегии
        update_type: Тип последнего изменения стратегии
    """

    competitors: Optional[list[StrategyCompetitor]] = Field(
        None,
        description="Список конкурентов с коэффициентами.",
    )
    enabled: Optional[bool] = Field(
        None,
        description="Статус стратегии: true — включена, false — отключена.",
    )
    name: Optional[str] = Field(
        None,
        description="Название стратегии.",
    )
    type: Optional[str] = Field(
        None,
        description="Тип стратегии: MIN_EXT_PRICE — системная, COMP_PRICE — пользовательская.",
    )
    update_type: Optional[str] = Field(
        None,
        description="Тип последнего изменения стратегии: strategyEnabled, strategyDisabled, "
                    "strategyChanged, strategyCreated, strategyItemsListChanged.",
    )


class StrategyInfoResponse(BaseModel):
    """Схема ответа на запрос информации о стратегии ценообразования.

    Attributes:
        result: Детальная информация о стратегии
    """

    result: Optional[StrategyInfoResult] = Field(
        None,
        description="Детальная информация о стратегии.",
    )
