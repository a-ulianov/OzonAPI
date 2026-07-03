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
    "ProductActionTimerUpdateRequest",
    "ProductActionTimerUpdateResponse",
    "ProductActionTimerStatusRequest",
    "ProductActionTimerStatusResponse",
    "ProductActionTimerStatus",
    "ProductInfoDiscountedRequest",
    "ProductInfoDiscountedResponse",
    "ProductInfoDiscountedItem",
    "ProductUpdateDiscountRequest",
    "ProductUpdateDiscountResponse",
    "ProductInfoWarehouseStocksRequest",
    "ProductInfoWarehouseStocksItem",
    "ProductInfoWarehouseStocksResponse",
    "ProductInfoStocksByWarehouseFBSV1Request",
    "ProductInfoStocksByWarehouseFBSV1Item",
    "ProductInfoStocksByWarehouseFBSV1Response",
    "ProductInfoStocksByWarehouseFBORequest",
    "ProductInfoStocksByWarehouseFBOItem",
    "ProductInfoStocksByWarehouseFBOResponse",
]

from .v1__product_import_prices import (
    ProductImportPricesRequest,
    ProductImportPricesResponse,
    ProductImportPricesItem,
    ProductImportPricesError,
    ProductImportPricesResultItem,
)
from .v2__product_info_stocks_by_warehouse_fbs import (
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
from .v1__product_action_timer_update import (
    ProductActionTimerUpdateRequest,
    ProductActionTimerUpdateResponse,
)
from .v1__product_action_timer_status import (
    ProductActionTimerStatusRequest,
    ProductActionTimerStatusResponse,
    ProductActionTimerStatus,
)
from .v1__product_info_discounted import (
    ProductInfoDiscountedRequest,
    ProductInfoDiscountedResponse,
    ProductInfoDiscountedItem,
)
from .v1__product_update_discount import (
    ProductUpdateDiscountRequest,
    ProductUpdateDiscountResponse,
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
from .v1__product_info_warehouse_stocks import (
    ProductInfoWarehouseStocksItem,
    ProductInfoWarehouseStocksRequest,
    ProductInfoWarehouseStocksResponse,
)
from .v1__product_info_stocks_by_warehouse_fbs import (
    ProductInfoStocksByWarehouseFBSV1Item,
    ProductInfoStocksByWarehouseFBSV1Request,
    ProductInfoStocksByWarehouseFBSV1Response,
)
from .v1__product_info_stocks_by_warehouse_fbo import (
    ProductInfoStocksByWarehouseFBOItem,
    ProductInfoStocksByWarehouseFBORequest,
    ProductInfoStocksByWarehouseFBOResponse,
)