"""Композиция миксинов методов раздела Возвраты.

Объединяет методы работы с возвратами FBO/FBS, rFBS и возвратными отгрузками
в единый класс :class:`SellerReturnsAPI`.
"""

from ...core import APIManager
from .returns_list import ReturnsListMixin
from .returns_settings_utilization_history import ReturnsSettingsUtilizationHistoryMixin
from .returns_settings_utilization_info import ReturnsSettingsUtilizationInfoMixin
from .returns_settings_utilization_update import ReturnsSettingsUtilizationUpdateMixin


class SellerReturnsAPI(
    ReturnsListMixin,
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
