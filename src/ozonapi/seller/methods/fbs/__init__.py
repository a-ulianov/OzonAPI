__all__ = ["SellerFBSAPI", ]

from .posting_fbs_arbitration import PostingFBSArbitrationMixin
from .posting_fbs_awaiting_delivery import PostingFBSAwaitingDeliveryMixin
from .posting_fbs_cancel import PostingFBSCancelMixin
from .posting_fbs_cancel_reason import PostingFBSCancelReasonMixin
from .posting_fbs_cancel_reason_list import PostingFBSCancelReasonListMixin
from .posting_fbs_get import PostingFBSGetMixin
from .posting_fbs_get_by_barcode import PostingFBSGetByBarcodeMixin
from .posting_fbs_list import PostingFBSListMixin
from .posting_fbs_multiboxqty_set import PostingFBSMultiBoxQtySetMixin
from .posting_fbs_package_label import PostingFBSPackageLabelMixin
from .posting_fbs_package_label_create import PostingFBSPackageLabelCreateMixin
from .posting_fbs_package_label_create_v1 import PostingFBSPackageLabelCreateV1Mixin
from .posting_fbs_package_label_get import PostingFBSPackageLabelGetMixin
from .posting_fbs_pick_up_code_verify import PostingFBSPickUpCodeVerifyMixin
from .posting_fbs_product_cancel import PostingFBSProductCancelMixin
from .posting_fbs_product_change import PostingFBSProductChangeMixin
from .posting_fbs_product_country_list import PostingFBSProductCountryListMixin
from .posting_fbs_product_country_set import PostingFBSProductCountrySetMixin
from .posting_fbs_restrictions import PostingFBSRestrictionsMixin
from .posting_fbs_unfulfilled_list import PostingFBSUnfulfilledListMixin
from .posting_global_etgb import PostingGlobalEtgbMixin
from .posting_unpaid_legal_product_list import PostingUnpaidLegalProductListMixin


class SellerFBSAPI(
    PostingFBSArbitrationMixin,
    PostingFBSAwaitingDeliveryMixin,
    PostingFBSCancelMixin,
    PostingFBSCancelReasonListMixin,
    PostingFBSCancelReasonMixin,
    PostingFBSGetByBarcodeMixin,
    PostingFBSGetMixin,
    PostingFBSListMixin,
    PostingFBSMultiBoxQtySetMixin,
    PostingFBSPackageLabelCreateMixin,
    PostingFBSPackageLabelCreateV1Mixin,
    PostingFBSPackageLabelGetMixin,
    PostingFBSPackageLabelMixin,
    PostingFBSPickUpCodeVerifyMixin,
    PostingFBSProductCancelMixin,
    PostingFBSProductChangeMixin,
    PostingFBSProductCountryListMixin,
    PostingFBSProductCountrySetMixin,
    PostingFBSRestrictionsMixin,
    PostingFBSUnfulfilledListMixin,
    PostingGlobalEtgbMixin,
    PostingUnpaidLegalProductListMixin,
):
    """Реализует методы раздела Обработка заказов FBS и rFBS.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/FBS
    """
    pass