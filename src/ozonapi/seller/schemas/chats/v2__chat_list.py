"""Схемы метода chat_list_v2 (список чатов, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ChatListFilter


class ChatListV2Request(BaseModel):
    """Параметры запроса списка чатов (версия 2).

    Attributes:
        filter: Фильтр списка чатов
        limit: Количество значений в ответе
        offset: Количество пропускаемых элементов
    """
    filter: Optional[ChatListFilter] = Field(
        None, description="Фильтр списка чатов."
    )
    limit: int = Field(..., description="Количество значений в ответе.")
    offset: Optional[int] = Field(
        None, description="Количество элементов, которое будет пропущено в ответе."
    )


class ChatListV2Item(BaseModel):
    """Информация о чате в списке (версия 2).

    Attributes:
        chat_id: Идентификатор чата
        chat_status: Статус чата
        chat_type: Тип чата
        created_at: Дата создания чата
        first_unread_message_id: Идентификатор первого непрочитанного сообщения
        last_message_id: Идентификатор последнего сообщения
        unread_count: Количество непрочитанных сообщений
    """
    chat_id: Optional[str] = Field(
        None, description="Идентификатор чата."
    )
    chat_status: Optional[str] = Field(
        None, description="Статус чата."
    )
    chat_type: Optional[str] = Field(
        None, description="Тип чата."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания чата."
    )
    first_unread_message_id: Optional[int] = Field(
        None, description="Идентификатор первого непрочитанного сообщения."
    )
    last_message_id: Optional[int] = Field(
        None, description="Идентификатор последнего сообщения."
    )
    unread_count: Optional[int] = Field(
        None, description="Количество непрочитанных сообщений."
    )


class ChatListV2Response(BaseModel):
    """Ответ со списком чатов (версия 2).

    Attributes:
        chats: Данные чатов
        total_chats_count: Общее количество чатов
        total_unread_count: Общее количество непрочитанных сообщений
    """
    chats: Optional[list[ChatListV2Item]] = Field(
        None, description="Данные чатов."
    )
    total_chats_count: Optional[int] = Field(
        None, description="Общее количество чатов."
    )
    total_unread_count: Optional[int] = Field(
        None, description="Общее количество непрочитанных сообщений."
    )
