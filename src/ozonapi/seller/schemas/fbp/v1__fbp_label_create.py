"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpCreateLabel"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpLabelCreateRequest(BaseModel):
    """Схема запроса задания на генерацию этикеток.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpLabelCreateResponse(BaseModel):
    """Схема ответа создания задания на генерацию этикеток.

    Attributes:
        code: Код задания на генерацию (для `fbp_label_get()`)
    """

    code: Optional[str] = Field(
        None, description="Код задания на генерацию (для `fbp_label_get()`)."
    )
