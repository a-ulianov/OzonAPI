"""https://docs.ozon.ru/api/seller/#operation/pricing_status"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyStatusRequest(BaseModel):
    """Схема запроса на изменение статуса стратегии ценообразования.

    Attributes:
        strategy_id: Идентификатор стратегии
        enabled: Новый статус стратегии
    """

    strategy_id: str = Field(
        ...,
        description="Идентификатор стратегии.",
    )
    enabled: Optional[bool] = Field(
        None,
        description="Статус стратегии: true — включена, false — отключена.",
    )


class StrategyStatusResponse(BaseModel):
    """Схема ответа на запрос изменения статуса стратегии ценообразования.

    Attributes:
        None — сервер возвращает пустой объект при успехе
    """

    pass
