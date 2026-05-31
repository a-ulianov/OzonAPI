"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderTimeslotStatus"""
from typing import Optional

from pydantic import BaseModel, Field


class SupplyOrderTimeslotStatusRequest(BaseModel):
    """Описывает схему запроса на получение статуса обновления интервала поставки.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции."
    )


class SupplyOrderTimeslotStatusResponse(BaseModel):
    """Описывает схему ответа на запрос статуса обновления интервала поставки.

    Attributes:
        status: Статус обновления интервала (строкой)
        errors: Список ошибок обновления (строками)
    """
    status: Optional[str] = Field(
        None, description="Статус обновления интервала."
    )
    errors: Optional[list[str]] = Field(
        default_factory=list, description="Список ошибок обновления."
    )
