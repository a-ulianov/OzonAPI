"""Схемы метода posting_digital_list (список цифровых отправлений, v2)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from .entities import BetaMoneyAmount


class PostingDigitalListFilter(BaseModel):
    """Фильтр выборки цифровых отправлений.

    Attributes:
        order_numbers: Номера заказов
        posting_numbers: Номера отправлений
        since: Начало периода (RFC3339)
        to_: Конец периода (RFC3339)
    """
    model_config = ConfigDict(populate_by_name=True)

    order_numbers: Optional[list[str]] = Field(None, description="Номера заказов.")
    posting_numbers: Optional[list[str]] = Field(
        None, description="Номера отправлений."
    )
    since: Optional[str] = Field(None, description="Начало периода (RFC3339).")
    to_: Optional[str] = Field(
        None, alias="to", description="Конец периода (RFC3339)."
    )


class PostingDigitalListWith(BaseModel):
    """Дополнительные поля в ответе.

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


class PostingDigitalListRequest(BaseModel):
    """Параметры запроса списка цифровых отправлений.

    Attributes:
        cursor: Указатель для выборки следующих данных
        filter: Фильтр выборки
        limit: Количество значений в ответе
        sort_dir: Направление сортировки (`ASC` или `DESC`)
        with_: Дополнительные поля в ответе
    """
    model_config = ConfigDict(populate_by_name=True)

    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    filter: Optional[PostingDigitalListFilter] = Field(
        None, description="Фильтр выборки."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки (`ASC` или `DESC`)."
    )
    with_: Optional[PostingDigitalListWith] = Field(
        None, alias="with", description="Дополнительные поля в ответе."
    )


class PostingDigitalListAdditionalData(BaseModel):
    """Дополнительные данные отправления.

    Attributes:
        key: Ключ
        value: Значение
    """
    key: Optional[str] = Field(None, description="Ключ.")
    value: Optional[str] = Field(None, description="Значение.")


class PostingDigitalListAnalyticsData(BaseModel):
    """Данные аналитики по отправлению.

    Attributes:
        city: Город доставки
        delivery_type: Способ доставки
        is_legal: Признак заказа юридического лица
        is_premium: Признак наличия подписки Premium
        payment_type_group_name: Способ оплаты
        region: Регион доставки
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    city: Optional[str] = Field(None, description="Город доставки.")
    delivery_type: Optional[str] = Field(None, description="Способ доставки.")
    is_legal: Optional[bool] = Field(
        None, description="Признак заказа юридического лица."
    )
    is_premium: Optional[bool] = Field(
        None, description="Признак наличия подписки Premium."
    )
    payment_type_group_name: Optional[str] = Field(None, description="Способ оплаты.")
    region: Optional[str] = Field(None, description="Регион доставки.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")
    warehouse_name: Optional[str] = Field(None, description="Название склада.")


class PostingDigitalListCancellation(BaseModel):
    """Информация об отмене отправления.

    Attributes:
        cancellation_initiator: Инициатор отмены
        cancellation_type: Тип отмены
    """
    cancellation_initiator: Optional[str] = Field(
        None, description="Инициатор отмены."
    )
    cancellation_type: Optional[str] = Field(None, description="Тип отмены.")


class PostingDigitalListExternalOrder(BaseModel):
    """Информация о внешнем заказе.

    Attributes:
        is_external: Признак внешнего заказа
        platform_name: Название площадки
    """
    is_external: Optional[bool] = Field(None, description="Признак внешнего заказа.")
    platform_name: Optional[str] = Field(None, description="Название площадки.")


class PostingDigitalListCommission(BaseModel):
    """Комиссия за товар.

    Attributes:
        amount: Сумма комиссии
        currency: Валюта
        percent: Процент комиссии
    """
    amount: Optional[float] = Field(None, description="Сумма комиссии.")
    currency: Optional[str] = Field(None, description="Валюта.")
    percent: Optional[int] = Field(None, description="Процент комиссии.")


class PostingDigitalListFinancialProduct(BaseModel):
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
    commission: Optional[PostingDigitalListCommission] = Field(
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


class PostingDigitalListFinancialData(BaseModel):
    """Финансовые данные отправления.

    Attributes:
        cluster_from: Кластер отправления
        cluster_to: Кластер доставки
        products: Финансовые данные по товарам
    """
    cluster_from: Optional[str] = Field(None, description="Кластер отправления.")
    cluster_to: Optional[str] = Field(None, description="Кластер доставки.")
    products: Optional[list[PostingDigitalListFinancialProduct]] = Field(
        None, description="Финансовые данные по товарам."
    )


class PostingDigitalListLegalInfo(BaseModel):
    """Юридическая информация о покупателе.

    Attributes:
        company_name: Название компании
        inn: ИНН
        kpp: КПП
    """
    company_name: Optional[str] = Field(None, description="Название компании.")
    inn: Optional[str] = Field(None, description="ИНН.")
    kpp: Optional[str] = Field(None, description="КПП.")


class PostingDigitalListProduct(BaseModel):
    """Товар в цифровом отправлении.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        price: Цена товара
        quantity: Количество товара
        required_qty_for_digital_code: Требуемое количество для цифрового кода
        sku: Идентификатор товара в системе Ozon — SKU
    """
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[BetaMoneyAmount] = Field(None, description="Цена товара.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    required_qty_for_digital_code: Optional[int] = Field(
        None, description="Требуемое количество для цифрового кода."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )


class PostingDigitalListPosting(BaseModel):
    """Цифровое отправление.

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
        waiting_deadline_for_digital_code: Срок ожидания цифрового кода
    """
    additional_data: Optional[list[PostingDigitalListAdditionalData]] = Field(
        None, description="Дополнительные данные."
    )
    analytics_data: Optional[PostingDigitalListAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    cancel_reason_id: Optional[int] = Field(
        None, description="Идентификатор причины отмены."
    )
    cancellation: Optional[PostingDigitalListCancellation] = Field(
        None, description="Информация об отмене."
    )
    created_at: Optional[str] = Field(
        None, description="Дата и время создания отправления."
    )
    external_order: Optional[PostingDigitalListExternalOrder] = Field(
        None, description="Информация о внешнем заказе."
    )
    financial_data: Optional[PostingDigitalListFinancialData] = Field(
        None, description="Финансовые данные."
    )
    in_process_at: Optional[str] = Field(
        None, description="Дата и время начала обработки."
    )
    legal_info: Optional[PostingDigitalListLegalInfo] = Field(
        None, description="Юридическая информация."
    )
    order_id: Optional[int] = Field(None, description="Идентификатор заказа.")
    order_number: Optional[str] = Field(None, description="Номер заказа.")
    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    products: Optional[list[PostingDigitalListProduct]] = Field(
        None, description="Товары в отправлении."
    )
    status: Optional[str] = Field(None, description="Статус отправления.")
    waiting_deadline_for_digital_code: Optional[str] = Field(
        None, description="Срок ожидания цифрового кода."
    )


class PostingDigitalListResponse(BaseModel):
    """Ответ со списком цифровых отправлений.

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
    postings: Optional[list[PostingDigitalListPosting]] = Field(
        None, description="Массив отправлений."
    )
