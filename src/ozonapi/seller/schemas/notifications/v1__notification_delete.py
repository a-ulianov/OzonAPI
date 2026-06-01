"""Схемы метода notification_delete (удаление URL для уведомлений, v1)."""
from pydantic import BaseModel, Field


class NotificationDeleteRequest(BaseModel):
    """Параметры запроса удаления URL для уведомлений.

    Attributes:
        id: Идентификатор подключённого URL-адреса
    """
    id: int = Field(..., description="Идентификатор подключённого URL-адреса.")


class NotificationDeleteResponse(BaseModel):
    """Ответ на удаление URL для уведомлений.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
