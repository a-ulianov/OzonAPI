"""Схемы метода notification_update (изменение URL для уведомлений, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.notifications import NotificationType


class NotificationUpdateRequest(BaseModel):
    """Параметры запроса изменения URL для уведомлений.

    Attributes:
        id: Идентификатор подключённого URL-адреса
        types: Типы пуш-уведомлений
        url: Новый URL-адрес для получения уведомлений
    """
    id: int = Field(..., description="Идентификатор подключённого URL-адреса.")
    types: Optional[list[NotificationType]] = Field(
        None, description="Типы пуш-уведомлений."
    )
    url: Optional[str] = Field(
        None, description="Новый URL-адрес для получения уведомлений."
    )


class NotificationUpdateResponse(BaseModel):
    """Ответ на изменение URL для уведомлений.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
