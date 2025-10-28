"""Описывает модели методов раздела Управление кодами маркировки и сборкой заказов для FBS/rFBS и rFBS.
https://docs.ozon.com/api/seller/?__rr=1#tag/FBSandrFBSMarks
"""
__all__ = [
    "FBSPostingProductExemplarSetExemplar",
    "FBSPostingProductExemplarSetExemplarMark",
    "FBSPostingProductExemplarSetProduct",
    "FBSPostingProductExemplarSetRequest",
    "FBSPostingProductExemplarSetResponse",
]

from .v6__fbs_posting_product_exemplar_set import \
    FBSPostingProductExemplarSetExemplar, FBSPostingProductExemplarSetExemplarMark, FBSPostingProductExemplarSetProduct, \
    FBSPostingProductExemplarSetRequest, FBSPostingProductExemplarSetResponse
