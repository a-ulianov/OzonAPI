"""Схемы метода posting_fbo_list (список отправлений FBO, v3 — канонический)."""
import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class PostingFBOListFilter(BaseModel):
    """Фильтр выборки отправлений FBO (API v3).

    Attributes:
        order_numbers: Номера заказов
        posting_numbers: Номера отправлений
        since: Начало периода
        statuses: Статусы отправлений
        to_: Конец периода
    """
    model_config = ConfigDict(populate_by_name=True)

    order_numbers: Optional[list[str]] = Field(None, description="Номера заказов.")
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )
    since: Optional[str] = Field(
        None, description="Начало периода (RFC3339, например 2026-05-01T00:00:00Z)."
    )
    statuses: Optional[list[str]] = Field(None, description="Статусы отправлений.")
    to_: Optional[str] = Field(
        None, alias="to", description="Конец периода (RFC3339, например 2026-06-01T00:00:00Z)."
    )


class PostingFBOListWith(BaseModel):
    """Дополнительные поля, которые нужно добавить в ответ (API v3).

    Attributes:
        analytics_data: Добавить данные аналитики
        financial_data: Добавить финансовые данные
        legal_info: Добавить юридическую информацию
    """
    analytics_data: Optional[bool] = Field(None, description="Добавить данные аналитики.")
    financial_data: Optional[bool] = Field(
        None, description="Добавить финансовые данные."
    )
    legal_info: Optional[bool] = Field(
        None, description="Добавить юридическую информацию."
    )


class PostingFBOListRequest(BaseModel):
    """Описывает схему запроса списка отправлений FBO (API v3).

    Attributes:
        cursor: Указатель для выборки следующих данных
        filter: Фильтр выборки
        limit: Количество значений в ответе
        sort_dir: Направление сортировки (`ASC` или `DESC`)
        translit: Включить транслитерацию адреса из кириллицы в латиницу
        with_: Дополнительные поля в ответе
    """
    model_config = ConfigDict(populate_by_name=True)

    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: Optional[PostingFBOListFilter] = Field(None, description="Фильтр выборки.")
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки (`ASC` или `DESC`)."
    )
    translit: Optional[bool] = Field(
        None, description="Включить транслитерацию адреса из кириллицы в латиницу."
    )
    with_: Optional[PostingFBOListWith] = Field(
        None, alias="with", description="Дополнительные поля в ответе."
    )


class PostingFBOListAdditionalData(BaseModel):
    """Дополнительные данные отправления.

    Attributes:
        key: Ключ
        value: Значение
    """
    key: Optional[str] = Field(None, description="Ключ.")
    value: Optional[str] = Field(None, description="Значение.")


