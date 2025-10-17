"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoSubscription"""
from pydantic import BaseModel, Field


class ProductInfoSubscriptionRequest(BaseModel):
    """Описывает схему запроса для получения количества пользователей, которые нажали `Узнать о поступлении` на странице товара.

    Attributes:
        skus: Список SKU, идентификаторов товара в системе Ozon
    """
    skus: list[int] = Field(
        ..., description="Список SKU, идентификаторов товара в системе Ozon."
    )


class ProductInfoSubscriptionItem(BaseModel):
    """Информация о количестве подписавшихся на поступление товара пользователей.

    Attributes:
        sku: Идентификатор товара в системе Ozon, SKU
        count: Количество подписавшихся пользователей
    """
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon, SKU."
    )
    count: int = Field(
        ..., description="Количество подписавшихся пользователей."
    )


class ProductInfoSubscriptionResponse(BaseModel):
    """Описывает схему ответа на запрос о получении количества пользователей, которые нажали `Узнать о поступлении` на странице товара.

    Attributes:
        result: Массив с информацией о подписавшихся на поступление товаров пользователей
    """
    result: list[ProductInfoSubscriptionItem] = Field(
        ..., description="Массив с информацией о подписавшихся на поступление товаров пользователей."
    )
