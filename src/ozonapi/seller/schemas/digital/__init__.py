"""Описывает модели методов раздела Работа с цифровыми товарами.
https://docs.ozon.ru/api/seller/#tag/Digital
"""
__all__ = [
    "PostingDigitalCodesUploadExemplar",
    "PostingDigitalCodesUploadExemplarError",
    "PostingDigitalCodesUploadRequest",
    "PostingDigitalCodesUploadResponse",
    "PostingDigitalCodesUploadResultExemplar",
    "ProductDigitalStocksImportError",
    "ProductDigitalStocksImportRequest",
    "ProductDigitalStocksImportResponse",
    "ProductDigitalStocksImportStatus",
    "ProductDigitalStocksImportStock",
]

from .v1__posting_digital_codes_upload import (
    PostingDigitalCodesUploadExemplar,
    PostingDigitalCodesUploadExemplarError,
    PostingDigitalCodesUploadRequest,
    PostingDigitalCodesUploadResponse,
    PostingDigitalCodesUploadResultExemplar,
)
from .v1__product_digital_stocks_import import (
    ProductDigitalStocksImportError,
    ProductDigitalStocksImportRequest,
    ProductDigitalStocksImportResponse,
    ProductDigitalStocksImportStatus,
    ProductDigitalStocksImportStock,
)
