__all__ = ["SellerSearchQueriesAPI", ]

from .search_queries_text import SearchQueriesTextMixin
from .search_queries_top import SearchQueriesTopMixin


class SellerSearchQueriesAPI(
    SearchQueriesTextMixin,
    SearchQueriesTopMixin,
):
    """Реализует методы раздела «Поисковые запросы» (Premium).

    References:
        https://docs.ozon.ru/api/seller/#tag/SearchQueriesAPI
    """
    pass
