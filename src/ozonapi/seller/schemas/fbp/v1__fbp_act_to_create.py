"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpCreateConsignmentNote"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpActToCreateRequest(BaseModel):
    """Схема запроса генерации транспортной накладной.

    Attributes:
        supply_id: Идентификатор поставки
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")


class FbpActToCreateResponse(BaseModel):
    """Схема ответа генерации транспортной накладной.

    Attributes:
        code: Код задания на генерацию (для `fbp_act_to_get()`)
    """

    code: Optional[str] = Field(
        None, description="Код задания на генерацию (для `fbp_act_to_get()`)."
    )
