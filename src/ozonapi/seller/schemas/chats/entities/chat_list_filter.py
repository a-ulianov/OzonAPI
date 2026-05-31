"""Общая модель фильтра списка чатов."""
from typing import Optional

from pydantic import BaseModel, Field


class ChatListFilter(BaseModel):
    """Фильтр списка чатов.

    Attributes:
        chat_status: Фильтр по статусу чата (`All`, `Opened`, `Closed`)
        unread_only: Фильтр по чатам с непрочитанными сообщениями
    """
    chat_status: Optional[str] = Field(
        None, description="Фильтр по статусу чата: `All`, `Opened`, `Closed`."
    )
    unread_only: Optional[bool] = Field(
        None, description="Фильтр по чатам с непрочитанными сообщениями."
    )
