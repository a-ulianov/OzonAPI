__all__ = ["SellerBarcodeAPI", ]

from .barcode_add import BarcodeAddMixin
from .barcode_generate import BarcodeGenerateMixin


class SellerBarcodeAPI(
    BarcodeAddMixin,
    BarcodeGenerateMixin,
):
    """Реализует методы раздела Штрихкоды товаров.

    References:
        https://docs.ozon.ru/api/seller/#tag/BarcodeAPI
    """
    pass