class PostingFBOListAnalyticsData(BaseModel):
    """Данные аналитики по отправлению.

    Attributes:
        city: Город доставки
        client_delivery_date_begin: Начало интервала доставки покупателю
        client_delivery_date_end: Конец интервала доставки покупателю
        delivery_type: Способ доставки
        is_legal: Признак заказа юридического лица
        is_premium: Признак наличия подписки Premium
        payment_type_group_name: Способ оплаты
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    city: Optional[str] = Field(None, description="Город доставки.")
    client_delivery_date_begin: Optional[datetime.datetime] = Field(
        None, description="Начало интервала доставки покупателю."
    )
    client_delivery_date_end: Optional[datetime.datetime] = Field(
        None, description="Конец интервала доставки покупателю."
    )
    delivery_type: Optional[str] = Field(None, description="Способ доставки.")
    is_legal: Optional[bool] = Field(
        None, description="Признак заказа юридического лица."
    )
    is_premium: Optional[bool] = Field(
        None, description="Признак наличия подписки Premium."
    )
    payment_type_group_name: Optional[str] = Field(None, description="Способ оплаты.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    warehouse_name: Optional[str] = Field(None, description="Название склада.")


class PostingFBOListCancellation(BaseModel):
    """Информация об отмене отправления.

    Attributes:
        cancel_reason: Причина отмены
        cancellation_initiator: Инициатор отмены
        cancellation_type: Тип отмены
    """
    cancel_reason: Optional[str] = Field(None, description="Причина отмены.")
    cancellation_initiator: Optional[str] = Field(
        None, description="Инициатор отмены."
    )
    cancellation_type: Optional[str] = Field(None, description="Тип отмены.")


class PostingFBOListExternalOrder(BaseModel):
    """Информация о внешнем заказе.

    Attributes:
        is_external: Признак внешнего заказа
        platform_name: Название площадки
    """
    is_external: Optional[bool] = Field(None, description="Признак внешнего заказа.")
    platform_name: Optional[str] = Field(None, description="Название площадки.")


class PostingFBOListCommission(BaseModel):
    """Комиссия за товар.

    Attributes:
        amount: Сумма комиссии
        currency: Валюта
        percent: Процент комиссии
    """
    amount: Optional[float] = Field(None, description="Сумма комиссии.")
    currency: Optional[str] = Field(None, description="Валюта.")
    percent: Optional[int] = Field(None, description="Процент комиссии.")


class PostingFBOListFinancialProduct(BaseModel):
    """Финансовые данные по товару.

    Attributes:
        actions: Список акций
        commission: Комиссия за товар
        old_price: Цена до скидок
        payout: Выплата продавцу
        price: Цена товара
        product_id: Идентификатор товара
        total_discount_percent: Процент итоговой скидки
        total_discount_value: Сумма итоговой скидки
    """
    actions: Optional[list[str]] = Field(None, description="Список акций.")
    commission: Optional[PostingFBOListCommission] = Field(
        None, description="Комиссия за товар."
    )
    old_price: Optional[float] = Field(None, description="Цена до скидок.")
    payout: Optional[float] = Field(None, description="Выплата продавцу.")
    price: Optional[float] = Field(None, description="Цена товара.")
    product_id: Optional[int] = Field(None, description="Идентификатор товара.")
    total_discount_percent: Optional[float] = Field(
        None, description="Процент итоговой скидки."
    )
    total_discount_value: Optional[float] = Field(
        None, description="Сумма итоговой скидки."
    )


class PostingFBOListFinancialData(BaseModel):
    """Финансовые данные отправления.

    Attributes:
        cluster_from: Кластер отправления
        cluster_to: Кластер доставки
        products: Финансовые данные по товарам
    """
    cluster_from: Optional[str] = Field(None, description="Кластер отправления.")
    cluster_to: Optional[str] = Field(None, description="Кластер доставки.")
    products: Optional[list[PostingFBOListFinancialProduct]] = Field(
        None, description="Финансовые данные по товарам."
    )


class PostingFBOListLegalInfo(BaseModel):
    """Юридическая информация о покупателе.

    Attributes:
        company_name: Название компании
        inn: ИНН
        kpp: КПП
    """
    company_name: Optional[str] = Field(None, description="Название компании.")
    inn: Optional[str] = Field(None, description="ИНН.")
    kpp: Optional[str] = Field(None, description="КПП.")


class PostingFBOListProductPrice(BaseModel):
    """Цена товара.

    Attributes:
        amount: Сумма
        currency: Валюта
    """
    amount: Optional[str] = Field(None, description="Сумма.")
    currency: Optional[str] = Field(None, description="Валюта.")


class PostingFBOListProduct(BaseModel):
    """Товар в отправлении.

    Attributes:
        digital_codes: Цифровые коды активации
        is_marketplace_buyout: Признак выкупа маркетплейсом
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        price: Цена товара
        quantity: Количество товара
        sku: Идентификатор товара в системе Ozon — SKU
    """
    digital_codes: Optional[list[str]] = Field(
        None, description="Цифровые коды активации."
    )
    is_marketplace_buyout: Optional[bool] = Field(
        None, description="Признак выкупа маркетплейсом."
    )
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[PostingFBOListProductPrice] = Field(None, description="Цена товара.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class PostingFBOListPosting(BaseModel):
    """Отправление FBO (API v3).

    Attributes:
        additional_data: Дополнительные данные
        analytics_data: Данные аналитики
        cancel_reason_id: Идентификатор причины отмены
        cancellation: Информация об отмене
        created_at: Дата и время создания отправления
        external_order: Информация о внешнем заказе
        financial_data: Финансовые данные
        in_process_at: Дата и время начала обработки
        legal_info: Юридическая информация
        order_id: Идентификатор заказа
        order_number: Номер заказа
        posting_number: Номер отправления
        products: Товары в отправлении
        status: Статус отправления
        substatus: Подстатус отправления
    """
    additional_data: Optional[list[PostingFBOListAdditionalData]] = Field(
        None, description="Дополнительные данные."
    )
    analytics_data: Optional[PostingFBOListAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены."
    )
    cancellation: Optional[PostingFBOListCancellation] = Field(
        None, description="Информация об отмене."
    )
    created_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время создания отправления."
    )
    external_order: Optional[PostingFBOListExternalOrder] = Field(
        None, description="Информация о внешнем заказе."
    )
    financial_data: Optional[PostingFBOListFinancialData] = Field(
        None, description="Финансовые данные."
    )
    in_process_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время начала обработки."
    )
    legal_info: Optional[PostingFBOListLegalInfo] = Field(
        None, description="Юридическая информация."
    )
    order_id: Optional[int] = Field(None, description="Идентификатор заказа.")
    order_number: Optional[str] = Field(None, description="Номер заказа.")
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    products: Optional[list[PostingFBOListProduct]] = Field(
        None, description="Товары в отправлении."
    )
    status: Optional[str] = Field(None, description="Статус отправления.")
    substatus: Optional[str] = Field(None, description="Подстатус отправления.")


class PostingFBOListResponse(BaseModel):
    """Описывает схему ответа на запрос списка отправлений FBO (API v3).

    Attributes:
        cursor: Указатель для выборки следующих данных
        has_next: Признак, что в ответе вернулась только часть отправлений
        postings: Массив отправлений
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак, что в ответе вернулась только часть отправлений."
    )
    postings: Optional[list[PostingFBOListPosting]] = Field(
        None, description="Массив отправлений."
    )
