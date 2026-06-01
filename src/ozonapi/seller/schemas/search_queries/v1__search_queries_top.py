"""https://docs.ozon.ru/api/seller/#operation/SearchQueriesAPI_SearchQueriesTop"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import SearchQuery


class SearchQueriesTopRequest(BaseModel):
    """Схема запроса списка популярных поисковых запросов.

    Attributes:
        limit: Количество значений в ответе
        offset: Количество элементов, пропускаемых в ответе
    """

    limit: Optional[str] = Field(
        None, description="Количество значений в ответе (строка с числом int64)."
    )
    offset: Optional[str] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе "
                          "(строка с числом int64)."
    )


class SearchQueriesTopResponse(BaseModel):
    """Схема ответа со списком популярных поисковых запросов.

    Attributes:
        search_queries: Список популярных поисковых запросов с метриками
        offset: Количество пропущенных элементов
        total: Общее количество поисковых запросов
    """

    search_queries: list[SearchQuery] = Field(
        default_factory=list, description="Список популярных поисковых запросов с метриками."
    )
    offset: Optional[str] = Field(
        None, description="Количество пропущенных элементов (строка с числом int64)."
    )
    total: Optional[str] = Field(
        None, description="Общее количество поисковых запросов (строка с числом int64)."
    )
