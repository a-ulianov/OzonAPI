"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFbpList"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.delivery import SortDir


class PostingFbpListFilter(BaseModel):
    """Фильтр списка отправлений FBP.

    Attributes:
        since: Начало периода (RFC3339)
        to: Конец периода (RFC3339)
        statuses: Статусы отправлений
        posting_numbers: Номера отправлений
        offer_id: Артикул товара в системе продавца
        name: Название товара
    """

    since: Optional[str] = Field(None, description="Начало периода в формате RFC3339.")
    to: Optional[str] = Field(None, description="Конец периода в формате RFC3339.")
    statuses: list[str] = Field(
        default_factory=list, description="Статусы отправлений."
    )
    posting_numbers: list[str] = Field(
        default_factory=list, description="Номера отправлений."
    )
    offer_id: Optional[str] = Field(
        None, description="Артикул товара в системе продавца."
    )
    name: Optional[str] = Field(None, description="Название товара.")


class PostingFbpListRequest(BaseModel):
    """Схема запроса списка отправлений FBP.

    Attributes:
        filter: Фильтр выборки
        limit: Количество значений в ответе
        cursor: Указатель для выборки следующих данных (курсорная пагинация)
        sort_by: Поле сортировки
        sort_dir: Направление сортировки
    """

    filter: Optional[PostingFbpListFilter] = Field(
        None, description="Фильтр выборки отправлений."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных (курсорная пагинация)."
    )
    sort_by: Optional[str] = Field(None, description="Поле сортировки.")
    sort_dir: Optional[SortDir] = Field(
        None, description="Направление сортировки (`ASC`/`DESC`)."
    )


class PostingFbpMoney(BaseModel):
    """Денежная сумма отправления FBP.

    Attributes:
        amount: Сумма (строка)
        currency: Код валюты
    """

    amount: Optional[str] = Field(None, description="Сумма (строка).")
    currency: Optional[str] = Field(None, description="Код валюты.")


class PostingFbpProduct(BaseModel):
    """Товар отправления FBP.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        name: Название товара
        offer_id: Артикул товара в системе продавца
        quantity: Количество товара
        price: Цена товара
        customer_price: Цена для покупателя
        seller_price: Цена продавца
    """

    sku: Optional[int] = Field(None, description="Идентификатор товара в системе Ozon — SKU.")
    name: Optional[str] = Field(None, description="Название товара.")
    offer_id: Optional[str] = Field(None, description="Артикул товара в системе продавца.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    price: Optional[PostingFbpMoney] = Field(None, description="Цена товара.")
    customer_price: Optional[PostingFbpMoney] = Field(None, description="Цена для покупателя.")
    seller_price: Optional[PostingFbpMoney] = Field(None, description="Цена продавца.")


class PostingFbpFinancialAction(BaseModel):
    """Акция, применённая к товару отправления FBP.

    Attributes:
        action_id: Идентификатор акции
        description: Описание акции
        date_from: Начало действия акции
        date_to: Конец действия акции
        discount_percent: Процент скидки
        discount_value: Размер скидки
        is_from_seller: Признак скидки от продавца
    """

    action_id: Optional[str] = Field(None, description="Идентификатор акции.")
    description: Optional[str] = Field(None, description="Описание акции.")
    date_from: Optional[str] = Field(None, description="Начало действия акции (RFC3339).")
    date_to: Optional[str] = Field(None, description="Конец действия акции (RFC3339).")
    discount_percent: Optional[float] = Field(None, description="Процент скидки.")
    discount_value: Optional[float] = Field(None, description="Размер скидки.")
    is_from_seller: Optional[bool] = Field(None, description="Признак скидки от продавца.")


class PostingFbpFinancialProduct(BaseModel):
    """Финансовые данные по товару отправления FBP.

    Attributes:
        product_id: Идентификатор товара
        quantity: Количество товара
        price: Цена товара
        old_price: Цена до скидок
        total_discount_percent: Суммарный процент скидки
        total_discount_value: Суммарный размер скидки
        commissions_currency_code: Код валюты комиссий
        actions: Применённые акции
    """

    product_id: Optional[int] = Field(None, description="Идентификатор товара.")
    quantity: Optional[int] = Field(None, description="Количество товара.")
    price: Optional[float] = Field(None, description="Цена товара.")
    old_price: Optional[float] = Field(None, description="Цена до скидок.")
    total_discount_percent: Optional[float] = Field(
        None, description="Суммарный процент скидки."
    )
    total_discount_value: Optional[float] = Field(
        None, description="Суммарный размер скидки."
    )
    commissions_currency_code: Optional[str] = Field(
        None, description="Код валюты комиссий."
    )
    actions: list[PostingFbpFinancialAction] = Field(
        default_factory=list, description="Применённые к товару акции."
    )


class PostingFbpFinancialData(BaseModel):
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
    products: list[PostingFbpFinancialProduct] = Field(
        default_factory=list, description="Финансовые данные по товарам."
    )


class PostingFbp(BaseModel):
    """Отправление FBP.

    Attributes:
        posting_number: Номер отправления
        order_id: Идентификатор заказа
        order_number: Номер заказа
        status: Статус отправления
        provider_id: Идентификатор провайдера доставки
        order_date: Дата заказа
        in_process_at: Дата перехода в обработку
        products: Товары отправления
        financial_data: Финансовые данные
    """

    posting_number: Optional[str] = Field(None, description="Номер отправления.")
    order_id: Optional[int] = Field(None, description="Идентификатор заказа.")
    order_number: Optional[str] = Field(None, description="Номер заказа.")
    status: Optional[str] = Field(
        None, description="Статус отправления (набор открытый — тип `str`)."
    )
    provider_id: Optional[int] = Field(None, description="Идентификатор провайдера доставки.")
    order_date: Optional[str] = Field(None, description="Дата заказа в формате RFC3339.")
    in_process_at: Optional[str] = Field(
        None, description="Дата перехода в обработку в формате RFC3339."
    )
    products: list[PostingFbpProduct] = Field(
        default_factory=list, description="Товары отправления."
    )
    financial_data: Optional[PostingFbpFinancialData] = Field(
        None, description="Финансовые данные отправления."
    )


class PostingFbpListResponse(BaseModel):
    """Схема ответа со списком отправлений FBP.

    Attributes:
        postings: Список отправлений
        cursor: Указатель для выборки следующих данных (курсорная пагинация)
    """

    postings: list[PostingFbp] = Field(
        default_factory=list, description="Список отправлений."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных (курсорная пагинация)."
    )
