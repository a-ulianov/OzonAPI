"""Схемы метода carriage_pass_delete (удаление пропуска для перевозки, v1)."""
from typing import Union

from pydantic import BaseModel, Field


class CarriagePassDeleteRequest(BaseModel):
    """Параметры запроса удаления пропуска для перевозки.

    Attributes:
        arrival_pass_ids: Идентификаторы пропусков
        carriage_id: Идентификатор перевозки
    """
    arrival_pass_ids: list[Union[int, str]] = Field(
        ..., description="Идентификаторы пропусков."
    )
    carriage_id: int = Field(..., description="Идентификатор перевозки.")


class CarriagePassDeleteResponse(BaseModel):
    """Ответ на удаление пропуска для перевозки.

    Notes:
        • Тело ответа отсутствует — успешное удаление возвращает код 200.
    """
