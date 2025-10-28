__all__ = ["SellerFBSAssemblyLabelingAPI", ]

from .fbs_posting_product_exemplar_set import FBSPostingProductExemplarSetMixin


class SellerFBSAssemblyLabelingAPI(FBSPostingProductExemplarSetMixin):
    """Реализует методы раздела Управление кодами маркировки и сборкой заказов для FBS/rFBS

    References:
        https://docs.ozon.com/api/seller/?__rr=1#tag/FBSandrFBSMarks
    """
    pass
