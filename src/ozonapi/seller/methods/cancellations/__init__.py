"""Композиция миксинов методов раздела Отмены заказов."""
from ...core import APIManager
from .conditional_cancellation_approve import ConditionalCancellationApproveMixin
from .conditional_cancellation_list import ConditionalCancellationListMixin
from .conditional_cancellation_reject import ConditionalCancellationRejectMixin


class SellerCancellationAPI(
    ConditionalCancellationApproveMixin,
    ConditionalCancellationListMixin,
    ConditionalCancellationRejectMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Отмены заказов.

    Notes:
        • Работа с заявками на отмену отправлений rFBS: список, подтверждение, отклонение.

    References:
        • https://docs.ozon.ru/api/seller/#tag/CancellationAPI
    """

    pass
