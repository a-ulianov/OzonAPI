from pydantic import BaseModel, Field

from ....common.enumerations.postings import CancellationReasonTypeId


class PostingFBSCancelReason(BaseModel):
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