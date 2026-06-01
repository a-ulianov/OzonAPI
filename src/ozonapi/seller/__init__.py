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
    SellerDigitalAPI,
    SellerFboSupplyRequestAPI,
    SellerInvoiceAPI,
    SellerOrderAPI,
    SellerPassAPI,
    SellerPostingAPI,
    SellerRFBSDeliveryAPI,
    SellerRatingAPI,
    SellerReceiptAPI,
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
    SellerDigitalAPI,
    SellerFBOAPI,
    SellerFBSAPI,
    SellerFBSAssemblyLabelingAPI,
    SellerFBSContainerAPI,
    SellerFBSDeliveryAPI,
    SellerFboSupplyRequestAPI,
    SellerFinanceAPI,
    SellerInvoiceAPI,
    SellerOrderAPI,
    SellerPassAPI,
    SellerPostingAPI,
    SellerPricesAndStocksAPI,
    SellerPricingStrategyAPI,
    SellerProductAPI,
    SellerQuestionAPI,
    SellerRFBSDeliveryAPI,
    SellerRatingAPI,
    SellerReceiptAPI,
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

