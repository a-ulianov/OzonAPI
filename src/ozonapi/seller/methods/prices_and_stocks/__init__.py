__all__ = ["SellerPricesAndStocksAPI", ]

from .product_action_timer_status import ProductActionTimerStatusMixin
from .product_action_timer_update import ProductActionTimerUpdateMixin
from .product_import_prices import ProductImportPricesMixin
from .product_info_discounted import ProductInfoDiscountedMixin
from .product_info_prices import ProductInfoPricesMixin
from .product_info_stocks import ProductInfoStocksMixin
from .product_info_stocks_by_warehouse_fbs import ProductInfoStocksByWarehouseFBSMixin
from .product_info_stocks_by_warehouse_fbs_v1 import (
    ProductInfoStocksByWarehouseFBSV1Mixin,
)
from .product_info_warehouse_stocks import ProductInfoWarehouseStocksMixin
from .product_update_discount import ProductUpdateDiscountMixin
from .products_stocks import ProductsStocksMixin


class SellerPricesAndStocksAPI(
    ProductActionTimerStatusMixin,
    ProductActionTimerUpdateMixin,
    ProductImportPricesMixin,
    ProductInfoDiscountedMixin,
    ProductInfoPricesMixin,
    ProductInfoStocksByWarehouseFBSMixin,
    ProductInfoStocksByWarehouseFBSV1Mixin,
    ProductInfoStocksMixin,
    ProductInfoWarehouseStocksMixin,
    ProductUpdateDiscountMixin,
    ProductsStocksMixin,

):
    """Реализует методы раздела Цены и остатки товаров.

    References:
        https://docs.ozon.ru/api/seller/#tag/PricesandStocksAPI
    """
    pass