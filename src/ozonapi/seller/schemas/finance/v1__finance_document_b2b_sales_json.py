"""Схемы метода finance_document_b2b_sales_json (продажи юр. лицам в JSON, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class FinanceB2BSalesBuyer(BaseModel):
    """Информация о покупателе — юридическом лице.

    Attributes:
        name: Название компании
        address: Юридический адрес
        inn: ИНН
        kpp: КПП
    """
    name: Optional[str] = Field(None, description="Название компании.")
    address: Optional[str] = Field(None, description="Юридический адрес.")
    inn: Optional[str] = Field(None, description="ИНН.")
    kpp: Optional[str] = Field(None, description="КПП.")


class FinanceB2BSalesInvoiceInfo(BaseModel):
    """Информация о счёте-фактуре.

    Attributes:
        date: Дата счёта-фактуры продавца
        number: Номер счёта-фактуры продавца
        status: Статус УКД или УПД
        type: Тип счёта-фактуры
    """
    date: Optional[str] = Field(
        None, description="Дата счёта-фактуры продавца."
    )
    number: Optional[str] = Field(
        None, description="Номер счёта-фактуры продавца."
    )
    status: Optional[str] = Field(
        None, description="Статус УКД или УПД."
    )
    type: Optional[str] = Field(
        None, description="Тип счёта-фактуры."
    )


class FinanceB2BSalesOperation(BaseModel):
    """Информация об операции в счёте-фактуре.

    Attributes:
        amount: Сумма реализации или возврата
        cost_without_vat: Стоимость товара без НДС
        date: Дата операции
        gtd_number: Номер ГТД
        origin_country: Страна происхождения товара
        posting_number: Номер отправления
        price: Цена реализации или возврата
        quantity: Количество товаров
        rnpt_number: РНПТ
        type: Тип операции
        vat_amount: Сумма НДС
        vat_rate: Ставка НДС
    """
    amount: Optional[float] = Field(
        None, description="Сумма реализации или возврата."
    )
    cost_without_vat: Optional[float] = Field(
        None, description="Стоимость товара без НДС."
    )
    date: Optional[str] = Field(
        None, description="Дата операции."
    )
    gtd_number: Optional[str] = Field(
        None, description="Номер ГТД."
    )
    origin_country: Optional[str] = Field(
        None, description="Страна происхождения товара."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    price: Optional[float] = Field(
        None, description="Цена реализации или возврата."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товаров."
    )
    rnpt_number: Optional[str] = Field(
        None, description="РНПТ."
    )
    type: Optional[str] = Field(
        None, description="Тип операции."
    )
    vat_amount: Optional[float] = Field(
        None, description="Сумма НДС."
    )
    vat_rate: Optional[float] = Field(
        None, description="Ставка НДС."
    )


class FinanceB2BSalesInvoice(BaseModel):
    """Счёт-фактура по продаже юридическому лицу.

    Attributes:
        buyer_info: Информация о покупателе
        currency: Валюта
        currency_code: Код валюты
        info: Информация о счёте-фактуре
        offer_id: Идентификатор товара в системе продавца
        operations: Список операций
        product_name: Название товара
        sku: Идентификатор товара в системе Ozon — SKU
        unit_code: Код условного обозначения единицы измерения
        unit_name: Условное обозначение единицы измерения
    """
    buyer_info: Optional[FinanceB2BSalesBuyer] = Field(
        None, description="Информация о покупателе."
    )
    currency: Optional[str] = Field(None, description="Валюта.")
    currency_code: Optional[int] = Field(None, description="Код валюты.")
    info: Optional[FinanceB2BSalesInvoiceInfo] = Field(
        None, description="Информация о счёте-фактуре."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    operations: Optional[list[FinanceB2BSalesOperation]] = Field(
        None, description="Список операций."
    )
    product_name: Optional[str] = Field(None, description="Название товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    unit_code: Optional[int] = Field(
        None, description="Код условного обозначения единицы измерения."
    )
    unit_name: Optional[str] = Field(
        None, description="Условное обозначение единицы измерения."
    )


class FinanceB2BSalesSellerInfo(BaseModel):
    """Информация о продавце.

    Attributes:
        company_name: Название компании
        inn: ИНН
        kpp: КПП
    """
    company_name: Optional[str] = Field(None, description="Название компании.")
    inn: Optional[str] = Field(None, description="ИНН.")
    kpp: Optional[str] = Field(None, description="КПП.")


class FinanceDocumentB2BSalesJSONRequest(BaseModel):
    """Параметры запроса отчёта по продажам юридическим лицам в формате JSON.

    Attributes:
        date: Отчётный период в формате `YYYY-MM`
    """
    date: str = Field(..., description="Отчётный период в формате `YYYY-MM`.")


class FinanceDocumentB2BSalesJSONResponse(BaseModel):
    """Ответ с отчётом по продажам юридическим лицам в формате JSON.

    Attributes:
        date_from: Дата начала отчётного периода
        date_to: Дата окончания отчётного периода
        invoices: Список счетов-фактур
        seller_info: Информация о продавце
    """
    date_from: Optional[str] = Field(
        None, description="Дата начала отчётного периода."
    )
    date_to: Optional[str] = Field(
        None, description="Дата окончания отчётного периода."
    )
    invoices: Optional[list[FinanceB2BSalesInvoice]] = Field(
        None, description="Список счетов-фактур."
    )
    seller_info: Optional[FinanceB2BSalesSellerInfo] = Field(
        None, description="Информация о продавце."
    )
