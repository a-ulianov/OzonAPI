"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbpPosting"""
from typing import Optional

from pydantic import BaseModel, Field


class PostingFbpGetRequest(BaseModel):
    """Схема запроса информации об отправлении FBP.

    Attributes:
        posting_number: Номер отправления
    """

    posting_number: str = Field(..., description="Номер отправления.")


class PostingFbpGetMoney(BaseModel):
    """Денежная сумма отправления FBP.

    Attributes:
        amount: Сумма (строка)
        currency: Код валюты
    """

    amount: Optional[str] = Field(None, description="Сумма (строка).")
    currency: Optional[str] = Field(None, description="Код валюты.")


class PostingFbpGetAnalyticsData(BaseModel):
    """Аналитические данные отправления FBP.

    Attributes:
        city: Город доставки
        delivery_date_begin: Начало периода доставки
        delivery_date_end: Конец периода доставки
        delivery_type: Тип доставки
        region: Регион доставки
        warehouse_id: Идентификатор склада
    """

    city: Optional[str] = Field(None, description="Город доставки.")
    delivery_date_begin: Optional[str] = Field(
        None, description="Начало периода доставки в формате RFC3339."
    )
    delivery_date_end: Optional[str] = Field(
        None, description="Конец периода доставки в формате RFC3339."
    )
    delivery_type: Optional[str] = Field(None, description="Тип доставки.")
    region: Optional[str] = Field(None, description="Регион доставки.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class PostingFbpGetCancellation(BaseModel):
    """Информация об отмене отправления FBP.

    Attributes:
        cancel_reason: Причина отмены
        cancel_reason_id: Идентификатор причины отмены
        cancellation_initiator: Инициатор отмены
        cancellation_type: Тип отмены
    """

    cancel_reason: Optional[str] = Field(None, description="Причина отмены.")
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены."
    )
    cancellation_initiator: Optional[str] = Field(
        None, description="Инициатор отмены."
    )
    cancellation_type: Optional[str] = Field(None, description="Тип отмены.")


class PostingFbpGetFinancialAction(BaseModel):
    """Акция, применённая к товару отправления FBP.

    Attributes:
        action_id: Идентификатор акции
        action_type: Тип акции
        date_from: Начало действия акции
        date_to: Конец действия акции
        description: Описание акции
        discount_percent: Процент скидки
        discount_value: Размер скидки
    """

    action_id: Optional[int] = Field(None, description="Идентификатор акции.")
    action_type: Optional[str] = Field(None, description="Тип акции.")
    date_from: Optional[str] = Field(
        None, description="Начало действия акции в формате RFC3339."
    )
    date_to: Optional[str] = Field(
        None, description="Конец действия акции в формате RFC3339."
    )
    description: Optional[str] = Field(None, description="Описание акции.")
    discount_percent: Optional[float] = Field(None, description="Процент скидки.")
    discount_value: Optional[float] = Field(None, description="Размер скидки.")


class PostingFbpGetCommission(BaseModel):
    """Комиссия по товару отправления FBP.

    Attributes:
        amount: Сумма комиссии
        payout: Выплата
        percent: Процент комиссии
    """

    amount: Optional[float] = Field(None, description="Сумма комиссии.")
    payout: Optional[float] = Field(None, description="Выплата.")
    percent: Optional[float] = Field(None, description="Процент комиссии.")


