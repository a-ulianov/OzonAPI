"""Схемы метода chat_history (история чата, v3)."""
from typing import Optional

from pydantic import BaseModel, Field


class ChatHistoryRequestFilter(BaseModel):
    """Фильтр истории чата.

    Attributes:
        message_ids: Идентификаторы сообщений
    """
    message_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы сообщений."
    )


class ChatHistoryRequest(BaseModel):
    """Параметры запроса истории чата.

    Attributes:
        chat_id: Идентификатор чата
        direction: Направление сортировки сообщений (`Forward`, `Backward`)
        filter: Фильтр истории чата
        from_message_id: Идентификатор сообщения, с которого начинается выборка
        limit: Количество сообщений в ответе
    """
    chat_id: str = Field(..., description="Идентификатор чата.")
    direction: Optional[str] = Field(
        None, description="Направление сортировки сообщений: `Forward`, `Backward`."
    )
    filter: Optional[ChatHistoryRequestFilter] = Field(
        None, description="Фильтр истории чата."
    )
    from_message_id: Optional[int] = Field(
        None, description="Идентификатор сообщения, с которого начинается выборка."
    )
    limit: Optional[int] = Field(
        None, description="Количество сообщений в ответе."
    )


class ChatMessageContext(BaseModel):
    """Контекст сообщения чата.

    Attributes:
        order_number: Номер заказа
        sku: Идентификатор товара в системе Ozon — SKU
    """
    order_number: Optional[str] = Field(
        None, description="Номер заказа."
    )
    sku: Optional[str] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class ChatMessageUser(BaseModel):
    """Участник чата — отправитель сообщения.

    Attributes:
        id: Идентификатор участника чата
        type: Тип участника чата (`Customer`, `Seller`, `Support`)
    """
    id: Optional[str] = Field(
        None, description="Идентификатор участника чата."
    )
    type: Optional[str] = Field(
        None, description="Тип участника чата: `Customer`, `Seller`, `Support`."
    )


class ChatMessage(BaseModel):
    """Сообщение в истории чата.

    Attributes:
        context: Контекст сообщения
        created_at: Дата создания сообщения
        data: Массив с содержимым сообщения
        is_image: Признак, что сообщение содержит изображение
        is_read: Признак, что сообщение прочитано
        message_id: Идентификатор сообщения
        moderate_image_status: Статус модерации изображения
        user: Отправитель сообщения
    """
    context: Optional[ChatMessageContext] = Field(
        None, description="Контекст сообщения."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания сообщения."
    )
    data: Optional[list[str]] = Field(
        None, description="Массив с содержимым сообщения."
    )
    is_image: Optional[bool] = Field(
        None, description="Признак, что сообщение содержит изображение."
    )
    is_read: Optional[bool] = Field(
        None, description="Признак, что сообщение прочитано."
    )
    message_id: Optional[int] = Field(
        None, description="Идентификатор сообщения."
    )
    moderate_image_status: Optional[str] = Field(
        None, description="Статус модерации изображения."
    )
    user: Optional[ChatMessageUser] = Field(
        None, description="Отправитель сообщения."
    )


class ChatHistoryResponse(BaseModel):
    """Ответ с историей чата.

    Attributes:
        has_next: Признак наличия следующих данных в выборке
        messages: Массив сообщений, отсортированный по дате создания
    """
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующих данных в выборке."
    )
    messages: Optional[list[ChatMessage]] = Field(
        None, description="Массив сообщений, отсортированный по дате создания."
    )
