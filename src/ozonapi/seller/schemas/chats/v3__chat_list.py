"""Схемы метода chat_list (список чатов, v3)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ChatListFilter


class ChatListRequest(BaseModel):
    """Параметры запроса списка чатов.

    Attributes:
        filter: Фильтр списка чатов
        limit: Количество значений в ответе
        cursor: Указатель для выборки следующих данных
    """
    filter: Optional[ChatListFilter] = Field(
        None, description="Фильтр списка чатов."
    )
    limit: int = Field(..., description="Количество значений в ответе.")
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )


class ChatListDetails(BaseModel):
    """Данные чата.

    Attributes:
        chat_id: Идентификатор чата
        chat_status: Статус чата
        chat_type: Тип чата
        created_at: Дата создания чата
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


class ChatListItem(BaseModel):
    """Информация о чате в списке.

    Attributes:
        chat: Данные чата
        first_unread_message_id: Идентификатор первого непрочитанного сообщения
        last_message_id: Идентификатор последнего сообщения
        unread_count: Количество непрочитанных сообщений
    """
    chat: Optional[ChatListDetails] = Field(
        None, description="Данные чата."
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


class ChatListResponse(BaseModel):
    """Ответ со списком чатов.

    Attributes:
        chats: Данные чатов
        total_unread_count: Общее количество непрочитанных сообщений
        cursor: Указатель для выборки следующих данных
        has_next: Признак наличия следующих данных в выборке
    """
    chats: Optional[list[ChatListItem]] = Field(
        None, description="Данные чатов."
    )
    total_unread_count: Optional[int] = Field(
        None, description="Общее количество непрочитанных сообщений."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующих данных в выборке."
    )
