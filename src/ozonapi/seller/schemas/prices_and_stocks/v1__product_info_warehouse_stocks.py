"""Схемы метода product_info_warehouse_stocks (остатки на складе FBS и rFBS, v1)."""
import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductInfoWarehouseStocksRequest(BaseModel):
    """Описывает схему запроса информации по остаткам на складе FBS и rFBS (API v1).

    Attributes:
        cursor: Указатель для выборки следующих данных
        limit: Количество значений в ответе
        warehouse_id: Идентификатор склада
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    warehouse_id: int = Field(..., description="Идентификатор склада.")


class ProductInfoWarehouseStocksItem(BaseModel):
    """Данные об остатках товара на складе (API v1).

    Attributes:
        free_stock: Количество товара, доступное к продаже
        offer_id: Идентификатор товара в системе продавца — артикул
        present: Общее количество товара на складе
        product_id: Идентификатор товара в системе Ozon
        reserved: Количество зарезервированных товаров на складе
        sku: Идентификатор товара в системе Ozon — SKU
        updated_at: Дата и время последнего обновления остатков
        warehouse_id: Идентификатор склада
    """
    free_stock: Optional[int] = Field(
        None, description="Количество товара, доступное к продаже."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    present: Optional[int] = Field(None, description="Общее количество товара на складе.")
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon."
    )
    reserved: Optional[int] = Field(
        None, description="Количество зарезервированных товаров на складе."
    )
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    updated_at: Optional[datetime.datetime] = Field(
        None, description="Дата и время последнего обновления остатков."
    )
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class ProductInfoWarehouseStocksResponse(BaseModel):
    """Описывает схему ответа на запрос остатков на складе FBS и rFBS (API v1).

    Attributes:
        cursor: Указатель для выборки следующих данных
        has_next: Признак, что в ответе вернулась только часть значений
        stocks: Массив данных об остатках товаров
    """
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    has_next: Optional[bool] = Field(
        None, description="Признак, что в ответе вернулась только часть значений."
    )
    stocks: Optional[list[ProductInfoWarehouseStocksItem]] = Field(
        None, description="Массив данных об остатках товаров."
    )
