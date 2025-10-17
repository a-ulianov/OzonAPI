from .core import APIConfig as SellerAPIConfig
from .methods import (
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerFBSAPI,
    SellerPricesAndStocksAPI,
    SellerProductAPI,
    SellerWarehouseAPI,
)


class SellerAPI(
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerFBSAPI,
    SellerPricesAndStocksAPI,
    SellerProductAPI,
    SellerWarehouseAPI,
):
    """
    Основной класс для работы с Seller API Ozon.
    Объединяет все доступные методы API в единый интерфейс.
    """
    pass


__all__ = ["SellerAPI", "SellerAPIConfig"]

# Импортируйте здесь бизнес-методы и собирайте публичный API
