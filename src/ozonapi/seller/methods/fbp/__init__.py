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
from .fbp_draft_pick_up_create import FbpDraftPickUpCreateMixin
from .fbp_draft_pick_up_delete import FbpDraftPickUpDeleteMixin
from .fbp_draft_pick_up_dlv_edit import FbpDraftPickUpDlvEditMixin
from .fbp_draft_pick_up_registrate import FbpDraftPickUpRegistrateMixin
from .fbp_draft_pick_up_product_validate import FbpDraftPickUpProductValidateMixin
from .fbp_order_direct_cancel import FbpOrderDirectCancelMixin
from .fbp_order_direct_seller_dlv_edit import FbpOrderDirectSellerDlvEditMixin
from .fbp_order_direct_timeslot_edit import FbpOrderDirectTimeslotEditMixin
from .fbp_order_direct_timeslot_list import FbpOrderDirectTimeslotListMixin
from .fbp_order_drop_off_cancel import FbpOrderDropOffCancelMixin
from .fbp_order_drop_off_dlv_edit import FbpOrderDropOffDlvEditMixin
from .fbp_order_drop_off_timetable import FbpOrderDropOffTimetableMixin
from .fbp_order_pick_up_cancel import FbpOrderPickUpCancelMixin
from .fbp_order_pick_up_dlv_edit import FbpOrderPickUpDlvEditMixin


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
    FbpDraftPickUpCreateMixin,
    FbpDraftPickUpDeleteMixin,
    FbpDraftPickUpDlvEditMixin,
    FbpDraftPickUpRegistrateMixin,
    FbpDraftPickUpProductValidateMixin,
    FbpOrderDirectCancelMixin,
    FbpOrderDirectSellerDlvEditMixin,
    FbpOrderDirectTimeslotEditMixin,
    FbpOrderDirectTimeslotListMixin,
    FbpOrderDropOffCancelMixin,
    FbpOrderDropOffDlvEditMixin,
    FbpOrderDropOffTimetableMixin,
    FbpOrderPickUpCancelMixin,
    FbpOrderPickUpDlvEditMixin,
):
    """Реализует методы раздела FBP (черновики и поставки).

    References:
        https://docs.ozon.ru/api/seller/#tag/DeliveryFBPDraft
    """
    pass
