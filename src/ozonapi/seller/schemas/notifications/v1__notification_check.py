"""Схемы метода notification_check (проверка URL для уведомлений, v1)."""
from pydantic import BaseModel, Field


class NotificationCheckRequest(BaseModel):
    """Параметры запроса проверки URL для уведомлений.

    Attributes:
        url: URL-адрес для проверки
    """
    url: str = Field(..., description="URL-адрес для проверки.")


class NotificationCheckError(BaseModel):
    """Ошибка проверки URL-адреса.

    Attributes:
        description: Описание ошибки
        type: Тип ошибки (`REQUEST_ERROR`, `REQUEST_TIMEOUT`, `SERVER_FAULT`,
            `STATUS_CODE_NOT_OK`, `EMPTY_BODY` и др.)
    """
    description: str = Field("", description="Описание ошибки.")
    type: str = Field("", description="Тип ошибки.")


class NotificationCheckResponse(BaseModel):
    """Ответ на проверку URL для уведомлений.

    Attributes:
        errors: Список ошибок проверки
        is_active: `true`, если URL-адрес активен и отвечает корректно
    """
    errors: list[NotificationCheckError] = Field(
        default_factory=list, description="Список ошибок проверки."
    )
    is_active: bool = Field(
        False, description="`true`, если URL-адрес активен и отвечает корректно."
    )
