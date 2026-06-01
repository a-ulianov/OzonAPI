"""https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatSendMessage"""
from typing import Optional

from pydantic import BaseModel, Field


class ChatSendMessageRequest(BaseModel):
    """Схема запроса на отправку текстового сообщения в чат (Premium).

    Attributes:
        chat_id: Идентификатор чата
        text: Текст сообщения
    """

    chat_id: str = Field(
        ..., description="Идентификатор чата."
    )
    text: str = Field(
        ..., description="Текст сообщения."
    )


class ChatSendMessageResponse(BaseModel):
    """Схема ответа на отправку сообщения в чат.

    Attributes:
        result: Результат обработки запроса
    """

    result: Optional[str] = Field(
        None, description="Результат обработки запроса."
    )
