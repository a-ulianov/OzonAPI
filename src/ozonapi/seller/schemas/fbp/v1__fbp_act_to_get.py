"""https://docs.ozon.ru/api/seller/#operation/DeliveryFBPSupply_FbpCheckConsignmentNoteState"""
from typing import Optional

from pydantic import BaseModel, Field


class FbpActToGetRequest(BaseModel):
    """Схема запроса статуса генерации транспортной накладной.

    Attributes:
        supply_id: Идентификатор поставки
        code: Код задания на генерацию
    """

    supply_id: str = Field(..., description="Идентификатор поставки.")
    code: str = Field(..., description="Код задания на генерацию.")


class FbpActToGetResponse(BaseModel):
    """Схема ответа со статусом генерации транспортной накладной.

    Attributes:
        state: Статус генерации (`IN_PROGRESS`, `FINISHED`, `FAILED`)
        label_url: Ссылка на готовую накладную
        error_message: Текст ошибки генерации
    """

    state: Optional[str] = Field(
        None,
        description="Статус генерации (`IN_PROGRESS`, `FINISHED`, `FAILED`; "
                    "набор открытый — тип `str`)."
    )
    label_url: Optional[str] = Field(
        None, description="Ссылка на готовую накладную."
    )
    error_message: Optional[str] = Field(
        None, description="Текст ошибки генерации."
    )
