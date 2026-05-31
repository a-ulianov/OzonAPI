"""https://docs.ozon.ru/api/seller/#operation/pricing_delete"""
from pydantic import BaseModel, Field


class StrategyDeleteRequest(BaseModel):
    """Схема запроса на удаление стратегии ценообразования.

    Attributes:
        strategy_id: Идентификатор стратегии
    """

    strategy_id: str = Field(
        ...,
        description="Идентификатор стратегии.",
    )


class StrategyDeleteResponse(BaseModel):
    """Схема ответа на запрос удаления стратегии ценообразования.

    Attributes:
        None — сервер возвращает пустой объект при успехе
    """

    pass
