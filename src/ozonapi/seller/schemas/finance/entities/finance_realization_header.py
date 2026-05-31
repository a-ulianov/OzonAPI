"""Общая модель заголовка отчёта о реализации."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceRealizationHeader(BaseModel):
    """Заголовок отчёта о реализации товаров.

    Attributes:
        contract_date: Дата договора
        contract_number: Номер договора
        currency_sys_name: Системное название валюты
        doc_amount: Сумма к начислению по документу
        doc_date: Дата формирования документа
        number: Номер документа
        payer_inn: ИНН плательщика
        payer_kpp: КПП плательщика
        payer_name: Наименование плательщика
        receiver_inn: ИНН получателя
        receiver_kpp: КПП получателя
        receiver_name: Наименование получателя
        start_date: Дата начала периода отчёта
        stop_date: Дата конца периода отчёта
    """
    contract_date: Optional[str] = Field(
        None, description="Дата договора."
    )
    contract_number: Optional[str] = Field(
        None, description="Номер договора."
    )
    currency_sys_name: Optional[str] = Field(
        None, description="Системное название валюты."
    )
    doc_amount: Optional[float] = Field(
        None, description="Сумма к начислению по документу."
    )
    doc_date: Optional[str] = Field(
        None, description="Дата формирования документа."
    )
    number: Optional[str] = Field(
        None, description="Номер документа."
    )
    payer_inn: Optional[str] = Field(
        None, description="ИНН плательщика."
    )
    payer_kpp: Optional[str] = Field(
        None, description="КПП плательщика."
    )
    payer_name: Optional[str] = Field(
        None, description="Наименование плательщика."
    )
    receiver_inn: Optional[str] = Field(
        None, description="ИНН получателя."
    )
    receiver_kpp: Optional[str] = Field(
        None, description="КПП получателя."
    )
    receiver_name: Optional[str] = Field(
        None, description="Наименование получателя."
    )
    start_date: Optional[str] = Field(
        None, description="Дата начала периода отчёта."
    )
    stop_date: Optional[str] = Field(
        None, description="Дата конца периода отчёта."
    )
