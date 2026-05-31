"""Композиция миксинов методов раздела Рейтинг продавца.

Объединяет методы работы с рейтингами в единый класс :class:`SellerRatingAPI`.
"""

from ...core import APIManager
from .rating_history import RatingHistoryMixin
from .rating_index_fbs_info import RatingIndexFBSInfoMixin
from .rating_index_fbs_posting_list import RatingIndexFBSPostingListMixin
from .rating_summary import RatingSummaryMixin


class SellerRatingAPI(
    RatingHistoryMixin,
    RatingIndexFBSInfoMixin,
    RatingIndexFBSPostingListMixin,
    RatingSummaryMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Рейтинг продавца.

    Notes:
        • Объединяет методы текущих рейтингов, истории рейтингов за период и индекса
          ошибок FBS/rFBS (сводка и список отправлений).

    References:
        • https://docs.ozon.ru/api/seller/#tag/SellerRating
    """

    pass
