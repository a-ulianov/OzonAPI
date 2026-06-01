"""Общие вложенные модели раздела Доставка rFBS."""
__all__ = [
    "FbsPostingMoveStatus",
    "FbsPostingMoveStatusResponse",
    "FbsPostingNumbersRequest",
]

from .move_status import FbsPostingMoveStatus, FbsPostingMoveStatusResponse
from .posting_numbers import FbsPostingNumbersRequest
