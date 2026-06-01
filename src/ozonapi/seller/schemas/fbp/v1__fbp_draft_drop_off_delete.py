"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffDelete"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpCancellationState


class FbpDraftDropOffDeleteRequest(BaseModel):
    """Схема запроса удаления черновика для доставки в drop-off пункт.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpDraftDropOffDeleteResponse(BaseModel):
    """Схема ответа удаления черновика для доставки в drop-off пункт.

    Attributes:
        cancellation_state: Состояние отмены
        row_version: Версия записи
    """

    cancellation_state: Optional[FbpCancellationState] = Field(
        None, description="Состояние отмены поставки."
    )
    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
