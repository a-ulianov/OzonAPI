"""https://docs.ozon.ru/api/seller/#operation/SearchQueriesAPI_SearchQueriesText"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.search_queries import (
    SearchQueriesSortBy,
    SearchQueriesSortDir,
)
from .base import SearchQuery


class SearchQueriesTextRequest(BaseModel):
    """Схема запроса списка поисковых запросов по тексту.

    Attributes:
        text: Текст для поиска по поисковым запросам
        limit: Количество значений в ответе
        offset: Количество элементов, пропускаемых в ответе
        sort_by: Поле сортировки
        sort_dir: Направление сортировки
    """

    text: Optional[str] = Field(
        None, description="Текст для поиска по поисковым запросам."
    )
    limit: Optional[str] = Field(
        None, description="Количество значений в ответе (строка с числом int64)."
    )
    offset: Optional[str] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе "
                          "(строка с числом int64)."
    )
    sort_by: Optional[SearchQueriesSortBy] = Field(
        None, description="Поле сортировки."
    )
    sort_dir: Optional[SearchQueriesSortDir] = Field(
        None, description="Направление сортировки."
    )


class SearchQueriesTextResponse(BaseModel):
    """Схема ответа со списком поисковых запросов по тексту.

    Attributes:
        search_queries: Список поисковых запросов с метриками
        offset: Количество пропущенных элементов
        total: Общее количество поисковых запросов
    """

    search_queries: list[SearchQuery] = Field(
        default_factory=list, description="Список поисковых запросов с метриками."
    )
    offset: Optional[str] = Field(
        None, description="Количество пропущенных элементов (строка с числом int64)."
    )
    total: Optional[str] = Field(
        None, description="Общее количество поисковых запросов (строка с числом int64)."
    )
