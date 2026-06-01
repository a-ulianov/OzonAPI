"""Схемы раздела Доставка rFBS."""
__all__ = [
    "FbsPostingMoveStatus",
    "FbsPostingMoveStatusResponse",
    "FbsPostingNumbersRequest",
    "FbsPostingTrackingNumber",
    "FbsPostingTrackingNumberSetRequest",
    "PostingFbsTimeslotChangeRestrictionsRequest",
    "PostingFbsTimeslotChangeRestrictionsInterval",
    "PostingFbsTimeslotChangeRestrictionsResponse",
    "PostingFbsTimeslotSetNewTimeslot",
    "PostingFbsTimeslotSetRequest",
    "PostingFbsTimeslotSetResponse",
    "PostingCutoffSetRequest",
    "PostingCutoffSetResponse",
]

from .entities import (
    FbsPostingMoveStatus,
    FbsPostingMoveStatusResponse,
    FbsPostingNumbersRequest,
)
from .v2__fbs_posting_tracking_number_set import (
    FbsPostingTrackingNumber,
    FbsPostingTrackingNumberSetRequest,
)
from .v1__posting_fbs_timeslot_change_restrictions import (
    PostingFbsTimeslotChangeRestrictionsInterval,
    PostingFbsTimeslotChangeRestrictionsRequest,
    PostingFbsTimeslotChangeRestrictionsResponse,
)
from .v1__posting_fbs_timeslot_set import (
    PostingFbsTimeslotSetNewTimeslot,
    PostingFbsTimeslotSetRequest,
    PostingFbsTimeslotSetResponse,
)
from .v1__posting_cutoff_set import (
    PostingCutoffSetRequest,
    PostingCutoffSetResponse,
)
