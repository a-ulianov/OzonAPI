"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageEttnStatus"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageEttnStatusRequest(BaseModel):
    """Описывает схему запроса на получение статуса проверки электронной ТТН.

    Attributes:
        carriage_id: Идентификатор перевозки
    """
    carriage_id: int = Field(
        ..., description="Идентификатор перевозки."
    )


class CarriageEttnStatusResponse(BaseModel):
    """Описывает схему ответа на запрос статуса проверки электронной ТТН.

    Attributes:
        status: Статус проверки электронной ТТН на прослеживаемой отгрузке
        errors: Ошибки проверки электронной ТТН на прослеживаемой отгрузке
    """
    status: Optional[str] = Field(
        None, description="Статус проверки электронной ТТН на прослеживаемой отгрузке."
    )
    errors: Optional[list[str]] = Field(
        None, description="Ошибки проверки электронной ТТН на прослеживаемой отгрузке."
    )
