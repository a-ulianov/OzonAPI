"""Композиция миксинов методов раздела Работа с квантами.

Объединяет методы работы с эконом-товарами (квантами)
в единый класс :class:`SellerQuantAPI`.
"""

from ...core import APIManager
from .product_quant_info import ProductQuantInfoMixin
from .product_quant_list import ProductQuantListMixin


class SellerQuantAPI(
    ProductQuantInfoMixin,
    ProductQuantListMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Работа с квантами.

    Notes:
        • Получение списка эконом-товаров (квантов) и подробной информации о них.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Quants
    """

    pass
