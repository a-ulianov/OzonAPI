"""Композиция миксинов методов раздела Отзывы (beta).

Объединяет методы работы с отзывами и комментариями к ним
в единый класс :class:`SellerReviewAPI`.
"""

from ...core import APIManager
from .review_change_status import ReviewChangeStatusMixin
from .review_change_status_v1 import ReviewChangeStatusV1Mixin
from .review_comment_create import ReviewCommentCreateMixin
from .review_comment_delete import ReviewCommentDeleteMixin
from .review_comment_delete_v1 import ReviewCommentDeleteV1Mixin
from .review_comment_list import ReviewCommentListMixin
from .review_count import ReviewCountMixin
from .review_count_v1 import ReviewCountV1Mixin
from .review_info import ReviewInfoMixin
from .review_info_v1 import ReviewInfoV1Mixin
from .review_list import ReviewListMixin
from .review_list_v1 import ReviewListV1Mixin


class SellerReviewAPI(
    ReviewChangeStatusMixin,
    ReviewChangeStatusV1Mixin,
    ReviewCommentCreateMixin,
    ReviewCommentDeleteMixin,
    ReviewCommentDeleteV1Mixin,
    ReviewCommentListMixin,
    ReviewCountMixin,
    ReviewCountV1Mixin,
    ReviewInfoMixin,
    ReviewInfoV1Mixin,
    ReviewListMixin,
    ReviewListV1Mixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Отзывы (beta).

    Notes:
        • Объединяет методы получения списка/информации/количества отзывов,
          управления статусом отзывов и работы с комментариями.
        • Раздел доступен продавцам с подпиской Premium Plus.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Review
    """

    pass
