"""Описывает модели методов раздела Штрихкоды товаров.
https://docs.ozon.ru/api/seller/?__rr=1#tag/BarcodeAPI
"""
__all__ = [
    "BarcodeAddRequest",
    "BarcodeAddResponse",
    "BarcodeGenerateRequest",
    "BarcodeGenerateResponse",
]

from .v1__barcode_add import BarcodeAddRequest, BarcodeAddResponse
from .v1__barcode_generate import BarcodeGenerateRequest, BarcodeGenerateResponse
