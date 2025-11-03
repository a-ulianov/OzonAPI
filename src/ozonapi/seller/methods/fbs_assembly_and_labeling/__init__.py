__all__ = ["SellerFBSAssemblyLabelingAPI", ]

from .fbs_posting_product_exemplar_create_or_get import FBSPostingProductExemplarCreateOrGetMixin
from .fbs_posting_product_exemplar_set import FBSPostingProductExemplarSetMixin
from .fbs_posting_product_exemplar_status import FBSPostingProductExemplarStatusMixin
from .fbs_posting_product_exemplar_update import FBSPostingProductExemplarUpdateMixin
from .fbs_posting_product_exemplar_validate import FBSPostingProductExemplarValidateMixin
from .posting_fbs_ship import PostingFBSShipMixin
from .posting_fbs_ship_package import PostingFBSShipPackageMixin


class SellerFBSAssemblyLabelingAPI(
    FBSPostingProductExemplarCreateOrGetMixin,
    FBSPostingProductExemplarSetMixin,
    FBSPostingProductExemplarStatusMixin,
    FBSPostingProductExemplarUpdateMixin,
    FBSPostingProductExemplarValidateMixin,
    PostingFBSShipMixin,
    PostingFBSShipPackageMixin,
):
    """Реализует методы раздела Управление кодами маркировки и сборкой заказов для FBS/rFBS

    References:
        https://docs.ozon.com/api/seller/?__rr=1#tag/FBSandrFBSMarks
    """
    pass
