"""Композиция миксинов методов раздела Доставка rFBS."""
from ...core import APIManager
from .fbs_posting_delivered import FbsPostingDeliveredMixin
from .fbs_posting_delivering import FbsPostingDeliveringMixin
from .fbs_posting_last_mile import FbsPostingLastMileMixin
from .fbs_posting_tracking_number_set import FbsPostingTrackingNumberSetMixin
from .posting_cutoff_set import PostingCutoffSetMixin
from .posting_fbs_timeslot_change_restrictions import (
    PostingFbsTimeslotChangeRestrictionsMixin,
)
from .posting_fbs_timeslot_set import PostingFbsTimeslotSetMixin


class SellerRFBSDeliveryAPI(
    FbsPostingDeliveredMixin,
    FbsPostingDeliveringMixin,
    FbsPostingLastMileMixin,
    FbsPostingTrackingNumberSetMixin,
    PostingCutoffSetMixin,
    PostingFbsTimeslotChangeRestrictionsMixin,
    PostingFbsTimeslotSetMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Доставка rFBS.

    Notes:
        • Добавление трек-номеров, смена статусов доставки (доставляется,
          последняя миля, доставлено), перенос даты доставки и уточнение
          даты отгрузки отправлений rFBS.

    References:
        • https://docs.ozon.ru/api/seller/#tag/RFBSDelivery
    """

    pass
