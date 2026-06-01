"""Описывает модели методов раздела Отправления.
https://docs.ozon.ru/api/seller/#tag/FboPostingAPI
"""
__all__ = [
    "PostingCancelRequest",
    "PostingCancelResponse",
    "PostingCancelStatusRequest",
    "PostingCancelStatusResponse",
    "PostingMarksIssuedExemplar",
    "PostingMarksNonIssuedExemplar",
    "PostingMarksRequest",
    "PostingMarksResponse",
]

from .v1__posting_cancel import (
    PostingCancelRequest,
    PostingCancelResponse,
)
from .v1__posting_cancel_status import (
    PostingCancelStatusRequest,
    PostingCancelStatusResponse,
)
from .v1__posting_marks import (
    PostingMarksIssuedExemplar,
    PostingMarksNonIssuedExemplar,
    PostingMarksRequest,
    PostingMarksResponse,
)
