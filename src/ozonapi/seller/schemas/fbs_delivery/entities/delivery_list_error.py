"""Общая модель ошибки в ответах списков методов доставки и отгрузок FBS."""
from typing import Optional

from pydantic import BaseModel, Field


class DeliveryListError(BaseModel):
    """Ошибка, которая возникла при обработке запроса списка методов доставки.

    Attributes:
        code: Код ошибки
        description: Описание ошибки
        status: Статус ошибки
    """
    code: Optional[str] = Field(
        None, description="Код ошибки."
    )
    description: Optional[str] = Field(
        None, description="Описание ошибки."
    )
    status: Optional[str] = Field(
        None, description="Статус ошибки."
    )
