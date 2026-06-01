"""Схемы метода return_pass_delete (удаление пропуска для возврата, v1)."""
from typing import Union

from pydantic import BaseModel, Field


class ReturnPassDeleteRequest(BaseModel):
    """Параметры запроса удаления пропуска для возврата.

    Attributes:
        arrival_pass_ids: Идентификаторы пропусков
    """
    arrival_pass_ids: list[Union[int, str]] = Field(
        ..., description="Идентификаторы пропусков."
    )


class ReturnPassDeleteResponse(BaseModel):
    """Ответ на удаление пропуска для возврата.

    Notes:
        • Тело ответа отсутствует — успешное удаление возвращает код 200.
    """
