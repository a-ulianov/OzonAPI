"""Композиция миксинов методов раздела Работа с пуш-уведомлениями.

Объединяет методы работы с пуш-уведомлениями
в единый класс :class:`SellerNotificationAPI`.
"""

from ...core import APIManager
from .notification_check import NotificationCheckMixin
from .notification_delete import NotificationDeleteMixin
from .notification_enable import NotificationEnableMixin
from .notification_list import NotificationListMixin
from .notification_push_type_list import NotificationPushTypeListMixin
from .notification_set import NotificationSetMixin
from .notification_update import NotificationUpdateMixin


class SellerNotificationAPI(
    NotificationCheckMixin,
    NotificationDeleteMixin,
    NotificationEnableMixin,
    NotificationListMixin,
    NotificationPushTypeListMixin,
    NotificationSetMixin,
    NotificationUpdateMixin,
    APIManager,
):
    """Класс-агрегатор методов раздела Работа с пуш-уведомлениями.

    Notes:
        • Подключение, изменение, удаление и проверка URL-адресов для пуш-уведомлений,
          включение/выключение уведомлений, список подключённых URL и типов уведомлений.

    References:
        • https://docs.ozon.ru/api/seller/#tag/Notification
    """

    pass
