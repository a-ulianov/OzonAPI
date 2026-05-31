"""Схемы метода rating_summary (текущие рейтинги продавца, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class RatingItemChange(BaseModel):
    """Изменение значения рейтинга.

    Attributes:
        direction: Как изменилось значение рейтинга
        meaning: Что означает изменение
    """
    direction: Optional[str] = Field(
        None, description="Как изменилось значение рейтинга."
    )
    meaning: Optional[str] = Field(
        None, description="Что означает изменение."
    )


class RatingSummaryItem(BaseModel):
    """Информация о рейтинге.

    Attributes:
        change: Изменение значения рейтинга
        current_value: Текущее значение рейтинга
        name: Название рейтинга
        past_value: Предыдущее значение рейтинга
        rating: Название рейтинга в системе
        rating_direction: Каким должно быть значение рейтинга
        status: Статус рейтинга
        value_type: Тип значения
    """
    change: Optional[RatingItemChange] = Field(
        None, description="Изменение значения рейтинга."
    )
    current_value: Optional[float] = Field(
        None, description="Текущее значение рейтинга."
    )
    name: Optional[str] = Field(
        None, description="Название рейтинга."
    )
    past_value: Optional[float] = Field(
        None, description="Предыдущее значение рейтинга."
    )
    rating: Optional[str] = Field(
        None, description="Название рейтинга в системе."
    )
    rating_direction: Optional[str] = Field(
        None, description="Каким должно быть значение рейтинга."
    )
    status: Optional[str] = Field(
        None, description="Статус рейтинга."
    )
    value_type: Optional[str] = Field(
        None, description="Тип значения."
    )


class RatingSummaryGroup(BaseModel):
    """Группа рейтингов.

    Attributes:
        group_name: Название группы рейтингов
        items: Список рейтингов
    """
    group_name: Optional[str] = Field(
        None, description="Название группы рейтингов."
    )
    items: Optional[list[RatingSummaryItem]] = Field(
        None, description="Список рейтингов."
    )


class RatingSummaryLocalIndex(BaseModel):
    """Данные по индексу локализации.

    Attributes:
        calculation_date: Дата расчёта индекса локализации
        localization_percentage: Значение индекса локализации
    """
    calculation_date: Optional[str] = Field(
        None, description="Дата расчёта индекса локализации."
    )
    localization_percentage: Optional[int] = Field(
        None, description="Значение индекса локализации."
    )


class RatingSummaryResponse(BaseModel):
    """Ответ с текущими рейтингами продавца.

    Attributes:
        groups: Список с группами рейтингов
        localization_index: Данные по индексу локализации
        penalty_score_exceeded: Признак, что баланс штрафных баллов превышен
        premium: Признак наличия подписки Premium
        premium_plus: Признак наличия подписки Premium Plus
    """
    groups: Optional[list[RatingSummaryGroup]] = Field(
        None, description="Список с группами рейтингов."
    )
    localization_index: Optional[RatingSummaryLocalIndex] = Field(
        None, description="Данные по индексу локализации."
    )
    penalty_score_exceeded: Optional[bool] = Field(
        None, description="Признак, что баланс штрафных баллов превышен."
    )
    premium: Optional[bool] = Field(
        None, description="Признак наличия подписки Premium."
    )
    premium_plus: Optional[bool] = Field(
        None, description="Признак наличия подписки Premium Plus."
    )
