"""Схемы метода chat_send_file (отправить файл в чат, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class ChatSendFileRequest(BaseModel):
    """Параметры запроса отправки файла в чат.

    Attributes:
        base64_content: Файл в виде строки base64
        chat_id: Идентификатор чата
        name: Название файла с расширением
    """
    base64_content: str = Field(..., description="Файл в виде строки base64.")
    chat_id: str = Field(..., description="Идентификатор чата.")
    name: str = Field(..., description="Название файла с расширением.")


class ChatSendFileResponse(BaseModel):
    """Ответ на отправку файла в чат.

    Attributes:
        result: Результат обработки запроса
    """
    result: Optional[str] = Field(
        None, description="Результат обработки запроса."
    )
