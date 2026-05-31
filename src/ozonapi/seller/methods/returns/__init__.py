"""Композиция миксинов методов раздела Возвраты.

Объединяет методы работы с возвратами FBO/FBS, rFBS и возвратными отгрузками
в единый класс :class:`SellerReturnsAPI`.
"""

from ...core import APIManager
from .returns_list import ReturnsListMixin
from .returns_rfbs_action_set import ReturnsRfbsActionSetMixin
from .returns_rfbs_compensate import ReturnsRfbsCompensateMixin
from .returns_rfbs_get import ReturnsRfbsGetMixin
from .returns_rfbs_list import ReturnsRfbsListMixin
from .returns_rfbs_receive_return import ReturnsRfbsReceiveReturnMixin
from .returns_rfbs_reject import ReturnsRfbsRejectMixin
from .returns_rfbs_return_money import ReturnsRfbsReturnMoneyMixin
from .returns_rfbs_verify import ReturnsRfbsVerifyMixin
from .returns_settings_utilization_history import ReturnsSettingsUtilizationHistoryMixin
from .returns_settings_utilization_info import ReturnsSettingsUtilizationInfoMixin
from .returns_settings_utilization_update import ReturnsSettingsUtilizationUpdateMixin


class SellerReturnsAPI(
    ReturnsListMixin,
    ReturnsRfbsActionSetMixin,
    ReturnsRfbsCompensateMixin,
    ReturnsRfbsGetMixin,
    ReturnsRfbsListMixin,
    ReturnsRfbsReceiveReturnMixin,
    ReturnsRfbsRejectMixin,
    ReturnsRfbsReturnMoneyMixin,
    ReturnsRfbsVerifyMixin,
    ReturnsSettingsUtilizationHistoryMixin,
    ReturnsSettingsUtilizationInfoMixin,
    ReturnsSettingsUtilizationUpdateMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Возвраты.

    Notes:
        • Объединяет методы получения списка возвратов FBO/FBS и управления настройками
          автоутилизации.

    References:
        • https://docs.ozon.ru/api/seller/#tag/ReturnsAPI
    """

    pass
