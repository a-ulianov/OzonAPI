"""Описывает модели методов раздела Отмены заказов.
https://docs.ozon.ru/api/seller/#tag/CancellationAPI
"""
__all__ = [
    "ConditionalCancellationListRequest",
    "ConditionalCancellationListFilters",
    "ConditionalCancellationListWith",
    "ConditionalCancellationListResponse",
    "ConditionalCancellationItem",
    "ConditionalCancellationReason",
    "ConditionalCancellationState",
    "ConditionalCancellationApproveRequest",
    "ConditionalCancellationApproveResponse",
    "ConditionalCancellationRejectRequest",
    "ConditionalCancellationRejectResponse",
    "CancelReason",
    "CancelReasonListResponse",
    "CancelReasonListByOrderRequest",
    "CancelReasonListByOrderResponse",
    "CancelReasonListByPostingRequest",
    "CancelReasonListByPostingResponse",
]

from .base import CancelReason
from .v1__cancel_reason_list import (
    CancelReasonListResponse,
)
from .v1__cancel_reason_list_by_order import (
    CancelReasonListByOrderRequest,
    CancelReasonListByOrderResponse,
)
from .v1__cancel_reason_list_by_posting import (
    CancelReasonListByPostingRequest,
    CancelReasonListByPostingResponse,
)
from .v2__conditional_cancellation_list import (
    ConditionalCancellationItem,
    ConditionalCancellationListFilters,
    ConditionalCancellationListRequest,
    ConditionalCancellationListResponse,
    ConditionalCancellationListWith,
    ConditionalCancellationReason,
    ConditionalCancellationState,
)
from .v2__conditional_cancellation_approve import (
    ConditionalCancellationApproveRequest,
    ConditionalCancellationApproveResponse,
)
from .v2__conditional_cancellation_reject import (
    ConditionalCancellationRejectRequest,
    ConditionalCancellationRejectResponse,
)
