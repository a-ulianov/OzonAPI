"""Схемы метода delivery_check (проверка доступности доставки Ozon, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class DeliveryCheckRequest(BaseModel):
    """Параметры запроса проверки доступности доставки Ozon для покупателя.

    Attributes:
        client_phone: Номер телефона покупателя
    """
    client_phone: str = Field(..., description="Номер телефона покупателя.")


class DeliveryCheckResponse(BaseModel):
    """Ответ на проверку доступности доставки Ozon.

    Attributes:
        is_possible: Признак доступности доставки Ozon для покупателя
    """
    is_possible: Optional[bool] = Field(
        None, description="Признак доступности доставки Ozon для покупателя."
    )
