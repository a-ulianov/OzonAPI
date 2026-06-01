"""Описывает модели методов раздела Работа с квантами.
https://docs.ozon.ru/api/seller/#tag/Quants
"""
__all__ = [
    "ProductQuantInfoBarcode",
    "ProductQuantInfoDimensions",
    "ProductQuantInfoItem",
    "ProductQuantInfoMarketingPrice",
    "ProductQuantInfoQuant",
    "ProductQuantInfoQuantInfo",
    "ProductQuantInfoRequest",
    "ProductQuantInfoResponse",
    "ProductQuantInfoStatuses",
    "ProductQuantListProduct",
    "ProductQuantListProductQuant",
    "ProductQuantListRequest",
    "ProductQuantListResponse",
]

from .v1__product_quant_info import (
    ProductQuantInfoBarcode,
    ProductQuantInfoDimensions,
    ProductQuantInfoItem,
    ProductQuantInfoMarketingPrice,
    ProductQuantInfoQuant,
    ProductQuantInfoQuantInfo,
    ProductQuantInfoRequest,
    ProductQuantInfoResponse,
    ProductQuantInfoStatuses,
)
from .v1__product_quant_list import (
    ProductQuantListProduct,
    ProductQuantListProductQuant,
    ProductQuantListRequest,
    ProductQuantListResponse,
)
