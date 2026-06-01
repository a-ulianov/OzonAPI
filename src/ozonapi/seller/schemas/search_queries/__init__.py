"""Описывает модели раздела «Поисковые запросы» (Premium).
https://docs.ozon.ru/api/seller/#tag/SearchQueriesAPI
"""
__all__ = [
    "SearchQuery",
    "SearchQueriesTextRequest",
    "SearchQueriesTextResponse",
    "SearchQueriesTopRequest",
    "SearchQueriesTopResponse",
]

from .base import SearchQuery
from .v1__search_queries_text import (
    SearchQueriesTextRequest,
    SearchQueriesTextResponse,
)
from .v1__search_queries_top import (
    SearchQueriesTopRequest,
    SearchQueriesTopResponse,
)