class PostingFbpGetFinancialProduct(BaseModel):
    """Финансовые данные по товару отправления FBP.

    Attributes:
        actions: Применённые к товару акции
        commissions_price: Цена комиссий
        customer_price: Цена для покупателя
        old_price: Цена до скидок
        posting_commission: Комиссия за отправление
        quantity: Количество товара
        return_commission: Комиссия за возврат
        seller_price: Цена продавца
        sku: Идентификатор товара в системе Ozon — SKU
        total_discount_percent: Суммарный процент скидки
        total_discount_value: Суммарный размер скидки
    """

    actions: list[PostingFbpGetFinancialAction] = Field(
        default_factory=list, description="Применённые к товару акции."
    )
    commissions_price: Optional[PostingFbpGetMoney] = Field(
        None, description="Цена комиссий."
    )
    customer_price: Optional[PostingFbpGetMoney] = Field(
        None, description="Цена для покупателя."
    )
    old_price: Optional[float] = Field(None, description="Цена до скидок.")
    posting_commission: Optional[PostingFbpGetCommission] = Field(
        None, description="Комиссия за отправление."
    )
    quantity: Optional[int] = Field(None, description="Количество товара.")
    return_commission: Optional[PostingFbpGetCommission] = Field(
        None, description="Комиссия за возврат."
    )
    seller_price: Optional[PostingFbpGetMoney] = Field(
        None, description="Цена продавца."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    total_discount_percent: Optional[float] = Field(
        None, description="Суммарный процент скидки."
    )
    total_discount_value: Optional[float] = Field(
        None, description="Суммарный размер скидки."
    )


class PostingFbpGetFinancialData(BaseModel):
    """Финансовые данные отправления FBP.

    Attributes:
        cluster_from: Кластер отправления
        cluster_to: Кластер назначения
        delivery_amount: Стоимость доставки
        products: Финансовые данные по товарам
    """

    cluster_from: Optional[str] = Field(None, description="Кластер отправления.")
    cluster_to: Optional[str] = Field(None, description="Кластер назначения.")
    delivery_amount: Optional[float] = Field(None, description="Стоимость доставки.")
    products: list[PostingFbpGetFinancialProduct] = Field(
        default_factory=list, description="Финансовые данные по товарам."
    )


class PostingFbpGetProduct(BaseModel):
    """Товар отправления FBP.

    Attributes:
        has_imei: Признак наличия IMEI
        marketplace_seller_price: Цена продавца на площадке
        name: Название товара
        offer_id: Артикул товара в системе продавца
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
        weight_max: Максимальный вес товара
    """

    has_imei: Optional[bool] = Field(None, description="Признак наличия IMEI.")
    marketplace_seller_price: Optional[PostingFbpGetMoney] = Field(
        None, description="Цена продавца на площадке."
    )
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Артикул товара в системе продавца."
    )
    quantity: Optional[int] = Field(None, description="Количество товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    weight_max: Optional[float] = Field(None, description="Максимальный вес товара.")


class PostingFbpGetPosting(BaseModel):
    """Отправление FBP.

    Attributes:
        analytics_data: Аналитические данные
        cancellation: Информация об отмене
        financial_data: Финансовые данные
        in_process_at: Дата перехода в обработку
        order_date: Дата заказа
        order_id: Идентификатор заказа
        order_number: Номер заказа
        posting_number: Номер отправления
        products: Товары отправления
        status: Статус отправления
        substatus: Подстатус отправления
        tpl_provider_id: Идентификатор провайдера доставки
    """

    analytics_data: Optional[PostingFbpGetAnalyticsData] = Field(
        None, description="Аналитические данные."
    )
    cancellation: Optional[PostingFbpGetCancellation] = Field(
        None, description="Информация об отмене."
    )
    financial_data: Optional[PostingFbpGetFinancialData] = Field(
        None, description="Финансовые данные."
    )
    in_process_at: Optional[str] = Field(
        None, description="Дата перехода в обработку в формате RFC3339."
    )
    order_date: Optional[str] = Field(
        None, description="Дата заказа в формате RFC3339."
    )
    order_id: Optional[int] = Field(None, description="Идентификатор заказа.")
    order_number: Optional[str] = Field(None, description="Номер заказа.")
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    products: list[PostingFbpGetProduct] = Field(
        default_factory=list, description="Товары отправления."
    )
    status: Optional[int] = Field(
        None, description="Статус отправления (числовой код)."
    )
    substatus: Optional[str] = Field(None, description="Подстатус отправления.")
    tpl_provider_id: Optional[int] = Field(
        None, description="Идентификатор провайдера доставки."
    )


class PostingFbpGetResponse(BaseModel):
    """Схема ответа с информацией об отправлении FBP.

    Attributes:
        posting: Данные отправления
    """

    posting: Optional[PostingFbpGetPosting] = Field(
        None, description="Данные отправления."
    )
