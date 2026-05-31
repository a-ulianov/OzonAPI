from .core import APIConfig as SellerAPIConfig
from .methods import (
    SellerActionsAPI,
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerFBSAPI,
    SellerFBOAPI,
    SellerPricesAndStocksAPI,
    SellerPricingStrategyAPI,
    SellerProductAPI,
    SellerWarehouseAPI,
    SellerFBSAssemblyLabelingAPI,
)


class SellerAPI(
    SellerActionsAPI,
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerFBOAPI,
    SellerFBSAPI,
    SellerFBSAssemblyLabelingAPI,
    SellerPricesAndStocksAPI,
    SellerPricingStrategyAPI,
    SellerProductAPI,
    SellerWarehouseAPI,
):
    """
    Основной класс для работы с Seller API Ozon.
    Объединяет все доступные методы API в единый интерфейс.
    """
    pass

__all__ = ["SellerAPI", "SellerAPIConfig"]

