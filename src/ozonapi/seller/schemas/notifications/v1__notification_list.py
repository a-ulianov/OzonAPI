"""Схемы метода notification_list (список подключённых URL для уведомлений, v1)."""
from pydantic import BaseModel, Field


class NotificationListType(BaseModel):
    """Тип уведомления, подключённый к URL-адресу.

    Attributes:
        description: Описание типа уведомления
        type: Тип уведомления
    """
    description: str = Field("", description="Описание типа уведомления.")
    type: str = Field("", description="Тип уведомления.")


class NotificationListItem(BaseModel):
    """Подключённый URL-адрес для уведомлений.

    Attributes:
        created_at: Дата подключения URL-адреса
        enable: `true`, если уведомления включены
        id: Идентификатор подключённого URL-адреса
        types: Типы уведомлений, подключённые к URL-адресу
        url: URL-адрес для получения уведомлений
    """
    created_at: str = Field("", description="Дата подключения URL-адреса.")
    enable: bool = Field(False, description="`true`, если уведомления включены.")
    id: int = Field(0, description="Идентификатор подключённого URL-адреса.")
    types: list[NotificationListType] = Field(
        default_factory=list, description="Типы уведомлений, подключённые к URL-адресу."
    )
    url: str = Field("", description="URL-адрес для получения уведомлений.")


class NotificationListResponse(BaseModel):
    """Ответ со списком подключённых URL для уведомлений.

    Attributes:
        urls: Список подключённых URL-адресов
    """
    urls: list[NotificationListItem] = Field(
        default_factory=list, description="Список подключённых URL-адресов."
    )
