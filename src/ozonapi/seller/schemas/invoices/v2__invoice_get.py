"""Схемы метода invoice_get (информация о счёте-фактуре, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import InvoiceHsCode


class InvoiceGetRequest(BaseModel):
    """Параметры запроса информации о счёте-фактуре.

    Attributes:
        posting_number: Номер отправления
    """
    posting_number: str = Field(..., description="Номер отправления.")


class InvoiceGetResult(BaseModel):
    """Информация о счёте-фактуре.

    Attributes:
        date: Дата загрузки счёта-фактуры
        file_url: Ссылка на счёт-фактуру
        hs_codes: HS-коды товаров
        number: Номер счёта-фактуры
        price: Стоимость, указанная в счёте-фактуре
        price_currency: Валюта счёта-фактуры
    """
    date: Optional[str] = Field(None, description="Дата загрузки счёта-фактуры.")
    file_url: Optional[str] = Field(None, description="Ссылка на счёт-фактуру.")
    hs_codes: Optional[list[InvoiceHsCode]] = Field(
        None, description="HS-коды товаров."
    )
    number: Optional[str] = Field(None, description="Номер счёта-фактуры.")
    price: Optional[float] = Field(
        None, description="Стоимость, указанная в счёте-фактуре."
    )
    price_currency: Optional[str] = Field(None, description="Валюта счёта-фактуры.")


class InvoiceGetResponse(BaseModel):
    """Ответ с информацией о счёте-фактуре.

    Attributes:
        result: Информация о счёте-фактуре
    """
    result: Optional[InvoiceGetResult] = Field(
        None, description="Информация о счёте-фактуре."
    )
