__all__ = ["SellerFBSAPI", ]

from .posting_fbs_get import PostingFBSGetMixin
from .posting_fbs_get_by_barcode import PostingFBSGetByBarcodeMixin
from .posting_fbs_list import PostingFBSListMixin
from .posting_fbs_multiboxqty_set import PostingFBSMultiBoxQtySetMixin
from .posting_fbs_product_change import PostingFBSProductChangeMixin
from .posting_fbs_product_country_list import PostingFBSProductCountryListMixin
from .posting_fbs_product_country_set import PostingFBSProductCountrySetMixin
from .posting_fbs_restrictions import PostingFBSRestrictionsMixin
from .posting_fbs_unfulfilled_list import PostingFBSUnfulfilledListMixin


class SellerFBSAPI(
    PostingFBSGetByBarcodeMixin,
    PostingFBSGetMixin,
    PostingFBSListMixin,
    PostingFBSMultiBoxQtySetMixin,
    PostingFBSProductChangeMixin,
    PostingFBSProductCountryListMixin,
    PostingFBSProductCountrySetMixin,
    PostingFBSRestrictionsMixin,
    PostingFBSUnfulfilledListMixin,
):
    """Реализует методы раздела Обработка заказов FBS и rFBS.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/FBS
    """
    pass