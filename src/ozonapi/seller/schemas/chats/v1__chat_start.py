"""https://docs.ozon.ru/api/seller/#operation/ChatAPI_ChatStart"""
from typing import Optional

from pydantic import BaseModel, Field


class ChatStartRequest(BaseModel):
    """Схема запроса на создание нового чата (Premium).

    Attributes:
        posting_number: Номер отправления, по которому создаётся чат
    """

    posting_number: str = Field(
        ..., description="Номер отправления, по которому создаётся чат."
    )


class ChatStartResult(BaseModel):
    """Результат создания чата.

    Attributes:
        chat_id: Идентификатор созданного чата
    """

    chat_id: Optional[str] = Field(
        None, description="Идентификатор созданного чата."
    )


class ChatStartResponse(BaseModel):
    """Схема ответа на создание нового чата.

    Attributes:
        result: Результат создания чата
    """

    result: Optional[ChatStartResult] = Field(
        None, description="Результат создания чата."
    )
