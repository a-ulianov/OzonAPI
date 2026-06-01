"""https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsProductQueriesDetails"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.analytics import (
    AnalyticsProductQueriesSortBy,
    AnalyticsProductQueriesSortDir,
)
from .v1__analytics_product_queries import AnalyticsPeriod


class AnalyticsProductQueriesDetailsRequest(BaseModel):
    """Схема запроса детализации запросов по товару (Premium).

    Attributes:
        date_from: Дата начала периода
        date_to: Дата окончания периода
        skus: Список SKU товаров (обязательное поле)
        limit_by_sku: Ограничение количества запросов на один SKU
        page: Номер страницы
        page_size: Размер страницы
        sort_by: Поле сортировки
        sort_dir: Направление сортировки
    """

    date_from: Optional[str] = Field(
        None, description="Дата начала периода в формате RFC3339."
    )
    date_to: Optional[str] = Field(
        None, description="Дата окончания периода в формате RFC3339."
    )
    skus: list[str] = Field(
        ..., description="Список SKU товаров. Поле обязательно (живой API возвращает "
                         "ошибку при его отсутствии, хотя swagger помечает необязательным).",
        min_length=1
    )
    limit_by_sku: Optional[int] = Field(
        None, description="Ограничение количества запросов на один SKU."
    )
    page: Optional[int] = Field(
        None, description="Номер страницы."
    )
    page_size: Optional[int] = Field(
        None, description="Размер страницы."
    )
    sort_by: Optional[AnalyticsProductQueriesSortBy] = Field(
        None, description="Поле сортировки."
    )
    sort_dir: Optional[AnalyticsProductQueriesSortDir] = Field(
        None, description="Направление сортировки."
    )


class AnalyticsProductQueriesDetailsQuery(BaseModel):
    """Детализация поискового запроса по товару.

    Attributes:
        sku: SKU товара
        query: Текст поискового запроса
        query_index: Индекс запроса
        currency: Валюта
        gmv: Оборот по запросу
        order_count: Количество заказов
        position: Средняя позиция в выдаче
        unique_search_users: Уникальные пользователи, искавшие товар
        unique_view_users: Уникальные пользователи, видевшие товар
        view_conversion: Конверсия в просмотр
    """

    sku: Optional[int] = Field(
        None, description="SKU товара."
    )
    query: Optional[str] = Field(
        None, description="Текст поискового запроса."
    )
    query_index: Optional[int] = Field(
        None, description="Индекс запроса."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )
    gmv: Optional[float] = Field(
        None, description="Оборот по запросу."
    )
    order_count: Optional[int] = Field(
        None, description="Количество заказов."
    )
    position: Optional[float] = Field(
        None, description="Средняя позиция в выдаче."
    )
    unique_search_users: Optional[int] = Field(
        None, description="Уникальные пользователи, искавшие товар."
    )
    unique_view_users: Optional[int] = Field(
        None, description="Уникальные пользователи, видевшие товар."
    )
    view_conversion: Optional[float] = Field(
        None, description="Конверсия в просмотр."
    )


class AnalyticsProductQueriesDetailsResponse(BaseModel):
    """Схема ответа с детализацией запросов по товару.

    Attributes:
        analytics_period: Период анализа
        queries: Детализация поисковых запросов
        page_count: Количество страниц
        total: Общее количество запросов
    """

    analytics_period: Optional[AnalyticsPeriod] = Field(
        None, description="Период анализа."
    )
    queries: list[AnalyticsProductQueriesDetailsQuery] = Field(
        default_factory=list, description="Детализация поисковых запросов."
    )
    page_count: Optional[int] = Field(
        None, description="Количество страниц."
    )
    total: Optional[int] = Field(
        None, description="Общее количество запросов."
    )
