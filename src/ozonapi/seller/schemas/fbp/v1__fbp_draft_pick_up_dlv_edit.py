"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftPickupDlvEdit"""
from typing import Optional

from pydantic import BaseModel, Field

from .v1__fbp_draft_pick_up_create import FbpPickUpDeliveryDetails


class FbpDraftPickUpDlvEditRequest(BaseModel):
    """Схема запроса изменения черновика pick-up поставки.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        pickup_details: Детали pick-up поставки (точка забора)
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    pickup_details: FbpPickUpDeliveryDetails = Field(
        ..., description="Детали pick-up поставки (точка забора)."
    )


class FbpDraftPickUpDlvEditResponse(BaseModel):
    """Схема ответа изменения черновика pick-up поставки.

    Attributes:
        row_version: Версия записи
    """

    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
