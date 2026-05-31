"""https://docs.ozon.ru/api/seller/#operation/pricing_competitors"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyCompetitorsListRequest(BaseModel):
    """Схема запроса на получение списка конкурентов.

    Attributes:
        page: Номер страницы списка
        limit: Максимальное количество конкурентов на странице
    """

    page: int = Field(
        ...,
        description="Страница списка, с которой нужно выгрузить конкурентов. Минимальное значение — 1.",
        ge=1,
    )
    limit: int = Field(
        ...,
        description="Максимальное количество конкурентов на странице. Допустимы значения от 1 до 50.",
        ge=1,
        le=50,
    )


class StrategyCompetitorItem(BaseModel):
    """Элемент списка конкурентов.

    Attributes:
        id: Идентификатор конкурента
        name: Название конкурента
    """

    id: Optional[int] = Field(
        None,
        description="Идентификатор конкурента.",
    )
    name: Optional[str] = Field(
        None,
        description="Название конкурента.",
    )


class StrategyCompetitorsListResponse(BaseModel):
    """Схема ответа на запрос списка конкурентов.

    Attributes:
        competitor: Список конкурентов
        total: Общее количество конкурентов
    """

    competitor: Optional[list[StrategyCompetitorItem]] = Field(
        None,
        description="Список конкурентов.",
    )
    total: Optional[int] = Field(
        None,
        description="Общее количество конкурентов.",
    )
