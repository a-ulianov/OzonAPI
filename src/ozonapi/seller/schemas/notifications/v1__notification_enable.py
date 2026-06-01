"""Схемы метода notification_enable (включение/выключение уведомлений, v1)."""
from pydantic import BaseModel, Field


class NotificationEnableRequest(BaseModel):
    """Параметры запроса включения или выключения уведомлений.

    Attributes:
        enabled: `true`, чтобы включить уведомления; `false`, чтобы выключить
        id: Идентификатор подключённого URL-адреса
    """
    enabled: bool = Field(
        ..., description="`true`, чтобы включить уведомления; `false`, чтобы выключить."
    )
    id: int = Field(..., description="Идентификатор подключённого URL-адреса.")


class NotificationEnableResponse(BaseModel):
    """Ответ на включение или выключение уведомлений.

    Notes:
        • Тело ответа отсутствует — успех подтверждается кодом 200.
    """
