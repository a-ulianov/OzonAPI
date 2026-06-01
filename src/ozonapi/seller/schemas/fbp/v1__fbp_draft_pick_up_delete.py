"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftPickUpDelete"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpCancellationState


class FbpDraftPickUpDeleteRequest(BaseModel):
    """Схема запроса отмены черновика pick-up поставки.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpDraftPickUpDeleteResponse(BaseModel):
    """Схема ответа отмены черновика pick-up поставки.

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
