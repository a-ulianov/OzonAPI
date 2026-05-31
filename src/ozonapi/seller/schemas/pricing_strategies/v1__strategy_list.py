"""https://docs.ozon.ru/api/seller/#operation/pricing_list"""
from typing import Optional

from pydantic import BaseModel, Field


class StrategyListRequest(BaseModel):
    """Схема запроса на получение списка стратегий ценообразования.

    Attributes:
        page: Номер страницы списка
        limit: Максимальное количество стратегий на странице
    """

    page: int = Field(
        ...,
        description="Страница списка, с которой нужно выгрузить стратегии. Минимальное значение — 1.",
        ge=1,
    )
    limit: int = Field(
        ...,
        description="Максимальное количество стратегий на странице. Допустимые значения — от 1 до 50.",
        ge=1,
        le=50,
    )


class StrategyListItem(BaseModel):
    """Элемент списка стратегий ценообразования.

    Attributes:
        id: Идентификатор стратегии
        name: Название стратегии
        type: Тип стратегии
        update_type: Тип последнего изменения стратегии
        updated_at: Дата последнего изменения
        products_count: Количество товаров в стратегии
        competitors_count: Количество выбранных конкурентов
        enabled: Статус стратегии
    """

    id: Optional[str] = Field(
        None,
        description="Идентификатор стратегии.",
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
    updated_at: Optional[str] = Field(
        None,
        description="Дата последнего изменения.",
    )
    products_count: Optional[int] = Field(
        None,
        description="Количество товаров в стратегии.",
    )
    competitors_count: Optional[int] = Field(
        None,
        description="Количество выбранных конкурентов.",
    )
    enabled: Optional[bool] = Field(
        None,
        description="Статус стратегии: true — включена, false — отключена.",
    )


class StrategyListResponse(BaseModel):
    """Схема ответа на запрос списка стратегий ценообразования.

    Attributes:
        strategies: Список стратегий
        total: Общее количество стратегий
    """

    strategies: Optional[list[StrategyListItem]] = Field(
        None,
        description="Список стратегий ценообразования.",
    )
    total: Optional[int] = Field(
        None,
        description="Общее количество стратегий.",
    )
