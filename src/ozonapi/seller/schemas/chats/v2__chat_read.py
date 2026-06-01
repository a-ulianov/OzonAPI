"""https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatReadV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ChatReadRequest(BaseModel):
    """Схема запроса на отметку сообщений чата как прочитанных (Premium).

    Attributes:
        chat_id: Идентификатор чата
        from_message_id: Идентификатор сообщения, начиная с которого
            отметить сообщения прочитанными
    """

    chat_id: str = Field(
        ..., description="Идентификатор чата."
    )
    from_message_id: int = Field(
        ..., description="Идентификатор сообщения, начиная с которого сообщения "
                         "будут отмечены прочитанными."
    )


class ChatReadResponse(BaseModel):
    """Схема ответа на отметку сообщений чата как прочитанных.

    Attributes:
        unread_count: Количество непрочитанных сообщений после операции
    """

    unread_count: Optional[int] = Field(
        None, description="Количество непрочитанных сообщений после операции."
    )
