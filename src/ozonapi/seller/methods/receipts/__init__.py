"""Композиция миксинов методов раздела Чеки.

Объединяет методы работы с чеками продавца
в единый класс :class:`SellerReceiptAPI`.
"""

from ...core import APIManager
from .receipts_get import ReceiptsGetMixin
from .receipts_seller_list import ReceiptsSellerListMixin
from .receipts_upload import ReceiptsUploadMixin


class SellerReceiptAPI(
    ReceiptsGetMixin,
    ReceiptsSellerListMixin,
    ReceiptsUploadMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Чеки.

    Notes:
        • Работа с чеками продавца: список чеков, получение чека в PDF и загрузка чека.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Receipt
    """

    pass
