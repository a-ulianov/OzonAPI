"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderPassStatus"""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderPassStatusRequest(BaseModel):
    """Описывает схему запроса на получение статуса ввода данных о водителе и автомобиле.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции."
    )


class SupplyOrderPassStatusResponse(BaseModel):
    """Описывает схему ответа на запрос статуса ввода данных о водителе и автомобиле.

    Attributes:
        result: Статус ввода данных (строкой)
        errors: Список причин ошибок (строками)
    """
    result: Optional[str] = Field(
        None, description="Статус ввода данных."
    )
    errors: Optional[list[str]] = Field(
        default_factory=list, description="Список причин ошибок."
    )
