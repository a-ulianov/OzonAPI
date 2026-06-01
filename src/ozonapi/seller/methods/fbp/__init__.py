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
from .fbp_draft_drop_off_create import FbpDraftDropOffCreateMixin
from .fbp_draft_drop_off_delete import FbpDraftDropOffDeleteMixin
from .fbp_draft_drop_off_dlv_edit import FbpDraftDropOffDlvEditMixin
from .fbp_draft_drop_off_registrate import FbpDraftDropOffRegistrateMixin
from .fbp_draft_drop_off_province_list import FbpDraftDropOffProvinceListMixin
from .fbp_draft_drop_off_point_list import FbpDraftDropOffPointListMixin
from .fbp_draft_drop_off_point_timetable import FbpDraftDropOffPointTimetableMixin
from .fbp_draft_drop_off_product_validate import FbpDraftDropOffProductValidateMixin


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
    FbpDraftDropOffCreateMixin,
    FbpDraftDropOffDeleteMixin,
    FbpDraftDropOffDlvEditMixin,
    FbpDraftDropOffRegistrateMixin,
    FbpDraftDropOffProvinceListMixin,
    FbpDraftDropOffPointListMixin,
    FbpDraftDropOffPointTimetableMixin,
    FbpDraftDropOffProductValidateMixin,
):
    """Реализует методы раздела FBP (черновики и поставки).

    References:
        https://docs.ozon.ru/api/seller/#tag/DeliveryFBPDraft
    """
    pass
