from pydantic import BaseModel, Field

from src.ozonapi.seller.common.enumerations.postings import CancellationReasonTypeId


class PostingCancelReason(BaseModel):
    """Базовая схема описания причины отмены отправления.

    Attributes:
        id_: Идентификатор причины отмены
        title: Название категории
        type_id: Инициатор отмены отправления
    """
    model_config = {'populate_by_name': True}

    id_: int = Field(
        ..., description="Идентификатор причины отмены.",
        alias="id",
    )
    title: str = Field(
        ..., description="Название категории.",
    )
    type_id: CancellationReasonTypeId = Field(
        ..., description="Инициатор отмены отправления.",
    )


class PostingCancelReasonListItem(PostingCancelReason):
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
