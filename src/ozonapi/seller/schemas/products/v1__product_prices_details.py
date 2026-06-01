"""https://docs.ozon.ru/api/seller/#operation/ProductPricesDetails"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductPricesDetailsRequest(BaseModel):
    """Схема запроса подробной информации о ценах товаров (Premium).

    Attributes:
        skus: Список SKU товаров
    """

    skus: list[str] = Field(
        ..., description="Список SKU товаров.", min_length=1
    )


class ProductPricesDetailsMoney(BaseModel):
    """Денежная сумма.

    Attributes:
        amount: Сумма
        currency: Валюта
    """

    amount: Optional[str] = Field(
        None, description="Сумма."
    )
    currency: Optional[str] = Field(
        None, description="Валюта."
    )


class ProductPricesDetailsIndexData(BaseModel):
    """Данные ценового индекса товара.

    Attributes:
        min_price: Минимальная цена товара
        price_index: Значение ценового индекса
        url: Ссылка на товар-эталон
    """

    min_price: Optional[ProductPricesDetailsMoney] = Field(
        None, description="Минимальная цена товара."
    )
    price_index: Optional[float] = Field(
        None, description="Значение ценового индекса."
    )
    url: Optional[str] = Field(
        None, description="Ссылка на товар-эталон."
    )


class ProductPricesDetailsPriceIndex(BaseModel):
    """Ценовые индексы товара.

    Attributes:
        external_index_data: Индекс по ценам конкурентов на других площадках
        self_index_data: Индекс по ценам этого же товара на Ozon
    """

    external_index_data: Optional[ProductPricesDetailsIndexData] = Field(
        None, description="Индекс по ценам конкурентов на других площадках."
    )
    self_index_data: Optional[ProductPricesDetailsIndexData] = Field(
        None, description="Индекс по ценам этого же товара на Ozon."
    )


class ProductPricesDetailsPrice(BaseModel):
    """Подробная информация о ценах товара.

    Attributes:
        sku: SKU товара
        offer_id: Идентификатор товара в системе продавца — артикул
        price: Цена товара
        customer_price: Цена для покупателя
        discount_percent: Процент скидки
        price_indexes: Ценовые индексы товара
    """

    sku: Optional[int] = Field(
        None, description="SKU товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    price: Optional[ProductPricesDetailsMoney] = Field(
        None, description="Цена товара."
    )
    customer_price: Optional[ProductPricesDetailsMoney] = Field(
        None, description="Цена для покупателя."
    )
    discount_percent: Optional[float] = Field(
        None, description="Процент скидки."
    )
    price_indexes: Optional[list[ProductPricesDetailsPriceIndex]] = Field(
        None, description="Ценовые индексы товара."
    )


class ProductPricesDetailsResponse(BaseModel):
    """Схема ответа с подробной информацией о ценах товаров.

    Attributes:
        prices: Список товаров с подробной информацией о ценах
    """

    prices: list[ProductPricesDetailsPrice] = Field(
        default_factory=list, description="Список товаров с подробной информацией о ценах."
    )
