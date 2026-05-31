"""Схемы метода rating_index_fbs_posting_list (отправления, повлиявшие на индекс, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class RatingIndexFBSPostingListFilter(BaseModel):
    """Фильтр списка отправлений, повлиявших на индекс ошибок.

    Attributes:
        date_from: Дата начала периода
        date_to: Дата конца периода
        posting_numbers: Номера отправлений
    """
    date_from: Optional[str] = Field(
        None, description="Дата начала периода."
    )
    date_to: Optional[str] = Field(
        None, description="Дата конца периода."
    )
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )


class RatingIndexFBSPostingListRequest(BaseModel):
    """Параметры запроса списка отправлений, повлиявших на индекс ошибок.

    Attributes:
        cursor: Указатель для выборки следующих данных
        filter: Фильтр отправлений
        limit: Количество значений в ответе
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: RatingIndexFBSPostingListFilter = Field(
        ..., description="Фильтр отправлений."
    )
    limit: int = Field(..., description="Количество значений в ответе.")


class RatingIndexFBSPostingError(BaseModel):
    """Отправление, повлиявшее на индекс ошибок.

    Attributes:
        charge_percent: Процент стоимости обработки ошибок
        charge_price: Стоимость обработки ошибок
        charge_price_currency_code: Код валюты стоимости обработки ошибок
        delivery_schema: Схема доставки (`FBS`, `rFBS`)
        error_at: Дата, когда возникла ошибка
        has_grace_status: Признак, что у отправления льготный статус
        index: Значение индекса ошибок
        posting_error_type: Тип ошибки отправления
        posting_number: Номер отправления
        product_price: Стоимость товара в отправлении
        product_price_currency_code: Код валюты стоимости товара
    """
    charge_percent: Optional[float] = Field(
        None, description="Процент стоимости обработки ошибок."
    )
    charge_price: Optional[float] = Field(
        None, description="Стоимость обработки ошибок."
    )
    charge_price_currency_code: Optional[str] = Field(
        None, description="Код валюты стоимости обработки ошибок."
    )
    delivery_schema: Optional[str] = Field(
        None, description="Схема доставки: `FBS`, `rFBS`."
    )
    error_at: Optional[str] = Field(
        None, description="Дата, когда возникла ошибка."
    )
    has_grace_status: Optional[bool] = Field(
        None, description="Признак, что у отправления льготный статус."
    )
    index: Optional[float] = Field(
        None, description="Значение индекса ошибок."
    )
    posting_error_type: Optional[str] = Field(
        None, description="Тип ошибки отправления."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    product_price: Optional[float] = Field(
        None, description="Стоимость товара в отправлении."
    )
    product_price_currency_code: Optional[str] = Field(
        None, description="Код валюты стоимости товара."
    )


class RatingIndexFBSPostingListResponse(BaseModel):
    """Ответ со списком отправлений, повлиявших на индекс ошибок.

    Attributes:
        cursor: Указатель для выборки следующих данных
        errors: Отправления, которые повлияли на индекс ошибок
        has_next: Признак наличия следующих данных в выборке
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    errors: Optional[list[RatingIndexFBSPostingError]] = Field(
        None, description="Отправления, которые повлияли на индекс ошибок."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующих данных в выборке."
    )
