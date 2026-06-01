"""Описывает модели методов раздела Накладные.
https://docs.ozon.ru/api/seller/#tag/SupplierAPI
"""
__all__ = [
    "InvoiceCreateOrUpdateRequest",
    "InvoiceCreateOrUpdateResponse",
    "InvoiceDeleteRequest",
    "InvoiceDeleteResponse",
    "InvoiceFileUploadRequest",
    "InvoiceFileUploadResponse",
    "InvoiceGetRequest",
    "InvoiceGetResponse",
    "InvoiceGetResult",
    "InvoiceHsCode",
]

from .entities import InvoiceHsCode
from .v1__invoice_delete import (
    InvoiceDeleteRequest,
    InvoiceDeleteResponse,
)
from .v1__invoice_file_upload import (
    InvoiceFileUploadRequest,
    InvoiceFileUploadResponse,
)
from .v2__invoice_create_or_update import (
    InvoiceCreateOrUpdateRequest,
    InvoiceCreateOrUpdateResponse,
)
from .v2__invoice_get import (
    InvoiceGetRequest,
    InvoiceGetResponse,
    InvoiceGetResult,
)
