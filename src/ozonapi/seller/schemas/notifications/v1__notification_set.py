"""Схемы метода notification_set (подключение URL для уведомлений, v1)."""
from pydantic import BaseModel, Field

from ...common.enumerations.notifications import NotificationType


class NotificationSetRequest(BaseModel):
    """Параметры запроса подключения URL для уведомлений.

    Attributes:
        types: Типы пуш-уведомлений, которые будут отправляться на URL
        url: URL-адрес для получения уведомлений
    """
    types: list[NotificationType] = Field(
        ..., description="Типы пуш-уведомлений, которые будут отправляться на URL."
    )
    url: str = Field(..., description="URL-адрес для получения уведомлений.")


class NotificationSetResponse(BaseModel):
    """Ответ на подключение URL для уведомлений.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
