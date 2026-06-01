__all__ = ["SellerFbpAPI", ]

from .fbp_warehouse_list import FbpWarehouseListMixin
from .fbp_draft_get import FbpDraftGetMixin
from .fbp_draft_list import FbpDraftListMixin


class SellerFbpAPI(
    FbpWarehouseListMixin,
    FbpDraftGetMixin,
    FbpDraftListMixin,
):
    """Реализует методы раздела FBP (черновики и поставки).

    References:
        https://docs.ozon.ru/api/seller/#tag/DeliveryFBPDraft
    """
    pass
