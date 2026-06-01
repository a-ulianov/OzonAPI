"""Композиция миксинов методов раздела Работа с цифровыми товарами.

Объединяет методы работы с цифровыми товарами
в единый класс :class:`SellerDigitalAPI`.
"""

from ...core import APIManager
from .posting_digital_codes_upload import PostingDigitalCodesUploadMixin
from .product_digital_stocks_import import ProductDigitalStocksImportMixin


class SellerDigitalAPI(
    PostingDigitalCodesUploadMixin,
    ProductDigitalStocksImportMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Работа с цифровыми товарами.

    Notes:
        • Загрузка кодов цифровых товаров для отправлений и обновление остатков
          цифровых товаров.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Digital
    """

    pass
