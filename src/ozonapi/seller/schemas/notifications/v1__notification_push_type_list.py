"""Схемы метода notification_push_type_list (типы пуш-уведомлений, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class NotificationPushTypeSellerEndpoint(BaseModel):
    """Подключённый URL-адрес продавца для типа уведомления.

    Attributes:
        id: Идентификатор подключённого URL-адреса
        url: URL-адрес для получения уведомлений
    """
    id: int = Field(0, description="Идентификатор подключённого URL-адреса.")
    url: str = Field("", description="URL-адрес для получения уведомлений.")


class NotificationPushType(BaseModel):
    """Тип пуш-уведомления.

    Attributes:
        description: Описание типа уведомления
        seller_endpoint: Подключённый URL-адрес продавца для этого типа
        type: Тип уведомления
    """
    description: str = Field("", description="Описание типа уведомления.")
    seller_endpoint: Optional[NotificationPushTypeSellerEndpoint] = Field(
        None, description="Подключённый URL-адрес продавца для этого типа."
    )
    type: str = Field("", description="Тип уведомления.")


class NotificationPushTypeListResponse(BaseModel):
    """Ответ со списком типов пуш-уведомлений.

    Attributes:
        types: Список типов пуш-уведомлений
    """
    types: list[NotificationPushType] = Field(
        default_factory=list, description="Список типов пуш-уведомлений."
    )
