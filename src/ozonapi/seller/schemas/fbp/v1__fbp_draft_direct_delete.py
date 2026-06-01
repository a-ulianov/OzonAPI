"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDirectDelete"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import FbpCancellationState


class FbpDraftDirectDeleteRequest(BaseModel):
    """Схема запроса удаления черновика заявки на поставку.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpDraftDirectDeleteResponse(BaseModel):
    """Схема ответа удаления черновика заявки на поставку.

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
