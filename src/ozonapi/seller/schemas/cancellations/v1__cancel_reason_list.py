"""https://docs.ozon.ru/api/seller/#operation/CancelReasonList"""
from pydantic import AliasChoices, BaseModel, ConfigDict, Field

from .base import CancelReason


class CancelReasonListResponse(BaseModel):
    """Схема ответа со списком причин отмены заказов.

    Notes:
        • Документация Ozon объявляет ключ верхнего уровня `reasons`, однако
          реальный API может возвращать тот же массив под ключом `result`
          (известная неточность swagger). Поле принимает оба ключа.

    Attributes:
        reasons: Список причин отмены
    """

    model_config = ConfigDict(populate_by_name=True)

    reasons: list[CancelReason] = Field(
        default_factory=list, description="Список причин отмены заказов.",
        validation_alias=AliasChoices("reasons", "result")
    )
