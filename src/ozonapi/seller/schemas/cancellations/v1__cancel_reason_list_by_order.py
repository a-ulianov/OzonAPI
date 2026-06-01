"""https://docs.ozon.ru/api/seller/#operation/CancelReasonListByOrder"""
from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base import CancelReason


class CancelReasonListByOrderRequest(BaseModel):
    """Схема запроса динамического списка причин отмены для заказа.

    Attributes:
        order_number: Номер заказа
    """

    order_number: str = Field(
        ..., description="Номер заказа."
    )


class CancelReasonListByOrderResponse(BaseModel):
    """Схема ответа со списком причин отмены для заказа.

    Notes:
        • Поле `reasons` также принимает ключ `result` (неточность swagger).

    Attributes:
        reasons: Список причин отмены
    """

    model_config = ConfigDict(populate_by_name=True)

    reasons: list[CancelReason] = Field(
        default_factory=list, description="Список причин отмены для заказа.",
        validation_alias=AliasChoices("reasons", "result")
    )
