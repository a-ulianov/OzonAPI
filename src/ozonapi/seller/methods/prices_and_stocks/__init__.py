__all__ = ["SellerPricesAndStocksAPI", ]

from .product_import_prices import ProductImportPricesMixin
from .product_info_prices import ProductInfoPricesMixin
from .product_info_stocks import ProductInfoStocksMixin
from .product_info_stocks_by_warehouse_fbs import ProductInfoStocksByWarehouseFBSMixin
from .products_stocks import ProductsStocksMixin


class SellerPricesAndStocksAPI(
    ProductImportPricesMixin,
    ProductInfoPricesMixin,
    ProductInfoStocksByWarehouseFBSMixin,
    ProductInfoStocksMixin,
    ProductsStocksMixin,

):
    """Реализует методы раздела Цены и остатки товаров.

    References:
        https://docs.ozon.ru/api/seller/#tag/PricesandStocksAPI
    """
    pass