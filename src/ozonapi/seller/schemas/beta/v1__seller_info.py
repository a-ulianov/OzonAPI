"""https://docs.ozon.ru/api/seller/?#operation/SellerAPI_SellerInfo"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.company import TaxSystem, RatingStatus, RatingValueType, SubscriptionType
from ...common.enumerations.localization import CurrencyCode


class SellerInfoCompany(BaseModel):
    """Описывает информацию о компании.

    Attributes:
        country: Страна
        currency: Валюта
        inn: ИНН
        legal_name: Название юридического лица
        name: Название компании на Ozon
        ogrn: ОГРН
        ownership_form: Форма собственности
        tax_system: Система налогообложения
    """
    country: str = Field(
        ..., description="Страна."
    )
    currency: CurrencyCode = Field(
        ..., description="Валюта."
    )
    inn: str = Field(
        ..., description="ИНН."
    )
    legal_name: str = Field(
        ..., description="Название юридического лица."
    )
    name: str = Field(
        ..., description="Название компании на Ozon."
    )
    ogrn: str = Field(
        ..., description="ОГРН."
    )
    ownership_form: str = Field(
        ..., description="Форма собственности."
    )
    tax_system: TaxSystem = Field(
        ..., description="Система налогообложения."
    )


class SellerInfoRatingStatus(BaseModel):
    """Статус рейтинга.

    Attributes:
        danger: Признак, превышено ли пороговое значение рейтинга для блокировки
        premium: Признак, достигнуто ли пороговое значение для участия в Premium-программе
        warning: Признак наличия предупреждения о возможном превышении порогового значения для блокировки
    """
    danger: bool = Field(
        ..., description="Признак, превышено ли пороговое значение рейтинга для блокировки."
    )
    premium: bool = Field(
        ..., description="Признак, достигнуто ли пороговое значение для участия в Premium-программе."
    )
    warning: bool = Field(
        ..., description="Признак наличия предупреждения о возможном превышении порогового значения для блокировки."
    )


class SellerInfoRatingValue(BaseModel):
    """Описывает значение рейтинга.

    Attributes:
        date_from: Дата начала подсчёта рейтинга
        date_to: Дата конца подсчёта рейтинга
        formatted: Отформатированное значение рейтинга
        status: Статус рейтинга
        value: Значение рейтинга в системе
    """
    date_from: Optional[datetime.datetime] = Field(
        None, description="Дата начала подсчёта рейтинга."
    )
    date_to: Optional[datetime.datetime] = Field(
        None, description="Дата конца подсчёта рейтинга."
    )
    formatted: Optional[str] = Field(
        None, description="<Отформатированное значение рейтинга."
    )
    status: Optional[SellerInfoRatingStatus] = Field(
        None, description="Статус рейтинга."
    )
    value: Optional[float] = Field(
        None, description="Значение рейтинга в системе."
    )


class SellerInfoRating(BaseModel):
    """Описывает информацию о рейтинге продавца.

    Attributes:
        current_value: Значение рейтинга
        name: Название рейтинга
        past_value: Предыдущее значение рейтинга
        rating: Название рейтинга в системе
        status: Статус рейтинга
        value_type: Тип значения
    """
    current_value: Optional[SellerInfoRatingValue] = Field(
        None, description="Значение рейтинга."
    )
    name: str = Field(
        ..., description="Название рейтинга."
    )
    past_value: Optional[SellerInfoRatingValue] = Field(
        None, description="Предыдущее значение рейтинга."
    )
    rating: Optional[str] = Field(
        None, description="Название рейтинга в системе."
    )
    status: RatingStatus | str = Field(
        ..., description="Статус рейтинга."
    )
    value_type: RatingValueType | str = Field(
        ..., description="Тип значения."
    )


class SellerInfoSubscription(BaseModel):
    """Информация о подписке.

    Attributes:
        is_premium: true, если есть подписка
        type: Тип подписки
    """
    is_premium: bool = Field(
        ..., description="true, если есть подписка."
    )
    type: SubscriptionType = Field(
        ..., description="Тип подписки."
    )


class SellerInfoResponse(BaseModel):
    """Описывает схему ответа на запрос о получении информации о продавце.

    Attributes:
        company: Информация о компании
        ratings: Список рейтингов
        subscription: Информация о подписке продавца
    """
    company: SellerInfoCompany = Field(
        ..., description="Информация о компании."
    )
    ratings: Optional[list[SellerInfoRating]] = Field(
        default_factory=list, description="Список рейтингов."
    )
    subscription: Optional[SellerInfoSubscription] = Field(
        None, description="Информация о подписке продавца."
    )