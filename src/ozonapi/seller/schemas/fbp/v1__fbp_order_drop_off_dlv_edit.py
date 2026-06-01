"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpOrderDropOffDlvEdit"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpOrderDropOffDlvEditRequest(BaseModel):
    """Схема запроса редактирования поставки на drop-off пункт.

    Attributes:
        supply_id: Идентификатор поставки
        row_version: Версия записи
        drop_off_date: Дата сдачи в drop-off пункт
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    row_version: int = Field(..., description="Версия записи.")
    drop_off_date: str = Field(
        ..., description="Дата сдачи в drop-off пункт в формате RFC3339."
    )


class FbpOrderDropOffDlvEditResponse(BaseModel):
    """Схема ответа редактирования поставки на drop-off пункт.

    Attributes:
        row_version: Версия записи
    """

    row_version: Optional[int] = Field(
        None, description="Версия записи."
    )
