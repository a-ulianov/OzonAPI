"""Схемы метода rating_history (рейтинги продавца за период, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class RatingHistoryRequest(BaseModel):
    """Параметры запроса рейтингов продавца за период.

    Attributes:
        date_from: Начало периода
        date_to: Конец периода
        ratings: Фильтр по рейтингу (системные названия)
        with_premium_scores: Признак, что в ответе нужны штрафные баллы Premium
    """
    date_from: str = Field(..., description="Начало периода.")
    date_to: str = Field(..., description="Конец периода.")
    ratings: list[str] = Field(
        ..., description="Фильтр по рейтингу (системные названия рейтингов)."
    )
    with_premium_scores: Optional[bool] = Field(
        None, description="Признак, что в ответе нужны штрафные баллы Premium."
    )


class RatingHistoryPremiumScore(BaseModel):
    """Информация о начисленных штрафных баллах.

    Attributes:
        date: Дата, когда были начислены штрафные баллы
        rating_value: Значение рейтинга, за которое начислены баллы
        value: Количество начисленных штрафных баллов
    """
    date: Optional[str] = Field(
        None, description="Дата, когда были начислены штрафные баллы."
    )
    rating_value: Optional[float] = Field(
        None, description="Значение рейтинга, за которое начислены баллы."
    )
    value: Optional[int] = Field(
        None, description="Количество начисленных штрафных баллов."
    )


class RatingHistoryPremiumScores(BaseModel):
    """Штрафные баллы по рейтингу.

    Attributes:
        rating: Название рейтинга
        scores: Информация о штрафных баллах
    """
    rating: Optional[str] = Field(
        None, description="Название рейтинга."
    )
    scores: Optional[list[RatingHistoryPremiumScore]] = Field(
        None, description="Информация о штрафных баллах."
    )


class RatingHistoryValueStatus(BaseModel):
    """Статус значения рейтинга.

    Attributes:
        danger: Признак, превышено ли пороговое значение
        premium: Признак, достигнуто ли пороговое значение Premium
        warning: Признак наличия предупреждения
    """
    danger: Optional[bool] = Field(
        None, description="Признак, превышено ли пороговое значение."
    )
    premium: Optional[bool] = Field(
        None, description="Признак, достигнуто ли пороговое значение Premium."
    )
    warning: Optional[bool] = Field(
        None, description="Признак наличия предупреждения."
    )


class RatingHistoryValue(BaseModel):
    """Значение рейтинга за период.

    Attributes:
        date_from: Дата начала подсчёта рейтинга
        date_to: Дата конца подсчёта рейтинга
        status: Статус значения рейтинга
        value: Значение рейтинга
    """
    date_from: Optional[str] = Field(
        None, description="Дата начала подсчёта рейтинга."
    )
    date_to: Optional[str] = Field(
        None, description="Дата конца подсчёта рейтинга."
    )
    status: Optional[RatingHistoryValueStatus] = Field(
        None, description="Статус значения рейтинга."
    )
    value: Optional[float] = Field(
        None, description="Значение рейтинга."
    )


class RatingHistoryRating(BaseModel):
    """Информация о рейтинге продавца.

    Attributes:
        danger_threshold: Пороговое значение рейтинга, при котором продажи блокируются
        premium_threshold: Пороговое значение рейтинга для Premium
        rating: Системное название рейтинга
        values: Список значений рейтинга
        warning_threshold: Пороговое значение рейтинга, при котором появляется предупреждение
    """
    danger_threshold: Optional[float] = Field(
        None, description="Пороговое значение рейтинга, при котором продажи блокируются."
    )
    premium_threshold: Optional[float] = Field(
        None, description="Пороговое значение рейтинга для Premium."
    )
    rating: Optional[str] = Field(
        None, description="Системное название рейтинга."
    )
    values: Optional[list[RatingHistoryValue]] = Field(
        None, description="Список значений рейтинга."
    )
    warning_threshold: Optional[float] = Field(
        None, description="Пороговое значение рейтинга, при котором появляется предупреждение."
    )


class RatingHistoryResponse(BaseModel):
    """Ответ с рейтингами продавца за период.

    Attributes:
        premium_scores: Информация о штрафных баллах
        ratings: Информация о рейтингах продавца
    """
    premium_scores: Optional[list[RatingHistoryPremiumScores]] = Field(
        None, description="Информация о штрафных баллах."
    )
    ratings: Optional[list[RatingHistoryRating]] = Field(
        None, description="Информация о рейтингах продавца."
    )
