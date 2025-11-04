from .core import APIConfig as SellerAPIConfig
from .methods import (
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerFBSAPI,
    SellerFBOAPI,
    SellerPricesAndStocksAPI,
    SellerProductAPI,
    SellerWarehouseAPI,
    SellerFBSAssemblyLabelingAPI,
)


class SellerAPI(
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerFBOAPI,
    SellerFBSAPI,
    SellerFBSAssemblyLabelingAPI,
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

