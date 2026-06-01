"""https://docs.ozon.ru/api/seller/#operation/CancelReasonAPI_CancelReasonListByPosting"""
from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base import CancelReason


class CancelReasonListByPostingRequest(BaseModel):
    """Схема запроса динамического списка причин отмены для отправления.

    Attributes:
        posting_number: Номер отправления
    """

    posting_number: str = Field(
        ..., description="Номер отправления."
    )


class CancelReasonListByPostingResponse(BaseModel):
    """Схема ответа со списком причин отмены для отправления.

    Notes:
        • Поле `reasons` также принимает ключ `result` (неточность swagger).

    Attributes:
        reasons: Список причин отмены
    """

    model_config = ConfigDict(populate_by_name=True)

    reasons: list[CancelReason] = Field(
        default_factory=list, description="Список причин отмены для отправления.",
        validation_alias=AliasChoices("reasons", "result")
    )
