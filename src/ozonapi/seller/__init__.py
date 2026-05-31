from .core import APIConfig as SellerAPIConfig
from .methods import (
    SellerActionsAPI,
    SellerAnalyticsAPI,
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
    SellerFBSDeliveryAPI,
    SellerFBSContainerAPI,
    SellerReturnsAPI,
    SellerReviewAPI,
    SellerQuestionAPI,
    SellerCertificateAPI,
    SellerReportAPI,
    SellerFinanceAPI,
)


class SellerAPI(
    SellerActionsAPI,
    SellerAnalyticsAPI,
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCategoryAPI,
    SellerCertificateAPI,
    SellerFBOAPI,
    SellerFBSAPI,
    SellerFBSAssemblyLabelingAPI,
    SellerFBSContainerAPI,
    SellerFBSDeliveryAPI,
    SellerFinanceAPI,
    SellerPricesAndStocksAPI,
    SellerPricingStrategyAPI,
    SellerProductAPI,
    SellerQuestionAPI,
    SellerReportAPI,
    SellerReturnsAPI,
    SellerReviewAPI,
    SellerWarehouseAPI,
):
    """
    Основной класс для работы с Seller API Ozon.
    Объединяет все доступные методы API в единый интерфейс.
    """
    pass

__all__ = ["SellerAPI", "SellerAPIConfig"]

