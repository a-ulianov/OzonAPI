from .core import APIConfig as SellerAPIConfig
from .methods import (
    SellerActionsAPI,
    SellerAnalyticsAPI,
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCancellationAPI,
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
    SellerChatAPI,
    SellerDeliveryAPI,
    SellerFboSupplyRequestAPI,
    SellerInvoiceAPI,
    SellerOrderAPI,
    SellerPostingAPI,
    SellerRFBSDeliveryAPI,
    SellerRatingAPI,
    SellerReportAPI,
    SellerFinanceAPI,
)


class SellerAPI(
    SellerActionsAPI,
    SellerAnalyticsAPI,
    SellerBetaAPI,
    SellerBarcodeAPI,
    SellerCancellationAPI,
    SellerCategoryAPI,
    SellerCertificateAPI,
    SellerChatAPI,
    SellerDeliveryAPI,
    SellerFBOAPI,
    SellerFBSAPI,
    SellerFBSAssemblyLabelingAPI,
    SellerFBSContainerAPI,
    SellerFBSDeliveryAPI,
    SellerFboSupplyRequestAPI,
    SellerFinanceAPI,
    SellerInvoiceAPI,
    SellerOrderAPI,
    SellerPostingAPI,
    SellerPricesAndStocksAPI,
    SellerPricingStrategyAPI,
    SellerProductAPI,
    SellerQuestionAPI,
    SellerRFBSDeliveryAPI,
    SellerRatingAPI,
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

