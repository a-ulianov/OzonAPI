"""Описывает модели методов раздела Работа с пуш-уведомлениями.
https://docs.ozon.ru/api/seller/#tag/Notification
"""
__all__ = [
    "NotificationCheckError",
    "NotificationCheckRequest",
    "NotificationCheckResponse",
    "NotificationDeleteRequest",
    "NotificationDeleteResponse",
    "NotificationEnableRequest",
    "NotificationEnableResponse",
    "NotificationListItem",
    "NotificationListResponse",
    "NotificationListType",
    "NotificationPushType",
    "NotificationPushTypeListResponse",
    "NotificationPushTypeSellerEndpoint",
    "NotificationSetRequest",
    "NotificationSetResponse",
    "NotificationUpdateRequest",
    "NotificationUpdateResponse",
]

from .v1__notification_check import (
    NotificationCheckError,
    NotificationCheckRequest,
    NotificationCheckResponse,
)
from .v1__notification_delete import (
    NotificationDeleteRequest,
    NotificationDeleteResponse,
)
from .v1__notification_enable import (
    NotificationEnableRequest,
    NotificationEnableResponse,
)
from .v1__notification_list import (
    NotificationListItem,
    NotificationListResponse,
    NotificationListType,
)
from .v1__notification_push_type_list import (
    NotificationPushType,
    NotificationPushTypeListResponse,
    NotificationPushTypeSellerEndpoint,
)
from .v1__notification_set import (
    NotificationSetRequest,
    NotificationSetResponse,
)
from .v1__notification_update import (
    NotificationUpdateRequest,
    NotificationUpdateResponse,
)
