"""Композиция миксинов методов раздела Накладные.

Объединяет методы работы со счетами-фактурами отправлений
в единый класс :class:`SellerInvoiceAPI`.
"""

from ...core import APIManager
from .invoice_create_or_update import InvoiceCreateOrUpdateMixin
from .invoice_delete import InvoiceDeleteMixin
from .invoice_file_upload import InvoiceFileUploadMixin
from .invoice_get import InvoiceGetMixin


class SellerInvoiceAPI(
    InvoiceCreateOrUpdateMixin,
    InvoiceDeleteMixin,
    InvoiceFileUploadMixin,
    InvoiceGetMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Накладные.

    Notes:
        • Работа со счетами-фактурами отправлений: загрузка файла, создание/изменение,
          получение информации и удаление ссылки.

    References:
        • https://docs.ozon.ru/api/seller/#tag/SupplierAPI
    """

    pass
