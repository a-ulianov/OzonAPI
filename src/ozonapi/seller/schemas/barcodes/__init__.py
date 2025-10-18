"""Описывает модели методов раздела Штрихкоды товаров.
https://docs.ozon.ru/api/seller/?__rr=1#tag/BarcodeAPI
"""
__all__ = [
    "BarcodeAddRequest",
    "BarcodeAddResponse",
    "BarcodeAddItem",
    "BarcodeAddError",
    "BarcodeGenerateRequest",
    "BarcodeGenerateResponse",
    "BarcodeGenerateError",
]

from .v1__barcode_add import BarcodeAddRequest, BarcodeAddResponse, BarcodeAddItem, BarcodeAddError
from .v1__barcode_generate import BarcodeGenerateRequest, BarcodeGenerateResponse, BarcodeGenerateError