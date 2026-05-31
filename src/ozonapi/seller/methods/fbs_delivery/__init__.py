"""Композиция миксинов методов раздела Доставка FBS.

Объединяет методы работы с отгрузками и перевозками FBS (carriage)
в единый класс :class:`SellerFBSDeliveryAPI`.
"""

from ...core import APIManager
from .carriage_act_discrepancy_pdf import CarriageActDiscrepancyPDFMixin
from .carriage_approve import CarriageApproveMixin
from .carriage_cancel import CarriageCancelMixin
from .carriage_create import CarriageCreateMixin
from .carriage_delivery_list import CarriageDeliveryListMixin
from .carriage_delivery_list_v1 import CarriageDeliveryListV1Mixin
from .carriage_get import CarriageGetMixin
from .carriage_set_postings import CarriageSetPostingsMixin
from .posting_carriage_available_list import PostingCarriageAvailableListMixin
from .posting_fbs_act_check_status import PostingFBSActCheckStatusMixin
from .posting_fbs_act_create import PostingFBSActCreateMixin
from .posting_fbs_act_get_barcode_text import PostingFBSActGetBarcodeTextMixin
from .posting_fbs_act_get_postings import PostingFBSActGetPostingsMixin
from .posting_fbs_act_list import PostingFBSActListMixin
from .posting_fbs_digital_act_check_status import PostingFBSDigitalActCheckStatusMixin


class SellerFBSDeliveryAPI(
    CarriageActDiscrepancyPDFMixin,
    CarriageApproveMixin,
    CarriageCancelMixin,
    CarriageCreateMixin,
    CarriageDeliveryListMixin,
    CarriageDeliveryListV1Mixin,
    CarriageGetMixin,
    CarriageSetPostingsMixin,
    PostingCarriageAvailableListMixin,
    PostingFBSActCheckStatusMixin,
    PostingFBSActCreateMixin,
    PostingFBSActGetBarcodeTextMixin,
    PostingFBSActGetPostingsMixin,
    PostingFBSActListMixin,
    PostingFBSDigitalActCheckStatusMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Доставка FBS (отгрузки и перевозки).

    Notes:
        • Объединяет методы создания, подтверждения, изменения состава и удаления
          отгрузок, а также получения информации о перевозках и списков методов доставки.

    References:
        • https://docs.ozon.ru/api/seller/#tag/CarriageAPI
    """

    pass
