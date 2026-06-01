"""https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsProductQueries"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.analytics import (
    AnalyticsProductQueriesSortBy,
    AnalyticsProductQueriesSortDir,
)


class AnalyticsProductQueriesRequest(BaseModel):
    """Схема запроса информации о запросах товаров продавца (Premium).

    Attributes:
        date_from: Дата начала периода
        date_to: Дата окончания периода
        skus: Список SKU товаров (обязательное поле)
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


class AnalyticsPeriod(BaseModel):
    """Период анализа.

    Attributes:
        date_from: Дата начала периода
        date_to: Дата окончания периода
    """

    date_from: Optional[str] = Field(
        None, description="Дата начала периода."
    )
    date_to: Optional[str] = Field(
        None, description="Дата окончания периода."
    )


class AnalyticsProductQueriesItem(BaseModel):
    """Информация о запросах по товару.

    Attributes:
        sku: SKU товара
        offer_id: Идентификатор товара в системе продавца — артикул
        name: Название товара
        category: Категория товара
        currency: Валюта
        gmv: Оборот по товару
        position: Средняя позиция в выдаче
        unique_search_users: Уникальные пользователи, искавшие товар
        unique_view_users: Уникальные пользователи, видевшие товар
        view_conversion: Конверсия в просмотр
    """

    sku: Optional[int] = Field(
        None, description="SKU товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    category: Optional[str] = Field(
        None, description="Категория товара."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )
    gmv: Optional[float] = Field(
        None, description="Оборот по товару."
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


class AnalyticsProductQueriesResponse(BaseModel):
    """Схема ответа с информацией о запросах товаров продавца.

    Attributes:
        analytics_period: Период анализа
        items: Товары с метриками по запросам
        page_count: Количество страниц
        total: Общее количество товаров
    """

    analytics_period: Optional[AnalyticsPeriod] = Field(
        None, description="Период анализа."
    )
    items: list[AnalyticsProductQueriesItem] = Field(
        default_factory=list, description="Товары с метриками по запросам."
    )
    page_count: Optional[int] = Field(
        None, description="Количество страниц."
    )
    total: Optional[int] = Field(
        None, description="Общее количество товаров."
    )
