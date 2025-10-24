"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetPostingFbsCancelReasonList"""
from pydantic import BaseModel, Field

from .entities import PostingFBSCancelReason


class PostingFBSCancelReasonListItem(PostingFBSCancelReason):
    """Описание причины отмены отправления.

    Attributes:
        id_: Идентификатор причины отмены
        is_available_for_cancellation: Результат отмены отправления (true, если запрос доступен для отмены)
        title: Название категории
        type_id: Инициатор отмены отправления
    """
    is_available_for_cancellation: bool = Field(
        ..., title="Результат отмены отправления (true, если запрос доступен для отмены)."
    )


class PostingFBSCancelReasonListResponse(BaseModel):
    """Возвращает список возможных причин отправлений.

    Attributes:
        result: список возможных причин отправлений
    """
    model_config = {'frozen': True}

    result: list[PostingFBSCancelReasonListItem] = Field(
        ..., description="Cписок возможных причин отправлений."
    )