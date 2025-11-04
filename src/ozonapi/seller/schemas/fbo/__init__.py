"""Описывает модели методов раздела Доставка FBO.
https://docs.ozon.com/api/seller/?#tag/FBO
"""
__all__ = [
    "PostingFilter",
    "PostingFilterWith",
    "PostingFBOListRequest",
    "PostingFBOListResponse",
]

from .v2__posting_fbo_list import PostingFBOListRequest, PostingFBOListResponse
from ..entities.postings import PostingFilter, PostingFilterWith
