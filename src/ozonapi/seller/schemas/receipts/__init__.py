"""Описывает модели методов раздела Чеки.
https://docs.ozon.ru/api/seller/#tag/Receipt
"""
__all__ = [
    "ReceiptsGetRequest",
    "ReceiptsGetResponse",
    "ReceiptsSellerListReceipt",
    "ReceiptsSellerListRequest",
    "ReceiptsSellerListResponse",
    "ReceiptsUploadRequest",
    "ReceiptsUploadResponse",
]

from .v1__receipts_get import (
    ReceiptsGetRequest,
    ReceiptsGetResponse,
)
from .v1__receipts_seller_list import (
    ReceiptsSellerListReceipt,
    ReceiptsSellerListRequest,
    ReceiptsSellerListResponse,
)
from .v1__receipts_upload import (
    ReceiptsUploadRequest,
    ReceiptsUploadResponse,
)
