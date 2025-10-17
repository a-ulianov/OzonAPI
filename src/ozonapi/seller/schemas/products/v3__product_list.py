"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductList"""
from typing import Optional

from pydantic import BaseModel, Field

from .base import BaseProductListFilter
from ..base import BaseRequestLastId, BaseRequestLimit1000, BaseResponseLastId


class ProductListFilter(BaseProductListFilter):
    """Модель фильтра для получения списка товаров.
    Позволяет фильтровать товары по артикулу, идентификатору и видимости.

    Attributes:
        offer_id: Фильтр по параметру offer_id
        product_id: Фильтр по параметру product_id
        visibility: Видимость товара
    """
    pass


class ProductListRequest(BaseRequestLimit1000, BaseRequestLastId):
    """Модель запроса для получения списка товаров.

    Attributes:
        filter: Фильтр товаров
        last_id: Идентификатор последнего товара для пагинации
        limit: Максимальное количество товаров в ответе (максимум 1000)
    """
    filter: Optional[ProductListFilter] = Field(
        default_factory=ProductListFilter, description="Фильтр выборки товаров."
    )


class ProductListQuants(BaseModel):
    """Информация о кванте.

    Attributes:
        quant_code: Идентификатор эконом-товара
        quant_size: Размер кванта
    """
    quant_code: str = Field(
        ..., description="Идентификатор эконом-товара."
    )
    quant_size: int = Field(
        ..., description="Размер кванта."
    )


class ProductListResponseItem(BaseModel):
    """Модель одного товара в списке товаров.

    Attributes:
        archived: Признак товара в архиве
        has_fbo_stocks: Наличие остатков на складах FBO
        has_fbs_stocks: Наличие остатков на складах FBS
        is_discounted: Признак уценённого товара
        product_id: Идентификатор товара в системе Ozon
        offer_id: Артикул товара
        quants: Массив с информацией о товарных квантах
    """
    archived: bool = Field(
        ..., description="Признак товара в архиве."
    )
    has_fbo_stocks: bool = Field(
        ..., description="Есть остатки на складах FBO."
    )
    has_fbs_stocks: bool = Field(
        ..., description="Есть остатки на складах FBS."
    )
    is_discounted: bool = Field(
        ..., description="Уценённый товар."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon."
    )
    offer_id: str = Field(
        ..., description="Артикул товара."
    )
    quants: list[ProductListQuants] = Field(
        default_factory=list, description="Массив с информацией о товарных квантах."
    )


class ProductListResponseResult(BaseResponseLastId):
    """Информация об отобранных товарах и их количестве.

    Attributes:
        items: Список товаров
        total: Общее количество товаров
        last_id: Идентификатор последнего товара для пагинации
    """
    items: list[ProductListResponseItem] = Field(
        ..., description="Список товаров"
    )


class ProductListResponse(BaseModel):
    """
    Модель ответа на запрос списка товаров.

    Attributes:
        result: Ответ с данными о товарах
    """
    result: ProductListResponseResult = Field(
        ..., description="Информация о выбранных товарах и их количестве."
    )
