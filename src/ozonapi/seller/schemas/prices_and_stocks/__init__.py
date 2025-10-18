"""Описывает модели методов раздела Цены и остатки товаров.
https://docs.ozon.ru/api/seller/#tag/PricesandStocksAPI
"""
__all__ = [
    "ProductImportPricesRequest",
    "ProductImportPricesResponse",
    "ProductInfoStocksByWarehouseFBSRequest",
    "ProductInfoStocksByWarehouseFBSResponse",
    "ProductInfoPricesRequest",
    "ProductInfoPricesResponse",
    "ProductInfoStocksRequest",
    "ProductInfoStocksResponse",
    "ProductsStocksRequest",
    "ProductsStocksResponse",
]

from .v1__product_import_prices import ProductImportPricesRequest, ProductImportPricesResponse
from .v1__product_info_stocks_by_warehouse_fbs import ProductInfoStocksByWarehouseFBSRequest, \
    ProductInfoStocksByWarehouseFBSResponse
from .v2__products_stocks import ProductsStocksRequest, ProductsStocksResponse
from .v4__product_info_stocks import ProductInfoStocksRequest, ProductInfoStocksResponse
from .v5__product_info_prices import ProductInfoPricesRequest, ProductInfoPricesResponse
