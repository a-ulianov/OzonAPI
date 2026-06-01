"""Схемы метода invoice_create_or_update (создать/изменить счёт-фактуру, v2)."""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import InvoiceHsCode


class InvoiceCreateOrUpdateRequest(BaseModel):
    """Параметры запроса создания или изменения счёта-фактуры.

    Attributes:
        date: Дата счёта-фактуры в формате RFC3339
        hs_codes: HS-коды товаров
        number: Номер счёта-фактуры (буквы и цифры, до 50 символов)
        posting_number: Номер отправления
        price: Стоимость, указанная в счёте-фактуре (до двух знаков после точки)
        price_currency: Валюта счёта-фактуры (`USD`, `EUR`, `TRY`, `CNY`, `RUB`, `GBP`)
        url: Ссылка на счёт-фактуру, созданная методом `invoice_file_upload()`
    """
    date: str = Field(..., description="Дата счёта-фактуры в формате RFC3339.")
    hs_codes: Optional[list[InvoiceHsCode]] = Field(
        None, description="HS-коды товаров."
    )
    number: Optional[str] = Field(
        None,
        description="Номер счёта-фактуры. Может содержать буквы и цифры, "
                    "максимальная длина — 50 символов."
    )
    posting_number: str = Field(..., description="Номер отправления.")
    price: Optional[float] = Field(
        None,
        description="Стоимость, указанная в счёте-фактуре. Разделитель дробной "
                    "части — точка, до двух знаков после точки."
    )
    price_currency: Optional[str] = Field(
        None,
        description="Валюта счёта-фактуры: `USD` — доллар, `EUR` — евро, "
                    "`TRY` — турецкая лира, `CNY` — юань, `RUB` — рубль, "
                    "`GBP` — фунт стерлингов. Значение по умолчанию — `USD`."
    )
    url: str = Field(
        ...,
        description="Ссылка на счёт-фактуру. Чтобы создать ссылку, используйте "
                    "метод `invoice_file_upload()`."
    )


class InvoiceCreateOrUpdateResponse(BaseModel):
    """Ответ на создание или изменение счёта-фактуры.

    Attributes:
        result: Результат обработки запроса — `true`, если успешно
    """
    result: bool = Field(False, description="Результат обработки запроса.")
