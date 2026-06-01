"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpGetLabel"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpLabelGetRequest(BaseModel):
    """Схема запроса статуса задания на генерацию этикеток.

    Attributes:
        supply_id: Идентификатор поставки
        code: Код задания на генерацию
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    code: str = Field(..., description="Код задания на генерацию.")


class FbpLabelGetResponse(BaseModel):
    """Схема ответа со статусом задания на генерацию этикеток.

    Attributes:
        state: Статус генерации (`IN_PROGRESS`, `FINISHED`, `FAILED`)
        label_url: Ссылка на готовые этикетки
    """

    state: Optional[str] = Field(
        None,
        description="Статус генерации (`IN_PROGRESS`, `FINISHED`, `FAILED`; "
                    "набор открытый — тип `str`)."
    )
    label_url: Optional[str] = Field(
        None, description="Ссылка на готовые этикетки."
    )
