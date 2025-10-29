__all__ = ["SellerFBSAssemblyLabelingAPI", ]

from .fbs_posting_product_exemplar_create_or_get import FBSPostingProductExemplarCreateOrGetMixin
from .fbs_posting_product_exemplar_set import FBSPostingProductExemplarSetMixin
from .fbs_posting_product_exemplar_status import FBSPostingProductExemplarStatusMixin


class SellerFBSAssemblyLabelingAPI(
    FBSPostingProductExemplarSetMixin,
    FBSPostingProductExemplarStatusMixin,
    FBSPostingProductExemplarCreateOrGetMixin,
):
    """Реализует методы раздела Управление кодами маркировки и сборкой заказов для FBS/rFBS

    References:
        https://docs.ozon.com/api/seller/?__rr=1#tag/FBSandrFBSMarks
    """
    pass
