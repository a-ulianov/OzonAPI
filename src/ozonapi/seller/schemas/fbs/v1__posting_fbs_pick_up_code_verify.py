"""Схемы метода posting_fbs_pick_up_code_verify (проверка кода курьера, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFBSPickUpCodeVerifyRequest(BaseModel):
    """Параметры запроса проверки кода курьера.

    Attributes:
        pickup_code: Код курьера
        posting_number: Номер отправления
    """
    pickup_code: str = Field(..., description="Код курьера.")
    posting_number: str = Field(..., description="Номер отправления.")


class PostingFBSPickUpCodeVerifyResponse(BaseModel):
    """Ответ на проверку кода курьера.

    Attributes:
        valid: Признак корректности кода курьера
    """
    valid: Optional[bool] = Field(
        None, description="Признак корректности кода курьера."
    )
