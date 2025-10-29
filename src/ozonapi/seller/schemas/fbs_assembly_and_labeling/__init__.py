"""Описывает модели методов раздела Управление кодами маркировки и сборкой заказов для FBS/rFBS и rFBS.
https://docs.ozon.com/api/seller/?__rr=1#tag/FBSandrFBSMarks
"""
__all__ = [
    "FBSPostingProductExemplarSetExemplar",
    "FBSPostingProductExemplarSetProduct",
    "FBSPostingProductExemplarSetRequest",
    "FBSPostingProductExemplarSetResponse",
    "FBSPostingProductExemplarStatusRequest",
    "FBSPostingProductExemplarStatusResponse",
    "FBSPostingProductExemplarCreateOrGetRequest",
    "FBSPostingProductExemplarCreateOrGetResponse",
    "PostingProduct",
    "ProductExemplar",
    "ProductExemplarMark",
]

from .entities import ProductExemplar, ProductExemplarMark, PostingProduct
from .v5__fbs_posting_product_exemplar_status import FBSPostingProductExemplarStatusResponse, \
    FBSPostingProductExemplarStatusRequest
from .v6__fbs_posting_product_exemplar_create_or_get import FBSPostingProductExemplarCreateOrGetResponse, \
    FBSPostingProductExemplarCreateOrGetRequest
from .v6__fbs_posting_product_exemplar_set import \
    FBSPostingProductExemplarSetExemplar, FBSPostingProductExemplarSetProduct, \
    FBSPostingProductExemplarSetRequest, FBSPostingProductExemplarSetResponse
