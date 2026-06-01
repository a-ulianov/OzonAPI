"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPDraft_FbpDraftDropOffDlvEdit"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpDraftDropOffDlvEditRequest(BaseModel):
    """Схема запроса редактирования деталей доставки для drop-off черновика.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        drop_off_date: Дата сдачи в drop-off пункт
        drop_off_point_id: Идентификатор drop-off пункта
        drop_off_province_uuid: Идентификатор провинции drop-off пункта
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    drop_off_date: str = Field(
        ..., description="Дата сдачи в drop-off пункт в формате RFC3339."
    )
    drop_off_point_id: int = Field(..., description="Идентификатор drop-off пункта.")
    drop_off_province_uuid: str = Field(
        ..., description="Идентификатор провинции drop-off пункта."
    )


class FbpDraftDropOffDlvEditResponse(BaseModel):
    """Схема ответа редактирования деталей доставки для drop-off черновика.

    Attributes:
        row_version: Версия записи
    """

    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
