from pydantic import BaseModel, Field

from ....common.enumerations.postings import CancellationType


class PostingFBSCancellation(BaseModel):
    """Информация об отмене.

    Attributes:
        affect_cancellation_rating: Влияние отмены на рейтинг продавца
        cancel_reason: Причина отмены
        cancel_reason_id: Идентификатор причины отмены отправления
        cancellation_initiator: Инициатор отмены
        cancellation_type: Тип отмены отправления
        cancelled_after_ship: Признак отмены после сборки отправления
    """
    affect_cancellation_rating: bool = Field(
        ..., description="Если отмена влияет на рейтинг продавца — true."
    )
    cancel_reason: str = Field(
        ..., description="Причина отмены."
    )
    cancel_reason_id: int = Field(
        ..., description="Идентификатор причины отмены отправления."
    )
    cancellation_initiator: str = Field(
        ..., description="Инициатор отмены."
    )
    cancellation_type: CancellationType = Field(
        ..., description="Тип отмены отправления."
    )
    cancelled_after_ship: bool = Field(
        ..., description="Если отмена произошла после сборки отправления — true."
    )
