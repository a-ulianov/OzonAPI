"""https://docs.ozon.ru/api/seller/#operation/SellerActionsVoucherGet"""
from typing import Optional

from pydantic import BaseModel, Field


class SellerActionsVoucherGetRequest(BaseModel):
    """Схема запроса файла с промокодами акции.

    Attributes:
        action_id: Идентификатор акции
    """

    action_id: int = Field(
        ..., description="Идентификатор акции."
    )


class SellerActionsVoucherGetResponse(BaseModel):
    """Схема ответа с файлом промокодов акции.

    Attributes:
        file: Ссылка на CSV-файл с промокодами
    """

    file: Optional[str] = Field(
        None, description="Ссылка на CSV-файл с промокодами."
    )
