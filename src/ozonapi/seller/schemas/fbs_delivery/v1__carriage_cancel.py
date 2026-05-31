"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageCancel"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageCancelRequest(BaseModel):
    """Описывает схему запроса на удаление отгрузки.

    Attributes:
        carriage_id: Идентификатор отгрузки
    """
    carriage_id: int = Field(
        ..., description="Идентификатор отгрузки."
    )


class CarriageCancelResponse(BaseModel):
    """Описывает схему ответа на запрос удаления отгрузки.

    Attributes:
        carriage_status: Статус отгрузки
        error: Описание ошибки
    """
    carriage_status: Optional[str] = Field(
        None, description="Статус отгрузки."
    )
    error: Optional[str] = Field(
        None, description="Описание ошибки."
    )
