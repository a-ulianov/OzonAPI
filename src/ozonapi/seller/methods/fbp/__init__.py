__all__ = ["SellerFbpAPI", ]

from .fbp_warehouse_list import FbpWarehouseListMixin
from .fbp_draft_get import FbpDraftGetMixin
from .fbp_draft_list import FbpDraftListMixin
from .fbp_draft_direct_create import FbpDraftDirectCreateMixin
from .fbp_draft_direct_seller_dlv_create import FbpDraftDirectSellerDlvCreateMixin
from .fbp_draft_direct_tpl_dlv_create import FbpDraftDirectTplDlvCreateMixin
from .fbp_draft_direct_seller_dlv_edit import FbpDraftDirectSellerDlvEditMixin
from .fbp_draft_direct_tpl_dlv_edit import FbpDraftDirectTplDlvEditMixin
from .fbp_draft_direct_delete import FbpDraftDirectDeleteMixin
from .fbp_draft_direct_registrate import FbpDraftDirectRegistrateMixin
from .fbp_draft_direct_product_validate import FbpDraftDirectProductValidateMixin
from .fbp_draft_direct_timeslot_get import FbpDraftDirectTimeslotGetMixin
from .fbp_draft_direct_timeslot_edit import FbpDraftDirectTimeslotEditMixin


class SellerFbpAPI(
    FbpWarehouseListMixin,
    FbpDraftGetMixin,
    FbpDraftListMixin,
    FbpDraftDirectCreateMixin,
    FbpDraftDirectSellerDlvCreateMixin,
    FbpDraftDirectTplDlvCreateMixin,
    FbpDraftDirectSellerDlvEditMixin,
    FbpDraftDirectTplDlvEditMixin,
    FbpDraftDirectDeleteMixin,
    FbpDraftDirectRegistrateMixin,
    FbpDraftDirectProductValidateMixin,
    FbpDraftDirectTimeslotGetMixin,
    FbpDraftDirectTimeslotEditMixin,
):
    """Реализует методы раздела FBP (черновики и поставки).

    References:
        https://docs.ozon.ru/api/seller/#tag/DeliveryFBPDraft
    """
    pass
