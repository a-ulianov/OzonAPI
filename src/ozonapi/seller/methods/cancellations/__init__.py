"""Композиция миксинов методов раздела Отмены заказов."""
from ...core import APIManager
from .cancel_reason_list import CancelReasonListMixin
from .cancel_reason_list_by_order import CancelReasonListByOrderMixin
from .cancel_reason_list_by_posting import CancelReasonListByPostingMixin
from .conditional_cancellation_approve import ConditionalCancellationApproveMixin
from .conditional_cancellation_list import ConditionalCancellationListMixin
from .conditional_cancellation_reject import ConditionalCancellationRejectMixin


class SellerCancellationAPI(
    CancelReasonListMixin,
    CancelReasonListByOrderMixin,
    CancelReasonListByPostingMixin,
    ConditionalCancellationApproveMixin,
    ConditionalCancellationListMixin,
    ConditionalCancellationRejectMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Отмены заказов.

    Notes:
        • Работа с заявками на отмену отправлений rFBS: список, подтверждение, отклонение.
        • Получение причин отмены заказов и отправлений (общий список и динамические).

    References:
        • https://docs.ozon.ru/api/seller/#tag/CancellationAPI
    """

    pass
