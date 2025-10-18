"""Описывает модели методов раздела Цены и остатки товаров.
https://docs.ozon.ru/api/seller/#tag/PricesandStocksAPI
"""
__all__ = [
    "ProductImportPricesRequest",
    "ProductImportPricesResponse",
    "ProductImportPricesItem",
    "ProductImportPricesError",
    "ProductImportPricesResultItem",
    "ProductInfoStocksByWarehouseFBSRequest",
    "ProductInfoStocksByWarehouseFBSResponse",
    "ProductInfoStocksByWarehouseFBSItem",
    "ProductInfoPricesRequest",
    "ProductInfoPricesResponse",
    "ProductInfoPricesFilter",
    "ProductInfoPricesCommissions",
    "ProductInfoPricesAction",
    "ProductInfoPricesMarketingActions",
    "ProductInfoPricesPrice",
    "ProductInfoPricesIndexData",
    "ProductInfoPricesPriceIndexes",
    "ProductInfoPricesItem",
    "ProductInfoStocksRequest",
    "ProductInfoStocksResponse",
    "ProductInfoPricesRequestFilterWithQuant",
    "ProductInfoStocksFilter",
    "ProductInfoStocksStock",
    "ProductInfoStocksItem",
    "ProductsStocksRequest",
    "ProductsStocksResponse",
    "ProductsStocksItem",
    "ProductsStocksError",
    "ProductsStocksResultItem",
]

from .v1__product_import_prices import (
    ProductImportPricesRequest,
    ProductImportPricesResponse,
    ProductImportPricesItem,
    ProductImportPricesError,
    ProductImportPricesResultItem,
)
from .v1__product_info_stocks_by_warehouse_fbs import (
    ProductInfoStocksByWarehouseFBSRequest,
    ProductInfoStocksByWarehouseFBSResponse,
    ProductInfoStocksByWarehouseFBSItem,
)
from .v2__products_stocks import (
    ProductsStocksRequest,
    ProductsStocksResponse,
    ProductsStocksItem,
    ProductsStocksError,
    ProductsStocksResultItem,
)
from .v4__product_info_stocks import (
    ProductInfoStocksRequest,
    ProductInfoStocksResponse,
    ProductInfoPricesRequestFilterWithQuant,
    ProductInfoStocksFilter,
    ProductInfoStocksStock,
    ProductInfoStocksItem,
)
from .v5__product_info_prices import (
    ProductInfoPricesRequest,
    ProductInfoPricesResponse,
    ProductInfoPricesFilter,
    ProductInfoPricesCommissions,
    ProductInfoPricesAction,
    ProductInfoPricesMarketingActions,
    ProductInfoPricesPrice,
    ProductInfoPricesIndexData,
    ProductInfoPricesPriceIndexes,
    ProductInfoPricesItem,
)