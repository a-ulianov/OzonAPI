"""Общая модель денежной суммы в разделе Возвраты."""
from typing import Optional

from pydantic import BaseModel, Field


class ReturnsMoney(BaseModel):
    """Денежная сумма.

    Attributes:
        price: Стоимость
        currency_code: Валюта
    """
    price: Optional[float] = Field(
        None, description="Стоимость."
    )
    currency_code: Optional[str] = Field(
        None, description="Валюта."
    )
