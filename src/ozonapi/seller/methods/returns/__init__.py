"""Композиция миксинов методов раздела Возвраты.

Объединяет методы работы с возвратами FBO/FBS, rFBS и возвратными отгрузками
в единый класс :class:`SellerReturnsAPI`.
"""

from ...core import APIManager
from .return_giveout_barcode import ReturnGiveoutBarcodeMixin
from .return_giveout_barcode_reset import ReturnGiveoutBarcodeResetMixin
from .return_giveout_get_pdf import ReturnGiveoutGetPDFMixin
from .return_giveout_get_png import ReturnGiveoutGetPNGMixin
from .return_giveout_info import ReturnGiveoutInfoMixin
from .return_giveout_is_enabled import ReturnGiveoutIsEnabledMixin
from .return_giveout_list import ReturnGiveoutListMixin
from .returns_company_fbs_info import ReturnsCompanyFbsInfoMixin
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
    ReturnGiveoutBarcodeMixin,
    ReturnGiveoutBarcodeResetMixin,
    ReturnGiveoutGetPDFMixin,
    ReturnGiveoutGetPNGMixin,
    ReturnGiveoutInfoMixin,
    ReturnGiveoutIsEnabledMixin,
    ReturnGiveoutListMixin,
    ReturnsCompanyFbsInfoMixin,
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
