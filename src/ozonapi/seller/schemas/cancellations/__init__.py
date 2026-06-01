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
]

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
