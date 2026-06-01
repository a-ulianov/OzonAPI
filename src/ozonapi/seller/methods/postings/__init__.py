"""Композиция миксинов методов раздела Отправления.

Объединяет методы работы с отправлениями заказа
в единый класс :class:`SellerPostingAPI`.
"""

from ...core import APIManager
from .posting_cancel import PostingCancelMixin
from .posting_cancel_status import PostingCancelStatusMixin
from .posting_marks import PostingMarksMixin


class SellerPostingAPI(
    PostingCancelMixin,
    PostingCancelStatusMixin,
    PostingMarksMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Отправления.

    Notes:
        • Отмена отправления из заказа, проверка статуса отмены и получение
          маркировок экземпляров из отправлений.

    References:
        • https://docs.ozon.ru/api/seller/#tag/FboPostingAPI
    """

    pass
