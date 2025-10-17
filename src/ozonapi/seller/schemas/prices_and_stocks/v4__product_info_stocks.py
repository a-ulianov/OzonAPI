"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoStocks"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.products import Visibility, ShipmentType
from .base import BaseRequestFilterSpec, BaseRequestCursorSpec
from ..base import BaseResponseCursor


class ProductInfoPricesRequestFilterWithQuant(BaseModel):
    """Фильтр товаров по тарифу Эконом.

    Attributes:
        created: Активные эконом-товары
        exists: Эконом-товары во всех статусах
    """
    created: bool = Field(
        ..., description="Активные эконом-товары."
    )
    exists: bool = Field(
        ..., description="Эконом-товары во всех статусах."
    )


class ProductInfoStocksFilter(BaseRequestFilterSpec):
    """Фильтр для запроса информации о количестве товаров по схемам FBS и rFBS.

    Attributes:
        offer_id (list[str]): Список offer_id (опционально, можно передавать до 1000 значений)
        product_id (list[int]): Список product_id (опционально, можно передавать до 1000 значений)
        visibility (Visibility): Фильтр по видимости товаров (опционально)
        with_quants: Товары по тарифу Эконом (опционально)
    """
    with_quants: Optional[ProductInfoPricesRequestFilterWithQuant] = Field(
        None, description="Товары по тарифу Эконом."
    )


class ProductInfoStocksRequest(BaseRequestCursorSpec):
    """Описывает схему запроса на получение информации о количестве товаров по схемам FBS и rFBS.

    Attributes:
        cursor (str): Указатель для выборки следующего чанка данных (опционально)
        filter: Фильтр по товарам (опционально)
        limit (int): Количество значений на странице (опционально, максимум 1000)
    """
    filter: Optional[ProductInfoStocksFilter] = Field(
        default_factory=ProductInfoStocksFilter, description="Фильтр по товарам."
    )


class ProductInfoStocksStock(BaseModel):
    """Информация об остатках.

    Attributes:
        present: Сейчас на складе
        reserved: Зарезервировано
        shipment_type: Тип упаковки
        sku: Идентификатор товара в системе Ozon
        type: Тип склада
        warehouse_ids: Идентификаторы складов
    """
    present: int = Field(
        ..., description="Сейчас на складе."
    )
    reserved: int = Field(
        ..., description="Зарезервировано."
    )
    shipment_type: ShipmentType = Field(
        ..., description="Тип упаковки."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )
    type: str = Field(
        ..., description="Тип склада."
    )
    warehouse_ids: list[int] = Field(
        ..., description="Идентификаторы складов, на которых хранился или хранится товар."
    )


class ProductInfoStocksItem(BaseModel):
    """Данные о количестве определенного товара по схемам FBS и rFBS.

    Attributes:
        offer_id: Идентификатор товара в системе продавца
        product_id: Идентификатор товара в системе продавца
        stocks: Информация об остатках
    """
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца — product_id."
    )
    stocks: list[ProductInfoStocksStock] = Field(
        ..., description="Информация об остатках."
    )


class ProductInfoStocksResponse(BaseResponseCursor):
    """Описывает схему ответа с информацией о количестве товаров по схемам FBS и rFBS.

    Attributes:
        cursor (str): Указатель для выборки следующего чанка данных
        items: Массив данных о количестве товаров FBS и rFBS
        total (int): Общее количество результатов
    """
    items: list[ProductInfoStocksItem] = Field(
        ..., description="Массив данных о количестве товаров FBS и rFBS."
    )